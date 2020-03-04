
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
				<h2 style="font-family:courier;">Success</h2>
				<button onclick="goBack()" class="button">Ok</button><br><br>
				</div>

				<script>
				function goBack() {
					location.assign("home");
				}
				</script>
			</body>
			</html>
		'''
	return text