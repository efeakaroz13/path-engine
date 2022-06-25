from flask import Flask,render_template,request,redirect,make_response
import requests
import templates
from auth import auth

app  =Flask(__name__)

class views:
	@app.route("/")
	def index():
		username = request.cookies.get("username")
		password = request.cookies.get("password")
		if username != None:
			theval = auth.sign_in(username,password)
			if theval["login"] == True:
				return templates.home()
			else:
				pass


		return templates.index()

	@app.route("/login",methods=["POST","GET"])
	def login():
		if request.method == "POST":
			username = request.form.get("username")
			password = request.form.get("password")
			theval = auth.sign_in(username,password)
			if theval["login"] == True:
				response = make_response(redirect("/"))
				response.set_cookie("username",username)
				response.set_cookie("password",password)
			else:
				response = make_response(templates.login_err())



			
			
			return response
		return templates.login()

	@app.route("/account")
	def account():
		username = request.cookies.get("username")
		
		return templates.profile(username)
app.run(debug=True)