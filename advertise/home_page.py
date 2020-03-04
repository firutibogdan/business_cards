def get_html(companies):
	text = '''<html>
				<head>
					<style>
						iframe {
							width: 50%;
							height: 100px;
						}
					</style>
				</head>
				<body>

				<div style="background-image: url('ads.jpg');">

				<iframe src="https://virginradio.ro/live/" name="myFrame"></iframe>
				<a class="weatherwidget-io" href="https://forecast7.com/ro/44d4326d10/bucharest/" data-label_1="BUCHAREST" data-theme="original" style="width:100%;"
				>BUCHAREST</a>
				<script>
				!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
				</script>



				<p></p>
				<a href="/ad?company=''' + companies[0] + '''" target="_blank">
				<img src="a.jpg" alt="Trulli" width="470" height="300">
				</a>
				<a href="/ad?company=''' + companies[1] + '''" target="_blank">
				<img src="b.png" alt="Trulli" width="470" height="300">
				</a>
				<a href="/ad?company=''' + companies[2] + '''" target="_blank">
				<img src="c.jpg" alt="Trulli" width="470" height="300">
				</a>
				<p></p>
				<a href="/ad?company=''' + companies[3] + '''" target="_blank">
				<img src="d.jpg" alt="Trulli" width="470" height="300">
				</a>
				<a href="/ad?company=''' + companies[4] + '''" target="_blank">
				<img src="e.jpg" alt="Trulli" width="470" height="300">
				</a>
				<a href="/ad?company=''' + companies[5] + '''" target="_blank">
				<img src="f.jpg" alt="Trulli" width="470" height="300">
				</a>
				</div>

				</body>
				</html>
			'''

	return text