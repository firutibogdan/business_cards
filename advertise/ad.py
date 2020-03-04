def get_html(info):
	text = '''
			<html>
			<head>
				<style>
				textarea {
				resize: none;
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

				div {
				display: inline-block;
				width: 500px;
				}
			</style>
			</head>
			<body style="background-image: url('business.jpg');">

			<div align="center">
			<h1 style="font-family:courier;">Company Data</h2><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[0] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[1] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[2] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[3] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[4] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[5] + '''</textarea><br><br><br>
			<textarea id="123" rows="1" cols="40" readonly>''' + info[6] + '''</textarea><br><br><br>
			<button onclick="goBack()" class="button">Back</button><br><br>
			</div>

			<div id="googleMap" style="width:60%;height:520px;"></div>

			<script>
			function myMap() {
			var mapProp= {
			center:new google.maps.LatLng(''' + str(info[7]) + ''', ''' + str(info[8]) + '''),
			zoom:15,
			};
			var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
			}
			</script>

			<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCY5hkNRAR9mc7uMs8TLi3-3WeGBI1w4LM&callback=myMap"></script>

			<script>
			function goBack() {
				location.assign("home");
			}
			</script>

			</body>
			</html>
			'''
			
	return text