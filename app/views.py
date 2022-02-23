# JPxG, 2022 January 30

from app import app
from app import search

from app import parseParams
from app import makeQueries
from app import renderPage

from app import logProfile

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
	parsedParams = parseParams.parse(request.args)
	# Parse parameters using parseParams.py.
	results = makeQueries.query(parsedParams)
	# Use those parameters to make queries, using makeQueries.py.
	
	logProfile.log(results)
	# Store some basic profiling information (number of queries, timestamp, etc)

	renderOutput = renderPage.render(results)
	# Use the query output to render a page, using renderPage.py.
	# If the params say "HTML", it'll render a Jinja template.
	# Otherwise, it's just going to return whatever the user asked for.


	if results[0]["format"] == "HTML":
		return render_template("results.html", inp=renderOutput)
	else:
		return renderOutput