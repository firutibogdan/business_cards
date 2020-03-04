import mysql.connector
import sys
import home_page
import login_page
import search_name_page
import search_city_page
import search_company_page
import search_job_page
import search_all_page
import search_all_company_page
import search_company_name_page
import search_company_domain_page
import search_company_city_page
import search_email_page
import search_logs
import company_data_page
import search_company_name_edit_page
import user_data_page
import check_company_name
import success
import hashlib

from sanic import Sanic, response
from sanic_httpauth import HTTPBasicAuth
from time import sleep

app = Sanic()
auth = HTTPBasicAuth()

connection = None
cursor = None

# connect to the database
def connect_db():
	global connection
	global cursor

	ok = False

	# try to connect to database
	while not ok:
		try:
			connection = mysql.connector.connect(
				host='db',
				user='root',
				password='password',
				port='3306',
				database='CARDS'
			)
			ok = True
		except:
			ok = False

	cursor = connection.cursor()

@app.route("/logs")
@auth.login_required
async def show_logs(request):
	# show logs only for admin
	if auth.username(request) != 'admin':
		return response.redirect('/home')

	text = ''
	connect_db()
	# call procedure and prin result
	cursor.callproc('SHOW_LOGS', [])
	for res in cursor.stored_results():
		text = search_logs.get_html(res.fetchall())
	cursor.close()

	return response.html(text)

@app.route("/my_data", methods=['GET', 'POST'])
@auth.login_required
async def my_data(request):
	if request.method == 'POST':
		# get data from input form
		name = request.form.get('name')
		surname = request.form.get('surname')
		phone = request.form.get('phone')
		email = request.form.get('email')
		password = request.form.get('password')
		birthday = request.form.get('birthday')
		company_name = request.form.get('company_name')
		department = request.form.get('department')
		job = request.form.get('job')
		country = request.form.get('country')
		city = request.form.get('city')

		connect_db()
		# check if company exists
		cursor.callproc('CHECK_COMPANY_NAME', [company_name])
		for res in cursor.stored_results():
			ok = res.fetchone()[0]
		cursor.close()

		connect_db()
		# update user to database
		if password != '******':
			password = hashlib.sha256(password.encode()).hexdigest()
			cursor.callproc('UPDATE_PERSON', [auth.username(request), name, surname, phone, email, password, birthday, company_name, department, job, country, city])
		else:
			cursor.callproc('UPDATE_PERSON_NO_PASS', [auth.username(request), name, surname, phone, email, birthday, company_name, department, job, country, city])
		cursor.close()

		if ok == 0:
			# if company not present, set data for it
			return response.redirect('/edit_c_info_user?name=' + company_name)

		return response.redirect('/success')

	connect_db()
	# get data for current user
	cursor.callproc('SEARCH_BY_EMAIL', [auth.username(request)])

	# add data tfrom database o form
	for res in cursor.stored_results():
		person = res.fetchall()[0]

		name = person[0]
		surname = person[1]
		phone = person[2]
		email = person[3]
		password = person[4]
		birthday = person[5].strftime("%Y-%m-%d")
		job = person[6]
		department = person[7]
		company_name = person[8]
		city = person[9]
		country = person[10]

		text = search_email_page.get_html(name, surname, phone, email, password, birthday, company_name, department, job, country, city)
	cursor.close()
	
	return response.html(text)

@app.route("/delete_info")
@auth.login_required
async def delete_info(request):
	# delete user by email
	if 'email' not in request.args.keys():
		return response.redirect('/all')
	
	# get current user
	old_email = request.args['email'][0]

	# check if user is deleting his account
	if auth.username(request) != old_email and auth.username(request) != 'admin':
		return response.redirect('/home')

	connect_db()
	# delete account
	cursor.callproc('DELETE_BY_EMAIL', [old_email])
	cursor.close()
	
	if auth.username(request) == 'admin':
		return response.redirect('/all')
	return response.redirect('/logout')


@app.route("/delete_c_info")
@auth.login_required
async def delete_c_info(request):
	# only admin can delete company by name
	if 'name' not in request.args.keys() or auth.username(request) != 'admin':
		return response.redirect('/all_companies')
	
	# get company name
	old_name = request.args['name'][0]

	connect_db()
	# delete company
	cursor.callproc('DELETE_COMPANY_BY_NAME', [old_name])
	cursor.close()

	return response.redirect('/all_companies')


