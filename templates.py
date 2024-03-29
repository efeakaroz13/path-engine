def index():
	return """
		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
			</nav>


			<div class="container">
			<center><br><br>
				<p>Welcome to <code>Path Engine</code> by Kentel</p><br>
				<br>
				<a href="/login">Login</a> or <a href="/register">Register</a>
					
				
				
				
			</center>
			</div>
			
			</body>

		</html>

	"""

def login():
	return """
		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
			</nav>


			<div class="container">
			<center><br><br>
				<div class="card" style="width:70%;">
					<div class="card-body">
						<h5 class="card-title">Log In</h5>
						<form action="/login" method="POST">
							<input type="text" autocomplete="off" name="username" placeholder="Username..." class="form-control" required><br>
							<input type="password" autocomplete="off" name="password" placeholder="Password..." class="form-control" required><br>
							<button class="btn btn-dark" type="submit">Log In</button>
						</form>
					</div>
				</div>
				
				
				
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
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
			</nav>


			<div class="container">
			<center><br><br>
				<div class="card" style="width:70%;">
					<div class="card-body">
						<h5 class="card-title">Log In</h5>
						<form action="/login" method="POST">
							<input type="text" autocomplete="off" name="username" placeholder="Username..." class="form-control" style="border:1px solid red;"required><br>
							<input type="password" autocomplete="off" name="password" placeholder="Password..." class="form-control" style="border:1px solid red;"required><br>
							<button class="btn btn-dark" type="submit">Log In</button>
						</form>
					</div>
				</div>
				
				
				
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
				<link rel="stylesheet" href="/static/main.css">
			</head>
			<body>
			
			<nav class="navbar navbar-light" style="background:#c4c4c4">
			  <a class="navbar-brand" href="/" style="font-family: 'Koulen', cursive;font-family: 'Merriweather', serif;">
			    <img src="/static/fav.png" width="30" height="30" class="d-inline-block align-top" alt="" style="margin-left:10px;margin-right:10px;">
			    Path Engine
			  </a>
			  <a href="/account" style="margin-right:20px;border:1px solid #fff;padding:10px;border-radius:50%;"><i class="fa fa-user" style="color:white"></i></a>
			</nav>
			<nav  class="d-lg-block sidebar  bg-white" style="width:%20;position:fixed;left:0px;border-right:1px solid #000;height100%;height:1700px;">
              <div class="position-sticky">
                <div class="list-group list-group-flush mx-3 mt-4">
                  <a href="/" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                    <i  style=""class="fas fa-tachometer-alt fa-fw me-3"></i><span></span>
                  </a>
                  <a href="/compile/android" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-android fa-fw  me-3" style="color:green"></i><span></span>
                  </a>
                  <a href="/compile/windows" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-windows fa-fw  me-3" style="color:#0087f5"></i><span></span>
                  </a>
                  <a href="/compile/website" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-js fa-fw  me-3" style="color:#c9aa0a"></i><span></span>
                  </a>
                  <a href="/compile/ios" class="list-group-item list-group-item-action py-2 ripple" >
                    <i class="fa-brands fa-app-store-ios fa-fw  me-3" style="color:#1a83f4"></i><span></span>
                  </a>
                  
                </div>
              </div>
            </nav>

			<div class="container" >

				<div class="grid-container">
					<div class="card" onclick="window.location.assign('/create_project')">
						<div class="card-body">
							<h5>Create project <img width="30" src="/static/fav.png"></h5>
							<p class="card-text">
								New path engine project.
							</p>
						</div>
					</div>
				</div>

			</div>
			
			</body>

		</html>

	"""


def profile(username,msg):
	if msg == "":

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
							<h5 class="card-title">"""+username+""" (you)<br> </h5>

						</div>

					</div><br>
					<div class="card" style="width:70%;padding-bottom:0px;">


						<div class="card-body">
							<h5 class="card-title">Settings</h5>

						

							<ul class="list-group" style="text-align:left;margin-bottom:0px">
								<li onclick="window.location.assign('/change_password')" class="list-group-item">Change Password</li>
								<li onclick="window.location.assign('/logout')" class="list-group-item">Logout</li>
							</ul>

						</div>
					</div>
					
				</center>
				</div>
				
				</body>

			</html>
		"""

	else:
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

				<div class="alert alert-primary" style="position:fixed;right:10px;bottom:10px" id="alert"><a href="/account" style="margin-right:10px">x</a>"""+msg+"""</div>
				<div class="container">
				<center><br><br>
					<div class="card" style="width:70%;">


						<div class="card-body">
							<h5 class="card-title">"""+username+""" (you)<br> </h5>

						</div>

					</div><br>
					<div class="card" style="width:70%;padding-bottom:0px;">


						<div class="card-body">
							<h5 class="card-title">Settings</h5>

						

							<ul class="list-group" style="text-align:left;margin-bottom:0px">
								<li onclick="window.location.assign('/change_password')" class="list-group-item">Change Password</li>
								<li onclick="window.location.assign('/logout')" class="list-group-item">Logout</li>
							</ul>

						</div>
					</div>
					
				</center>
				</div>
				
				</body>

			</html>
		"""
