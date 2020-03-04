import mysql.connector
import sys
import home_page
import ad
import hashlib
import random

from sanic import Sanic, response
from time import sleep

app = Sanic()

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

@app.route("/home")
async def basic(request):
	# show user menu
	companies = []

	connect_db()
	# gey all companies
	cursor.callproc('SEARCH_ALL_COMPANIES', [])
	for res in cursor.stored_results():
		comps = res.fetchall()

		for _ in range(6):
			c = random.choice(comps)
			companies.append(c[0])
			comps.remove(c)
	cursor.close()

	return response.html(home_page.get_html(companies))

@app.route("/ad")
async def start(request):
	# redirect to home or login
	if len(request.args) == 0 or 'company' not in request.args.keys():
		return response.redirect('/home')


	info = []
	connect_db()
	cursor.callproc('SEARCH_COMPANY_BY_NAME_PLUS', [request.args['company'][0]])
	for res in cursor.stored_results():
		for i in res.fetchall():
			info = i
	cursor.close()

	return response.html(ad.get_html(info))

@app.route("/")
async def start(request):
	# redirect to home or login
	return response.redirect('/home')

if __name__ == "__main__":
	connect_db()
	cursor.close()
	
	app.static('/ads.jpg', '/app/ads.jpg', name='ads_jpg')
	app.static('/business.jpg', '/app/business.jpg', name='business_jpg')
	app.static('/a.jpg', '/app/a.jpg', name='a_jpg')
	app.static('/b.png', '/app/b.png', name='b_png')
	app.static('/c.jpg', '/app/c.jpg', name='c_jpg')
	app.static('/d.jpg', '/app/d.jpg', name='d_jpg')
	app.static('/e.jpg', '/app/e.jpg', name='e_jpg')
	app.static('/f.jpg', '/app/f.jpg', name='f_jpg')

	app.run(host="0.0.0.0", port=82)