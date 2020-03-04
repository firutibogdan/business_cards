
def get_html(persons):
	text = '''
			<html>
    <head>
      <style>
        div {
          background-color: #e6e6e6;
          width: 80%;
          border: 15px solid #006600;
          padding: 50px;
          position: absolute;
          top: 10%;
          left: 5%;
        }

        .button1 {
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

        .button1:hover {background-color: #80bdff}

        .button1:active {
          background-color: #4da3ff;
          box-shadow: 0 5px #666;
          transform: translateY(4px);
        }

        .button2 {
          display: inline-block;
          padding: 6px 10px;
          font-size: 12px;
          cursor: pointer;
          text-align: center;
          text-decoration: none;
          outline: none;
          color: #663300;
          background-color: #33cc33;
          border: none;
          border-radius: 15px;
          box-shadow: 0 9px #999;
          font-family:courier;
        }

        .button2:hover {background-color: #29a329}

        .button2:active {
          background-color: #1f7a1f;
          box-shadow: 0 5px #666;
          transform: translateY(4px);
        }

        .button3 {
          display: inline-block;
          padding: 6px 10px;
          font-size: 12px;
          cursor: pointer;
          text-align: center;
          text-decoration: none;
          outline: none;
          color: #663300;
          background-color: #ff3333;
          border: none;
          border-radius: 15px;
          box-shadow: 0 9px #999;
          font-family:courier;
        }

        .button3:hover {background-color: #cc0000}

        .button3:active {
          background-color: #800000;
          box-shadow: 0 5px #666;
          transform: translateY(4px);
        }
      </style>
    </head>
    <body>

      <div>
	  <h2 align="center">Logs</h2>
        <button onclick="myFunction()" class="button1">Back</button><br><br>

        <table cellspacing=1 cellpadding=1 width="100%" border=1 bgcolor=lightgray>
          <tr align=center>
            <th><b>Name</b></th> 
            <th><b>Surname</b></th>
            <th><b>Email</b></th>
            <th><b>Activity</b></th>
            <th><b>Timestamp</b></th>
            </tr>'''

	for person in persons:
		text += '''
				<tr align=center>
				'''
		for attr in person:
			text += '''
					<td>
					'''
			text += str(attr)
			text += '''
					</td>
					'''
		text += '''
				</tr>
				'''
	text += '''
			</table>
			</div>
			<script>
			function myFunction() {
				location.assign("home");
			}
			</script>
			</body>
			</html>
			'''

	return text