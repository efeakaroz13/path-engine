def index():
	return """
		<html>
			<head>
				<title>Path Engine - Login</title>
			</head>
			<body>
			<div class="nav">
				<h3>Path Engine</h3>
			</div>
			<div style="margin-left:10px">
				<p>Make your 2 option games online for free!</p>
			</div>
			<center>

				<br>
				<h4 style="font-size:25px;" >Login or Register</h4>
				<button style="width:25%; font-size:20px;" onclick="window.location.assign('/login')">Login</button><br><br><button style="width:25%;font-size:20px;">Register</button>
			</center>
			</body>

		</html>

	"""

def login():
	return """
		<html>
			<head>
				<title>Path Engine - Login</title>
			</head>
			<body>
			<div class="nav">
				<h3>Path Engine - Login</h3>
				<center>
					<br><br>
					<form action="" method="POST" style="font-size:25px">
						<input type="text" name="username" placeholder="Username..."><br>
						<input type="password" name="password" placeholder="Password..."><br>
						<button type="submit">Log in</button>
					</form>
				</center>
			</div>
			
			</body>

		</html>

	"""