def register():
	return """

		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
			 </nav>


			<div class="container">
			<center><br><br>
				<div class="card" style="width:70%;">


					<div class="card-body">
							<h5 class="card-title">Register to PathEngine</h5>
							<p class="card-text">
								<form action="" method="POST">
									<input type="text" autocomplete="off" placeholder="Username..." name="username" class="form-control" required><br>
									<input type="text" autocomplete="off" placeholder="Full Name..." name="fullname" class="form-control" required><br>
									<input type="text" autocomplete="off" placeholder="Birth Year..." name="birthyear" class="form-control" required><br>
									<textarea placeholder="Bio..." class="form-control" name="bio" required></textarea><br>
									<input type="password" autocomplete="off" placeholder="Password..." name="password" class="form-control" required><br>
									<button class="btn btn-dark">Register</button>
									
									
									

								</form>
							</p>
					</div>

				</div><br>
				
			</center>
			</div>
			
			</body>

		</html>

	"""




def change_password():
	return """

		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
				<script src="/static/change-password.js"></script>
			</head>
			<body>
			
			<nav class="navbar navbar-light " style="background:#c4c4c4">
			  <a class="navbar-brand" href="/" style="font-family: 'Koulen', cursive;font-family: 'Merriweather', serif;">
			    <img src="/static/fav.png" width="30" height="30" class="d-inline-block align-top" alt="" style="margin-left:10px;margin-right:10px;">
			    Path Engine
			  </a>
			 </nav>


			<div class="container">
			<center><br><br>
				<div class="card" style="width:70%;">


					<div class="card-body">
							<h5 class="card-title">Change Password</h5>
							<form action="" method="POST">
								<input type="password" placeholder="Old Password" name="oldpassword" class="form-control"><br>
								<input type="password" placeholder="New Password" name="newpassword" class="form-control"><br>

							</form>
							<button onclick="change_password()" class="btn btn-primary" style="margin-right:10px">Change</button><button class="btn btn-danger" onclick="cancel()">Cancel</button>
					</div>

				</div><br>
				
			</center>
			</div>
			
			</body>

		</html>

	"""







def createProj():
	return """

		<html>
			<head>
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<title>Path Engine</title>
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
				<script src="/static/projectcreate.js"></script>
			</head>
			<body>
			
			<nav class="navbar navbar-light " style="background:#c4c4c4">
			  <a class="navbar-brand" href="/" style="font-family: 'Koulen', cursive;font-family: 'Merriweather', serif;">
			    <img src="/static/fav.png" width="30" height="30" class="d-inline-block align-top" alt="" style="margin-left:10px;margin-right:10px;">
			    Path Engine
			  </a>
			 </nav>


			<div class="container">
			<center><br><br>

				<div class="card" style="width:70%;">


					<div class="card-body">
							<h5 class="card-title">Create A Path Engine Project</h5>
							<form action="" method="POST" id="formcreate">
								
							</form>
							<button onclick="createProject()" class="btn btn-primary" style="margin-right:10px">Create</button><button class="btn btn-danger" onclick="cancel()">Cancel</button>
					</div>

				</div><br>
				
			</center>
			</div>
			<center><div style='position:absolute;top:100px;right:20px;left:20px;height:500px;display:none;padding-top:200px;' id="cancelpopup" class='card'><div class='card-body'><h5 class='card-title'>Do you want to cancel?</h5><p class='card-text'><button class="btn btn-danger" onclick="yescancel()">Yes</button><button style="margin-left:10px"  onclick="cancel()"class="btn btn-dark">No</button></p></div></div></center>
			</body>

		</html>

	"""


