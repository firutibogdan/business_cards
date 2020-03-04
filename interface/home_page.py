
def get_html(admin, username):
	text = '''
			<html>
			<head>
			<style>
			div {
				background-color: #e6e6e6;
				width: 40%;
				border: 15px solid #006600;
				padding: 50px;
				position: absolute;
				top: 15%;
				left: 25%;
			}

			.button {
				display: inline-block;
				padding: 6px 10px;
				font-size: 12px;
				cursor: pointer;
				text-align: center;
				text-decoration: none;
				outline: none;
				color: #663300;
				background-color: #cce5ff;
				border: none;
				border-radius: 15px;
				box-shadow: 0 9px #999;
				font-family:courier;
			}

			.button:hover {background-color: #80bdff}

			.button:active {
				background-color: #4da3ff;
				box-shadow: 0 5px #666;
				transform: translateY(4px);
			}
			</style>
			</head>
			<body>

				<div align="center">
				<h2>Welcome, ''' + username + '''!</h2>
				'''
	
	if admin:
		text += '''<button onclick="showDashboard()" class="button">Show Statistics</button><br><br>
					<button onclick="myLogs()" class="button">Logs</button><br><br>'''
	else:
		text += '''<button onclick="myInfo()" class="button">My info</button><br><br>'''

	text += ''' <button onclick="searchName()" class="button">Search Person by Name</button><br><br>
				<button onclick="searchJob()" class="button">Search Person by Job</button><br><br>
				<button onclick="searchCompany()" class="button">Search person by Company</button><br><br>
				<button onclick="searchCity()" class="button">Search Person by City</button><br><br>
				<button onclick="searchCompanyName()" class="button">Search Company by Name</button><br><br>
				<button onclick="searchCompanyDomain()" class="button">Search Company by Domain</button><br><br>
				<button onclick="searchCompanyCity()" class="button">Search Company by City</button><br><br>
				<button onclick="showAll()" class="button">Show All Persons</button><br><br>
				<button onclick="showCompanies()" class="button">Show All Companies</button><br><br>
				<button onclick="logOut()" class="button">Log Out</button>
				</div>

				<script>
				function showDashboard() {
					window.location = "http://" + window.location.hostname + ":3000/d/ZD_0XMLZz/dashboard";
				}

				function myLogs() {
					location.assign("logs");
				}
				
				function myInfo() {
					location.assign("my_data");
				}

				function searchName() {
					location.assign("search_name");
				}

				function searchJob() {
					location.assign("search_job");
				}

				function searchCompany() {
					location.assign("search_company");
				}

				function searchCity() {
					location.assign("search_city");
				}

				function searchCompanyName() {
					location.assign("search_company_name");
				}
				
				function searchCompanyDomain() {
					location.assign("search_company_domain");
				}
				
				function searchCompanyCity() {
					location.assign("search_company_city");
				}

				function showAll() {
					location.assign("all");
				}

				function showCompanies() {
					location.assign("all_companies");
				}

				function logOut() {
					location.assign("logout");
				}
				</script>

			</body>
			</html>
			'''
	return text