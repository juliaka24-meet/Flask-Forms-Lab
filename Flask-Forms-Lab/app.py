from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

login_data = {"username":["ju","itai","daniel"],"password":["123","456","789"]}
facebook_friends=["Itai","Romie","Aidan", "Maria", "Ghassan", "Atef"]


@app.route('/', methods=["GET","POST"])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		username=request.form["username"]
		password=request.form["password"]
		for username_data in login_data["username"]:
			if username == username_data and password == login_data["password"][login_data["username"].index(username_data)]:
				print("i")
				return redirect(url_for('home'))
		else:
			return render_template('login.html')
  
@app.route('/home', methods=["GET","POST"])
def home():
	return render_template("home.html", friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend(name):
	return render_template('friend_exists.html', name=name, friends=facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True,
	)