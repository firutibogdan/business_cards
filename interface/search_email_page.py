
def get_html(name, surname, phone, email, password, birthday, company_name, department, job, country, city):
	text = '''
			<html>
		<head>
			<style>
			div {
				background-color: #e6e6e6;
				width: 70%;
				border: 15px solid #006600;
				padding: 50px;
				position: absolute;
				top: 10%;
				left: 10%;
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
			<h2>Update personal data</h2>
			<form action="" method="POST">
				<input class="name" id="name" name="name"
					placeholder="Last name" type="text" value="'''
	text += name + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="surname" id="surname" name="surname"
					placeholder="First name" type="text" value="'''
	text += surname + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="phone" id="phone" name="phone"
					placeholder="Phone" type="tel" value="'''
	text += phone + '''"
					style="font-family:courier;"
					required="required"
					size="18"
					pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}" 
					onchange="this.setCustomValidity(this.validity.patternMismatch ? 'Format example: 0712-345-678' : ''); if(this.checkValidity()) form.password_two.pattern = this.value;"><br><br>
				<input class="email" id="email" name="email"
					placeholder="Email" type="email" value="'''
	text += email + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="birthday" id="birthday" name="birthday"
					placeholder="Birthday" type="date" value="'''
	text += birthday + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="company_name" id="company_name" name="company_name"
					placeholder="Company name" type="text" value="'''
	text += company_name + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="department" id="department" name="department"
					placeholder="Department" type="text" value="'''
	text += department + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="job" id="job" name="job"
					placeholder="Job Title" type="text" value="'''
	text += job + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="country" id="country" name="country"
					placeholder="Country" type="text" value="'''
	text += country +'''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input class="city" id="city" name="city"
					placeholder="City" type="text" value="'''
	text += city + '''"
					style="font-family:courier;"
					required="required"
					size="18"><br><br>
				<input id="password" name="password" type="password" value="******"
					style="font-family:courier;"
					size="18"
					pattern="^\S{6,}$"
					onchange="this.setCustomValidity(this.validity.patternMismatch ? 'Must have at least 6 characters' : ''); if(this.checkValidity()) form.password_two.pattern = this.value;"
					placeholder="Password" required><br><br>
				<small>Let "******" (6 stars) if you do not want to change password!</small><br><br>
				<input class="button" id="submit" name="submit" type="submit"
					value="Update"><br><br>
				</form>
				<button onclick="goBack()" class="button">Back</button><br><br><br>
				<button onclick="deleteThis()" class="button">Delete Account</button><br><br>

				</div>
			<script>
				function goBack() {
					location.assign("home");
				}

				function deleteThis() {
					location.assign("delete_info?email='''
	text += email
	text += 	'''");
				}
			</script>
			</body>
		</html>
        '''

	return text