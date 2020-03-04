def get_html(user, friend, messages):
	text = '''
			<html>
            <head>
                <style>
                textarea {
                    resize: none;
                }

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
                <textarea id="messages" name="messages" rows="20" cols="50" readonly>''' + messages + \
                '''</textarea><br><br>
                <form action="" method="POST">
                    <input class="message" id="message" name="message"
                        placeholder="Message" type="text" value=""
                        style="font-family:courier;"
                        required="required" size="40"><br><br>
                    <input class="button" id="submit" name="submit" type="submit"
                        value="Send">
                </form>
                <button onclick="goBack()" class="button">Go Back</button>
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