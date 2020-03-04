
def get_html(user):
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
				<h2>Welcome, ''' + user + '''!</h2>
				<h3>Who would you like to chat with?</h3>
				<form action="" method="POST">
					<input class="username" id="name" name="username"
						placeholder="username" type="text" value=""
						style="font-family:courier;"
						required="required"><br><br>
					<input class="button" id="submit" name="submit" type="submit"
						value="Chat">
				</form>
				<button onclick="logOut()" class="button">Log Out</button>
				</div>

				<script>
				function logOut() {
					location.assign("logout");
				}
				</script>

			</body>
			</html>
			'''

	return text