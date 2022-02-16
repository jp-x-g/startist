# JPxG, 2022 January 30

from app import app
from app import search

from flask import render_template
from flask import request

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api")
def about():
	return(search.doSearch(request.args))

@app.route("/results")
def showResults():
	#return (search.doSearch(request.args))
	# Simple thing that works.

	return render_template("results.html", content=search.doSearch(request.args))
	#return(render_template(search.doSearch(request.args)))
	# This doesn't work, even though it ought to.