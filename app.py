from flask import Flask,render_template,request,redirect,make_response
import requests
import templates

app  =Flask(__name__)

class views:
	@app.route("/")
	def index():
		return templates.index()

	@app.route("/login",methods=["POST","GET"])
	def login():
		if request.method == "POST":
			username = request.form.get("username")
			password = request.form.get("password")
			
			response = make_response(redirect("/"))
			return response
		return templates.login()
app.run(debug=True)