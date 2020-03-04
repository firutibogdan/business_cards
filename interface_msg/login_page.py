
def get_html(message):
	text = '''
		<html>
		<head>
		<style>
		div {
			background-color: #e6e6e6;
			width: 40%;
			border: 15px solid #3399ff;
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
		<h2 style="font-family:courier;">BizyCards</h2>
		''' + \
		'''<p>{}</p>'''.format(message) + \
		'''
		<form action="" method="POST">
			<input class="username" id="name" name="username"
				placeholder="username" type="text" value=""
				style="font-family:courier;"
				required="required"><br>
			<input class="password" id="password" name="password"
				placeholder="password" type="password" value=""
				style="font-family:courier;"
				required="required"><br><br>
			<input class="button" id="submit" name="submit" type="submit"
				value="Sign In">
		</form>
		<button onclick="signUp()" class="button">Sign Up</button>
		</div>

		<script>
		function signUp() {
			location.assign("http://localhost/check_company_name");
		}
		</script>
		</body>
		</html>
		'''
	return text