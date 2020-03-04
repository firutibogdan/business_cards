
def get_html(admin, persons):
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
      <br><br><button onclick="myFunction()" class="button1">Back</button><br><br>

      <table cellspacing=1 cellpadding=1 width="100%" border=1 bgcolor=lightgray>
        <tr align=center>
          <th><b>Name</b></th> 
          <th><b>Surname</b></th>
          <th><b>Phone</b></th>
          <th><b>Email</b></th>
          <th><b>Job</b></th>
          <th><b>Department</b></th>
          <th><b>Company</b></th>
          <th><b>City</b></th>
          <th><b>Country</b></th>'''

	if admin:
		text += '''
		  <th><b>Edit</b></th>
          <th><b>Delete</b></th>'''
	
	text += '''</tr>'''

	for person in persons:
		text += '''
				<tr align=center>
				'''
		for attr in person:
			text += '''
					<td>
					'''
			if admin:
				text += '''<br>'''
			text += str(attr)
			if admin:
				text += '''<br><br>'''
			text += '''
					</td>
					'''

		if admin:
			text += '''
				<td><br><button onclick="location.assign('edit_info?email={}');" class="button2"></button><br><br></td>
          		<td><br><button onclick="location.assign('delete_info?email={}');" class="button3"></button><br><br></td>
			'''.format(person[3], person[3])

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