@app.route("/edit_info", methods=['GET', 'POST'])
@auth.login_required
async def edit_info(request):
	# edit user info only by admin
	if 'email' not in request.args.keys() or auth.username(request) != 'admin':
		return response.redirect('/all')

	# get user email
	old_email = request.args['email'][0]

	if request.method == 'POST':
		# get user data
		name = request.form.get('name')
		surname = request.form.get('surname')
		phone = request.form.get('phone')
		email = request.form.get('email')
		password = request.form.get('password')
		birthday = request.form.get('birthday')
		company_name = request.form.get('company_name')
		department = request.form.get('department')
		job = request.form.get('job')
		country = request.form.get('country')
		city = request.form.get('city')

		connect_db()
		# check if company exists
		cursor.callproc('CHECK_COMPANY_NAME', [company_name])
		for res in cursor.stored_results():
			ok = res.fetchone()[0]
		cursor.close()

		connect_db()
		# update user data
		if password != '******':
			password = hashlib.sha256(password.encode()).hexdigest()
			cursor.callproc('UPDATE_PERSON', [old_email, name, surname, phone, email, password, birthday, company_name, department, job, country, city])
		else:
			cursor.callproc('UPDATE_PERSON_NO_PASS', [old_email, name, surname, phone, email, birthday, company_name, department, job, country, city])
		cursor.close()

		if ok == 0:
			# if company not present, set data for it
			return response.redirect('/edit_c_info?name=' + company_name)

		return response.redirect('/all')

	connect_db()
	cursor.callproc('SEARCH_BY_EMAIL', [old_email])
	for res in cursor.stored_results():
		# get user data to complete form with data from database
		person = res.fetchall()[0]

		name = person[0]
		surname = person[1]
		phone = person[2]
		email = person[3]
		password = person[4]
		birthday = person[5].strftime("%Y-%m-%d")
		job = person[6]
		department = person[7]
		company_name = person[8]
		city = person[9]
		country = person[10]

		text = search_email_page.get_html(name, surname, phone, email, password, birthday, company_name, department, job, country, city)
	cursor.close()
	
	return response.html(text)

@app.route("/edit_c_info_user", methods=['GET', 'POST'])
@auth.login_required
async def edit_c_info_user(request):
	# edit company info by any user (when new company added)
	if 'name' not in request.args.keys():
		return response.redirect('/home')

	# get company name
	old_name = request.args['name'][0]

	if request.method == 'POST':
		# get company info
		name = request.form.get('name')
		phone = request.form.get('phone')
		email = request.form.get('email')
		address = request.form.get('address')
		domain = request.form.get('domain')
		country = request.form.get('country')
		city = request.form.get('city')

		connect_db()
		# update company info
		cursor.callproc('UPDATE_COMPANY', [old_name, name, phone, email, address, domain, country, city])
		cursor.close()

		return response.redirect('/success')

	connect_db()
	cursor.callproc('SEARCH_COMPANY_BY_NAME', [old_name])
	for res in cursor.stored_results():
		# get company data from database and complete form
		company = res.fetchall()[0]

		name = company[0]
		phone = company[1]
		email = company[2]
		address = company[3]
		domain = company[4]
		city = company[5]
		country = company[6]

		text = search_company_name_edit_page.get_html(name, phone, email, address, domain, country, city)
	cursor.close()
	
	return response.html(text)

@app.route("/edit_c_info", methods=['GET', 'POST'])
@auth.login_required
async def edit_c_info(request):
	# edit company info only by admin
	if 'name' not in request.args.keys() or auth.username(request) != 'admin':
		return response.redirect('/all_companies')

	# get company name
	old_name = request.args['name'][0]

	if request.method == 'POST':
		# get company data from form
		name = request.form.get('name')
		phone = request.form.get('phone')
		email = request.form.get('email')
		address = request.form.get('address')
		domain = request.form.get('domain')
		country = request.form.get('country')
		city = request.form.get('city')

		connect_db()
		# update company info
		cursor.callproc('UPDATE_COMPANY', [old_name, name, phone, email, address, domain, country, city])
		cursor.close()

		return response.redirect('/all_companies')

	connect_db()
	# get company info from database
	cursor.callproc('SEARCH_COMPANY_BY_NAME', [old_name])

	for res in cursor.stored_results():
		# complete form with info
		company = res.fetchall()[0]

		name = company[0]
		phone = company[1]
		email = company[2]
		address = company[3]
		domain = company[4]
		city = company[5]
		country = company[6]

		text = search_company_name_edit_page.get_html(name, phone, email, address, domain, country, city)
	cursor.close()
	
	return response.html(text)

