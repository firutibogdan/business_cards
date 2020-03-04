
def get_html():
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
				top: 25%;
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
			<h2 style="font-family:courier;">Sign Up</h2>
			<h3 style="font-family:courier;">Company not found.</h3>
			<h3 style="font-family:courier;">Please add info for it!</h3><br>
			<form action="" method="POST">
				<input class="name" id="name" name="name"
					placeholder="Company name" type="text" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="phone" id="phone" name="phone"
					placeholder="Company phone" type="tel" value=""
					style="font-family:courier;"
					required="required"
					pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}" 
					onchange="this.setCustomValidity(this.validity.patternMismatch ? 'Format example: 0712-345-678' : ''); if(this.checkValidity()) form.password_two.pattern = this.value;"><br><br>
				<input class="email" id="email" name="email"
					placeholder="Company email" type="email" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="address" id="address" name="address"
					placeholder="Company address" type="text" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="domain" id="domain" name="domain"
					placeholder="Company domain" type="text" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="country" id="country" name="country"
					placeholder="Company country" type="text" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="city" id="city" name="city"
					placeholder="Company city" type="text" value=""
					style="font-family:courier;"
					required="required"><br><br>
				<input class="latitude" id="latitude" name="latitude"
					placeholder="Company latitude" type="text" value=""
					style="font-family:courier;"
					pattern="-?[0-9][0-9]?[0-9]?[.][0-9]{6}"
					title="-?[0-9][0-9]?[0-9]?.[0-9]{6}"
					required="required"><br><br>
				<input class="longitude" id="longitude" name="longitude"
					placeholder="Company longitude" type="text" value=""
					style="font-family:courier;"
					pattern="-?[0-9][0-9]?[0-9]?[.][0-9]{6}"
					title="-?[0-9][0-9]?[0-9]?.[0-9]{6}"
					required="required"><br><br><br>
				<input class="button" id="submit" name="submit" type="submit"
					value="Next">
			</form>
			<button onclick="goBack()" class="button">Cancel</button>
			</div>

			<script>
			function goBack() {
				location.assign("login");
			}
			</script>
		</body>
		</html>
		'''
	return text