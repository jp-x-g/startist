docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""
import requests
from datetime import date
from datetime import datetime
from datetime import timedelta
# For validating timestamps.

def queryNamespace(ob, item, include=False):

	ob["debug"] = "queryNamespace has been called"

	ob["namespaces"][item[0]] = {}
	ob["namespaces"][item[0]]["include"] = include
	ob["namespaces"][item[0]]["count"] = 0
	ob["namespaces"][item[0]]["edits"] = {}
	# Initialize object for this namespace.

	# Now we're going to actually hit the API and get all edits from this namespace.

	continueQuerying = 1
	if ((ob["startdate"].find("INVALID") != -1) or (ob["enddate"].find("INVALID") != -1)):
		ob["debug"] = "Invalid date detected"
		return ob

		#return "Invalid date stamps. Start date: " + ob["startdate"].replace("INVALID:", "") + " End date: " + ob["enddate"].replace("INVALID:", "")
	if (ob["startdate"] != ""):
		# If the oldest date is valid.
		oldest = ob["startdate"]
	else:
		oldest = "20000101000000"

	if (ob["enddate"] != ""):
		newest = ob["enddate"]
	else:
		newest = "20991231235959"

	# If the timestamps supplied by the user are valid, use them.
	# Otherwise, set the range to be the whole damn 21st century.
	# If people are still using this software in the 22nd century, well, sucks to be them.

	continueTimestamp = newest + "|10000000000"
	# Time to start the loop where we get all contribs.

	ob["debug"] = "about to open session"
	

	sess = requests.Session()
	apiUrl = "https://en.wikipedia.org/w/api.php"
	# Open session.
	ob["debug"] = "Opened session for API queries"
	print("Beginning queries.")
	while (continueQuerying == 1):
		queryParams = {
		"action": "query",
		"format": "json",
		"list": "usercontribs",
		"ucuser": ob["username"],
		"uclimit": 500,
		"ucnamespace": item[0],
		"uccontinue": continueTimestamp
		}
		# The next line is for debug only.
		#print("Querying")
		ob["debug"] = "Current query: " + str(queryParams)
		#print(f"Querying with {apiUrl}")
		print(queryParams)
		response = sess.get(url=apiUrl, params=queryParams, timeout=5)
		#print("Querying")
		r = response.json()
		#print("Querying")
		ob["totalQueries"] += 1
		#ob["response"] = r
		ob["debug"] = ob["debug"] + " . Query now received"

		if "continue" in r:
			continueTimestamp = r["continue"]["uccontinue"]
			continueQuerying = 1
		else:
			# Set this to 0 to make the current iteration the last one.
			continueQuerying = 0
			ob["debug"] = "Query response had no 'continue', processing last batch of results"
		for result in r["query"]["usercontribs"]:
			# 2022-02-13T01:46:08Z
			# print("New result")
			ob["totalResults"] += 1
			ts = result["timestamp"].replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
			if int(ts) > int(oldest):
				# If it's within the selected date range.
				try:
					if (result["comment"].find(ob["hotstring"]) != -1):
						ob["totalHits"] += 1
						ob["namespaces"][item[0]]["count"] += 1
						ob["namespaces"][item[0]]["edits"][result["revid"]] = result
				except:
					ob["exceptions"] += 1
					# I am not sure how this could possibly generate a KeyError for "comment", but it did when processing a large request.
					# Handling the exception seemed to work fine.
			else:
				# If the timestamp of the rev being processed is older than the "oldest" cutoff:
				# Set this to 0 to make the current iteration the last one.
				continueQuerying = 0
	
	ob["debug"] = "queryNamespace completed, returning parsed results"

	return ob
	# This returns ob to query, but also sometimes to queryPage.


def queryPage(ob, item, prefix="", category="misc"):

	# "Item" should look like:
	# [4, "Administrators'_noticeboard", "AN"]
	#ob['debug'] = ob['debug'] + "ns: " + str(item[0]) + " keys: " + str(ob["namespaces"].keys())
	ob["debug"] = "queryPage is running"
	if (item[0] in ob["namespaces"].keys()):
		pass
		# I had to debug this for about an hour and a half. Stick a fork in me...
	else:
		ob = queryNamespace(ob, item)
	if (category in ob) == False:
		ob[category] = {}

	prefixedName = prefix + item[1]
	# prefixedName = "Wikipedia:" + "Administrators'_noticeboard"

	ob[category][prefixedName] = {
		"count": 0,
		"name": [item[1], item[2]],
		"edits": {}
		}
	# Something like this:
	# ob["noticeboards"]["Wikipedia:Administrators'_noticeboard"]

	# The object has been initialized now, and queryNamespace has been run
	# (whether invoked by the page selection or by the namespace being itself selected)

	# Now we're going to go through the results and find just the ones from that page

	for key in ob["namespaces"][item[0]]["edits"]:
		value = ob["namespaces"][item[0]]["edits"][key]
		if (str(value["title"]).replace("_", " ") == str(prefixedName).replace("_", " ")):
			revisionId = value["revid"]
			ob[category][prefixedName]["edits"][revisionId] = value
			# Store the diff in the object.
			ob[category][prefixedName]["count"] += 1
			# Increment the count by one.

	return ob
	# This returns ob to, most likely, query.

def query(params):
	"""Main entry point for views.py: uses parseParams.py output to query en.wp API on namespaces, and filter by individual pages."""
	hotString = "*/ new section"

	output = {
	"username": params["username"],
	"startdate": params["startdate"], 
	"enddate":  params["enddate"], 
	"format": params["format"],
	"hotstring": hotString,
	"debug": "makeQueries initializing",
	"totalQueries": 0,
	"totalResults": 0,
	"totalHits": 0,
	"exceptions": 0,
	"namespaces": {
		}
	}

	# This is a special case, because the entire namespace is being searched, not just one page.
	for item in params["namespaces"]:
		output = queryNamespace(output, item, include=True)
		pass

	#return params, output

	# Everything in these categories is in namespace 4 (Wikipedia).
	for cat in ["noticeboards", "refdesks", "villagepumps"]:
		for item in params[cat]:
			output = queryPage(output, item, prefix="Wikipedia:", category=cat)
			pass
	for item in params["misc"]:
		output = queryPage(output, item, prefix="Wikipedia:", category="misc")
		pass



	# All queries have been executed, and all data is stored.

	# Now we will remove the results from every namespace that wasn't actually specified.
	# That is, if you are just searching for edits on one page, you don't care about others in the same namespace, even if we had to query it to find those edits.
	# 

	for item in output["namespaces"]:
		if output["namespaces"][item]["include"] == False:
			#del output["namespaces"][item]
			output["namespaces"][item]["edits"] = {}


	# Now for the last step -- seeing how long this whole business took to run.
	timeNow = datetime.now()
	timeThen = datetime.strptime(params["runstamp"], "%Y%m%d%H%M%S%f")
	elapsed = timeNow - timeThen
	params["finished"] = timeNow.strftime("%Y%m%d%H%M%S%f")
	params["elapsed"] = elapsed.total_seconds() 

	return [params, output]
	# This is the final output of the script, which is probably being returned to views.py.

if __name__ == "__main__":
	print(docstring)
