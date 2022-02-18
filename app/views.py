# JPxG, 2022 January 30

from app import app
from app import search

from app import parseParams
from app import makeQueries
from app import renderPage

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
	# Simple thing that works. This doesn't invoke Jinja, though, so we won't use it.
	parsedParams = parseParams.parse(request.args)
	results = makeQueries.query(parsedParams)

	if results[0]["format"] == "HTML":
		return render_template("results.html", inp=renderPage.render(results))
	else:
		return renderPage.render(results)
	#return(render_template(search.doSearch(request.args)))
	# This doesn't work, even though it ought to.