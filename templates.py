def index():
	return """
		<html>
			<head>
				<title>Path Engine - Login</title>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<link rel="shortcut icon" href="/static/fav.png">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
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
				<link rel="shortcut icon" href="/static/fav.png">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
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


def login_err():
	return """
		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

				<title>Path Engine - Login</title>
				<link rel="shortcut icon" href="/static/fav.png">
			</head>
			<body>
			<div class="nav">
				<h3>Path Engine - Login</h3>
				<center>
					<br><br>
					<form action="" method="POST" style="font-size:25px">
						<input type="text" name="username" placeholder="Username..."><br>
						<input type="password" name="password" placeholder="Password..."><br>
						<button type="submit">Log in</button><br>
						<p style="color:red">Email or password is not correct!</p>
					</form>
				</center>
			</div>
			
			</body>

		</html>

	"""

def home():
	return """
		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine - Home</title>
				<link rel="shortcut icon" href="/static/fav.png">
				<link rel="preconnect" href="https://fonts.googleapis.com">
				<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
				<link href="https://fonts.googleapis.com/css2?family=Koulen&family=Merriweather:wght@300&display=swap" rel="stylesheet">
				
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css" integrity="sha512-q3eWabyZPc1XTCmF+8/LuE1ozpg5xxn7iO89yfSOd5/oKvyqLngoNGsx8jq92Y8eXJ/IRxQbEC+FGSYxtk2oiw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/js/all.min.js" integrity="sha512-LW9+kKj/cBGHqnI4ok24dUWNR/e8sUD8RLzak1mNw5Ja2JYCmTXJTF5VpgFSw+VoBfpMvPScCo2DnKTIUjrzYw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/solid.min.css" integrity="sha512-LopA1sokwAW/FNZdP+/5q8MGyb9CojL1LTz8JMyu/8YZ8XaCDn1EOm6L7RWIIOHRM7K4jwnHuOmyLZeeeYxSOA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/v4-shims.min.css" integrity="sha512-fSDKn6bxKjJWWaTbtlYfFf+1sRuP/CC+T+jhy26N/s2FcBI89kn6aShnsDmECKd2I1nRlXOButa2A2wzQ8mNEw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<!-- Google Fonts -->
				<link
				  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
				  rel="stylesheet"
				/>
				<!-- MDB -->
				<link
				  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
				  rel="stylesheet"
				/>
			</head>
			<body>
			
			<nav class="navbar navbar-light " style="background:#c4c4c4">
			  <a class="navbar-brand" href="/" style="font-family: 'Koulen', cursive;font-family: 'Merriweather', serif;">
			    <img src="/static/fav.png" width="30" height="30" class="d-inline-block align-top" alt="" style="margin-left:10px;margin-right:10px;">
			    Path Engine
			  </a>
			  <a href="/account" style="margin-right:20px;border:1px solid #fff;padding:10px;border-radius:50%;"><i class="fa fa-user" style="color:white"></i></a>
			</nav>
			<nav  class=" d-lg-block sidebar  bg-white" style="width:%20;position:fixed;left:0px;border-right:1px solid #000;height100%;">
              <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                  <a href="/" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                    <i  style=""class="fas fa-tachometer-alt fa-fw me-3"></i><span>Dashboard</span>
                  </a>
                  <a href="/compile/android" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-android fa-fw  me-3" style="color:green"></i><span>Android Compiler</span>
                  </a>
                  <a href="/compile/windows" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-windows fa-fw  me-3" style="color:#0087f5"></i><span>Windows Compiler</span>
                  </a>
                  <a href="/compile/website" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-js fa-fw  me-3" style="color:#c9aa0a"></i><span>Website Compiler</span>
                  </a>
                  <a href="/compile/ios" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-app-store-ios fa-fw  me-3" style="color:#1a83f4"></i><span>iOS Compiler</span>
                  </a>
                  
                </div>
              </div>
            </nav>

			<div class="container">
			</div>
			
			</body>

		</html>

	"""


def profile(username):
	return """
		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>("""+username+""")Path Engine</title>
				<link rel="shortcut icon" href="/static/fav.png">
				<link rel="preconnect" href="https://fonts.googleapis.com">
				<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
				<link href="https://fonts.googleapis.com/css2?family=Koulen&family=Merriweather:wght@300&display=swap" rel="stylesheet">
				
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css" integrity="sha512-q3eWabyZPc1XTCmF+8/LuE1ozpg5xxn7iO89yfSOd5/oKvyqLngoNGsx8jq92Y8eXJ/IRxQbEC+FGSYxtk2oiw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/js/all.min.js" integrity="sha512-LW9+kKj/cBGHqnI4ok24dUWNR/e8sUD8RLzak1mNw5Ja2JYCmTXJTF5VpgFSw+VoBfpMvPScCo2DnKTIUjrzYw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/solid.min.css" integrity="sha512-LopA1sokwAW/FNZdP+/5q8MGyb9CojL1LTz8JMyu/8YZ8XaCDn1EOm6L7RWIIOHRM7K4jwnHuOmyLZeeeYxSOA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/v4-shims.min.css" integrity="sha512-fSDKn6bxKjJWWaTbtlYfFf+1sRuP/CC+T+jhy26N/s2FcBI89kn6aShnsDmECKd2I1nRlXOButa2A2wzQ8mNEw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
				<!-- Google Fonts -->
				<link
				  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
				  rel="stylesheet"
				/>
				<!-- MDB -->
				<link
				  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
				  rel="stylesheet"
				/>
			</head>
			<body>
			
			<nav class="navbar navbar-light " style="background:#c4c4c4">
			  <a class="navbar-brand" href="/" style="font-family: 'Koulen', cursive;font-family: 'Merriweather', serif;">
			    <img src="/static/fav.png" width="30" height="30" class="d-inline-block align-top" alt="" style="margin-left:10px;margin-right:10px;">
			    Path Engine
			  </a>
			  <a href="/account" style="margin-right:20px;border:1px solid #fff;padding:10px;border-radius:50%;background:#fff"><i class="fa fa-user" style="color:black"></i></a>
			</nav>


			<div class="container">
			<center><br><br>
				<div class="card" style="width:70%;">


					<div class="card-body">
						<h5 class="card-title">"""+username+""" (you)</h5>

					</div>

				</div><br>
				<div class="card" style="width:70%;">


					<div class="card-body">
						<h5 class="card-title">Complete your profile</h5>

					</div>
					<p class="card-text">
					<form action="" method="POST">
						<input type="email" name="email" placeholder="Enter email..." class="form-control" style="width:60%;"><br>
						<input type="text" name="fullname" placeholder="Your Full Name?" class="form-control" style="width:60%;"><br>
						<input type="file" name="ppicture" placeholder="Profile Picture" class="form-control" style="width:60%;"><br>
						<button type="submit" class="btn btn-primary"> Enter your profile</button>
						
					</form>
					</p>
				</div>
				
			</center>
			</div>
			
			</body>

		</html>
	"""