@app.route("/home")
@auth.login_required
async def basic(request):
	# show user menu
	if auth.username(request) == 'admin':
		return response.html(home_page.get_html(True, 'admin'))
	return response.html(home_page.get_html(False, auth.username(request)))

@app.route("/success")
@auth.login_required
async def success_op(request):
	# show success on modifications
	return response.html(success.get_html())

@app.route("/")
@auth.login_required
async def start(request):
	# redirect to home or login
	return response.redirect('/home')

@app.route('/check_company_name', methods=['GET', 'POST'])
async def check_company_name_func(request):
	if request.method == 'POST':
		name = request.form.get('name')

		connect_db()
		# check if company exists
		cursor.callproc('CHECK_COMPANY_NAME', [name])
		for res in cursor.stored_results():
			ok = res.fetchone()[0]
		cursor.close()

		if ok != 0:
			return response.redirect('/user_data')
		return response.redirect('/company_data')
	return response.html(check_company_name.get_html())

@auth.verify_password
def verify_password(username, password):
	username = username
	password = hashlib.sha256(password.encode()).hexdigest()

	ok = False

	if username == 'admin' and 	password == hashlib.sha256(b'admin').hexdigest():
		ok = True

	if not ok:
		connect_db()
		ok = False
		
		# check if login is successful
		cursor.callproc('LOGIN_USER', [username, password])
		for res in cursor.stored_results():
			if res.fetchone()[0] == 1:
				ok = True
		cursor.close()

	if ok:
		return True
	return False

@app.route('/user_data', methods=['GET', 'POST'])
async def user_data(request):
	if request.method == 'POST':
		# get new user data from form
		name = request.form.get('name')
		surname = request.form.get('surname')
		phone = request.form.get('phone')
		email = request.form.get('email')
		password = hashlib.sha256(request.form.get('password').encode()).hexdigest()
		birthday = request.form.get('birthday')
		company_name = request.form.get('company_name')
		department = request.form.get('department')
		job = request.form.get('job')
		country = request.form.get('country')
		city = request.form.get('city')

		connect_db()
		# check email if already exists
		cursor.callproc('CHECK_EMAIL', [email])
		for res in cursor.stored_results():
			ok = res.fetchone()[0]
		cursor.close()

		if ok != 0:
			return response.html(user_data_page.get_html("Email already used!"))

		connect_db()
		# check if company exists
		cursor.callproc('CHECK_COMPANY_NAME', [company_name])
		for res in cursor.stored_results():
			ok = res.fetchone()[0]
		cursor.close()

		if ok == 0:
			return response.redirect('/company_data')

		connect_db()
		# add user data to database
		cursor.callproc('ADD_PERSON', [name, surname, phone, email, password, birthday, company_name, department, job, country, city])
		cursor.close()

		return response.redirect('/success')

	return response.html(user_data_page.get_html(''))

@app.route('/company_data', methods=['GET', 'POST'])
async def company_data(request):
	if request.method == 'POST':
		# get new company data from form
		name = request.form.get('name')
		phone = request.form.get('phone')
		email = request.form.get('email')
		address = request.form.get('address')
		domain = request.form.get('domain')
		country = request.form.get('country')
		city = request.form.get('city')
		latitude = float(request.form.get('latitude').replace(',', '.'))
		longitude = float(request.form.get('longitude').replace(',', '.'))

		connect_db()
		# add company to database
		cursor.callproc('ADD_COMPANY', [name, phone, email, address, domain, country, city, latitude, longitude])
		cursor.close()

		return response.redirect('/user_data')

	return response.html(company_data_page.get_html())

@app.route('/logout')
@auth.login_required
def Logout(request):
	return response.redirect('/home', status = 401)

@app.route("/search_name", methods=['GET', 'POST'])
@auth.login_required
async def search_name(request):
	if request.method == 'POST':
		name = request.form.get('name')

		connect_db()
		# search person by name
		cursor.callproc('SEARCH_BY_NAME', [name])
		for res in cursor.stored_results():
			text = search_name_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_name_page.get_html(False, None))

