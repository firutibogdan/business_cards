import mysql.connector
import sys
import home_page
import login_page
import chatter
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

@app.route("/home", methods=['GET', 'POST'])
@auth.login_required
async def basic(request):
	# show user menu
	if request.method == 'POST':
		username = request.form.get('username')
		return response.redirect('/chatter?friend=' + username)
	return response.html(home_page.get_html(auth.username(request).split('@')[0]))

@app.route("/chatter", methods=['GET', 'POST'])
@auth.login_required
async def start(request):
	# redirect to home or login
	if len(request.args) == 0 or 'friend' not in request.args.keys():
		return response.redirect('/home')

	if request.method == 'POST':
		message = request.form.get('message')
		connect_db()
		cursor.callproc('ADD_MSG', [auth.username(request), request.args['friend'][0], message])
		cursor.close()
		return response.redirect('/chatter?friend=' + request.args['friend'][0])

	msgs = ''
	connect_db()
	# through last messages
	cursor.callproc('SHOW_LAST_MSGS', [auth.username(request), request.args['friend'][0]])
	for res in cursor.stored_results():
		for msg in res.fetchall():
			if msg[2] == auth.username(request):
				msgs = "You: " + msg[1] + '\n' + msgs
			else:
				msgs = request.args['friend'][0].split('@')[0] + ': ' + msg[1] + '\n' + msgs
	cursor.close()

	return response.html(chatter.get_html(auth.username(request), request.args['friend'][0], msgs))

@app.route("/")
@auth.login_required
async def start(request):
	# redirect to home or login
	return response.redirect('/home')


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

@app.route('/logout')
@auth.login_required
def Logout(request):
	return response.redirect('/home', status = 401)

if __name__ == "__main__":
	connect_db()
	cursor.close()

	app.run(host="0.0.0.0", port=81)