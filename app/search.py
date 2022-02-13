docstring = """
 JPxG, 2022 February 12
 This is the main file that handles the user's query.
 Here is what it does:
1) Parses the request (which namespaces, pages, etc to query)
2) Queries the en.wp API to get the user's contributions.
3) Composes a results page containing these results.

It doesn't just directly do all these things itself.
Instead, it imports other programs to do them.
Otherwise, it would be unimaginably long and hard to work with.
"""

from app import parseParams
from app import makeQueries
from app import renderPage

def doSearch(params):
	#return "baba booey! params were \"" + params + "\""
	parsedParams = parseParams.parse(params)
	results = makeQueries.query(parsedParams)
	renderedPage = renderPage.render(results)
	return renderedPage

if __name__ == "__main__":
	print(docstring)