@app.route("/search_city", methods=['GET', 'POST'])
@auth.login_required
async def search_city(request):
	if request.method == 'POST':
		city = request.form.get('city')

		connect_db()
		# search person by city
		cursor.callproc('SEARCH_BY_CITY', [city])
		for res in cursor.stored_results():
			text = search_city_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_city_page.get_html(False, None))

@app.route("/search_company_name", methods=['GET', 'POST'])
@auth.login_required
async def search_company_name(request):
	if request.method == 'POST':
		name = request.form.get('name')

		connect_db()
		# search company by name
		cursor.callproc('SEARCH_COMPANY_BY_NAME', [name])
		for res in cursor.stored_results():
			text = search_company_name_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_company_name_page.get_html(False, None))

@app.route("/search_company_domain", methods=['GET', 'POST'])
@auth.login_required
async def search_company_domain(request):
	if request.method == 'POST':
		domain = request.form.get('domain')

		connect_db()
		# search company by domain
		cursor.callproc('SEARCH_COMPANY_BY_DOMAIN', [domain])
		for res in cursor.stored_results():
			text = search_company_domain_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_company_domain_page.get_html(False, None))

@app.route("/search_company_city", methods=['GET', 'POST'])
@auth.login_required
async def search_company_city(request):
	if request.method == 'POST':
		city = request.form.get('city')

		connect_db()
		# search company by city
		cursor.callproc('SEARCH_COMPANY_BY_CITY', [city])
		for res in cursor.stored_results():
			text = search_company_city_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_company_city_page.get_html(False, None))

@app.route("/search_company", methods=['GET', 'POST'])
@auth.login_required
async def search_company(request):
	if request.method == 'POST':
		company = request.form.get('company')

		connect_db()
		# search person by company name
		cursor.callproc('SEARCH_BY_COMPANY', [company])
		for res in cursor.stored_results():
			text = search_company_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_company_page.get_html(False, None))

@app.route("/search_job", methods=['GET', 'POST'])
@auth.login_required
async def search_job(request):
	if request.method == 'POST':
		job = request.form.get('job')

		connect_db()
		# search person by job
		cursor.callproc('SEARCH_BY_JOB', [job])
		for res in cursor.stored_results():
			text = search_job_page.get_html(True, res.fetchall())
		cursor.close()
		return response.html(text)
	
	return response.html(search_job_page.get_html(False, None))


@app.route("/all")
@auth.login_required
async def all(request):
	text = ''
	connect_db()
	# show all persons
	cursor.callproc('SEARCH_ALL', [])
	for res in cursor.stored_results():
		if auth.username(request) == 'admin':
			text = search_all_page.get_html(True, res.fetchall())
		else:
			text = search_all_page.get_html(False, res.fetchall())
	cursor.close()
	
	return response.html(text)

@app.route("/all_companies")
@auth.login_required
async def all_companies(request):
	text = ''
	connect_db()
	# show all companies
	cursor.callproc('SEARCH_ALL_COMPANIES', [])
	for res in cursor.stored_results():
		if auth.username(request) == 'admin':
			text = search_all_company_page.get_html(True, res.fetchall())
		else:
			text = search_all_company_page.get_html(False, res.fetchall())
	cursor.close()
	
	return response.html(text)

