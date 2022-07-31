from flask import Flask,render_template,request,redirect,make_response,abort
import requests
import templates
from kentelauth import kauth 


app  =Flask(__name__)
auth = kauth("PathEngine")

class views:
	@app.route("/")
	def index():
		username = request.cookies.get("username")
		password = request.cookies.get("password")
		if username != None:
			theval = auth.login(username,password)
			if theval["SCC"] == True:
				return templates.home()
			else:
				pass


		return templates.index()

	@app.route("/login",methods=["POST","GET"])
	def login():
		if request.method == "POST":
			username = request.form.get("username")
			password = request.form.get("password")
			theval = auth.login(username,password)
			if theval["SCC"] == True:
				response = make_response(redirect("/"))
				response.set_cookie("username",username)
				response.set_cookie("password",password)
			else:
				response = make_response(templates.login_err())



			
			
			return response
		return templates.login()

	@app.route("/account")
	def account():
		msg = request.args.get("msg")
		if msg == None:
			msg=""

		username = request.cookies.get("username")
		
		return templates.profile(username,msg)

	@app.route("/logout")
	def logout ():
		response = make_response(redirect("/"))
		response.set_cookie("username","")
		return response

	@app.route("/register",methods=["POST","GET"])
	def register():
		if request.method == "POST":
			username = request.form.get("username")
			password = request.form.get("password")
			fullname = request.form.get("fullname")
			talents=request.form.get("bio")
			birthyear=request.form.get("birthyear")
			auth.createuser(username=username,password=password,fullname=fullname,talents=talents,birthyear=birthyear)
			return redirect("/login")
		return templates.register()

	@app.route("/change_password",methods=["POST","GET"])
	def change_password():
		username = request.cookies.get("username")
		if request.method == "POST":
			oldpassword=request.form.get("oldpassword")
			newpassword= request.form.get("newpassword")
			checkout = auth.login(username,oldpassword)
			if checkout["SCC"] == True:
				auth.changepassword(username=username,password=oldpassword,newpassword=newpassword)
				return redirect("/account?msg=Password Changed")
			else:
				return abort(403)
		if username == None:
			return abort(403)
		else:
			password=request.cookies.get("password")
			if password == None:
				return abort(403)

			else:
				output = auth.login(username,password)
				if output["SCC"] == True:
					return templates.change_password()
				else:
					return abort(403)


	@app.route("/create_project")
	def create_project():
		return templates.createProj()
app.run(debug=True)