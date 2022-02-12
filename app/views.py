# JPxG, 2022 January 30

from app import app

@app.route("/")
def index():
	return("meow meow meow")

@app.route("/about")
def about():
	return("woof woof woof")