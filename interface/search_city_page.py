
def get_html(table, persons):
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

			<div>
			<h2 align="center">Search by city</h2>
				<button onclick="goBack()" class="button">Back</button><br><br>
				<form action="" method="POST">
					<input class="city" id="city" name="city"
						placeholder="Insert city name" type="text" value=""
						style="font-family:courier;"
						required="required">
					<input class="button" id="submit" name="submit" type="submit"
						value="Search">
				</form>
			'''

    if table:
        text += '''
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
					<th><b>Country</b></th>
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
				'''

    text +=	'''
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