if __name__ == "__main__":

	# # mock-up data
	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['ITSecBF', '0742-422-346', 'hr@itsecbf.com', 'Str. Dorobanti, Nr. 44', 'Internet Security', 'Romania', 'Bucharest', 44.437019, 26.086546])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['FlowerRose', '0742-422-333', 'hr@flowerrose.com', 'Str. Anghel Petru, Nr. 21', 'Agriculture', 'Romania', 'Cluj-Napoca', 46.775389, 23.607987])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['Regio', '0742-422-297', 'apa@regio.com', 'Str. Geneva, Nr. 124', 'Water Provider', 'Romania', 'Bucharest', 44.440619, 26.082736])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['GasBack', '0743-322-546', 'gas@back.com', 'Str. Aluminiului, Nr. 21', 'Gas', 'Romania', 'Bucharest', 44.435763, 26.111755])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['FoodFood', '0729-395-283', 'hr@foodfood.com', 'Str. Mircea Bades, Nr. 1', 'Food', 'Romania', 'Iasi', 47.159092, 27.615032])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['BricoHouse', '0711-432-229', 'brico@brico.com', 'Str. Gargaritei, Nr. 29', 'House', 'Romania', 'Bucharest', 44.443971, 26.138219])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['PubliciTaT', '0763-123-334', 'pub@pub.com', 'Str. Alioanei, Nr. 95', 'Publiciy', 'Romania', 'Targu Mures', 46.542835, 24.573699])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['FlowerPot', '0712-234-558', 'pr@flowerpot.com', 'Str. Petru Rares, Nr. 139', 'Agriculture', 'Romania', 'Craiova', 44.316589, 23.819930])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['SmartPhone', '0722-199-349', 'smart@smartphone.com', 'Drumul Sarii, Nr. 9', 'Mobile Phones', 'Romania', 'Arad', 46.180103, 21.304070])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_COMPANY', ['MichaMich', '0744-542-330', 'micha@michamich.com', 'Bulevardul Revolutiei, Nr. 279', 'Hypermarket', 'Spain', 'Barcelona', 41.386158, 2.149816])
	# cursor.close()

	# # mock-up data
	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Popescu', 'George', '0744-204-589', 'george.popescu@yahoo.com', hashlib.sha256(b'gPope3').hexdigest(), '1999-05-08', 'ITSecBF', 'IT', 'Junior Programmer', 'Romania', 'Bucharest'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Popescu', 'Mihai', '0744-204-588', 'mihai.popescu@yahoo.com', hashlib.sha256(b'mPope3').hexdigest(), '1999-05-07', 'ITSecBF', 'IT', 'Junior Programmer', 'Romania', 'Timisoara'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Popescu', 'Ion', '0744-204-587', 'ion.popescu@yahoo.com', hashlib.sha256(b'iPope3').hexdigest(), '1999-05-06', 'ITSecBF', 'IT', 'Junior Programmer', 'Romania', 'Timisoara'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Mircea', 'Gheorghe', '0744-234-187', 'mircea.gheorghe@yahoo.com', hashlib.sha256(b'gMirc5').hexdigest(), '1992-12-03', 'FlowerRose', 'Sales', 'Shop Assistant', 'Romania', 'Cluj'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Fracu', 'Mihai', '0724-304-187', 'mihai.fracu@yahoo.com', hashlib.sha256(b'mFrac5').hexdigest(), '1991-04-02', 'FlowerRose', 'IT', 'Database Keeper', 'Romania', 'Cluj'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Mica', 'Alina', '0722-219-483', 'micaalin@yahoo.com', hashlib.sha256(b'aMica6').hexdigest(), '1988-03-12', 'Regio', 'HR', 'HR Chief', 'Romania', 'Bucharest'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Cescu', 'Catalina', '0799-234-188', 'ccatalin@yahoo.com', hashlib.sha256(b'cCesc6').hexdigest(), '1989-11-04', 'Regio', 'Sales', 'SEO', 'France', 'Paris'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Ceausu', 'Mihnea', '0714-222-345', 'mceausu@gmail.com', hashlib.sha256(b'mCeau9').hexdigest(), '1996-12-03', 'MichaMich', 'Sales', 'SEO', 'Spain', 'Barcelona'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Dodo', 'Adelina', '0749-299-999', 'dadelina@yahoo.com', hashlib.sha256(b'aDodo1').hexdigest(), '1986-06-24', 'FlowerPot', 'HR', 'Personal', 'Romania', 'Timisoara'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_PERSON', ['Cosma', 'Catrina', '0788-149-227', 'ccatrina@gmail.com', hashlib.sha256(b'cCosm2').hexdigest(), '1955-01-01', 'BricoHouse', 'Sales', 'Shop Assistant', 'Romania', 'Constanta'])
	# cursor.close()

	# connect_db()
	# cursor.callproc('ADD_MSG', ['mihai.popescu@yahoo.com', 'dadelina@yahoo.com', 'Buna! Ce mai faci?'])
	# cursor.close()

	# sleep(1)

	# connect_db()
	# cursor.callproc('ADD_MSG', ['dadelina@yahoo.com', 'mihai.popescu@yahoo.com', 'Hello! Pe la munca. Tu?'])
	# cursor.close()

	connect_db()
	cursor.close()

	app.run(host="0.0.0.0", port=80)