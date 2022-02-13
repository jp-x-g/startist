# JPxG, 2022 January 30

from app import app
from app import search

from flask import render_template
from flask import request

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return("woof woof woof")

@app.route("/results")
def showResults():
	return(search.doSearch(request.args))