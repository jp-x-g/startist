docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""
import requests

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
	ob["debug"] = "opened session"

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
		ob["query"] = queryParams

		response = sess.get(url=apiUrl, params=queryParams)
		r = response.json()
		#ob["response"] = r

		if "continue" in r:
			continueTimestamp = r["continue"]["uccontinue"]
			continueQuerying = 1
		else:
			# Set this to 0 to make the current iteration the last one.
			continueQuerying = 0

		for result in r["query"]["usercontribs"]:
			# 2022-02-13T01:46:08Z
			ts = result["timestamp"].replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
			if int(ts) > int(oldest):
				# If it's within the selected date rance.
				#try:
				if (result["comment"].find(ob["hotstring"]) != -1):
					ob["namespaces"][item[0]]["count"] += 1
					ob["namespaces"][item[0]]["edits"][result["revid"]] = result
				#except:
					#pass
					# I am not sure how this could possibly generate a KeyError for "comment", but it did when processing a large request.
					# Adding an exception handler caused the application to produce questionable output, so I'm not going to use this exception handler. I guess it can just crash and burn if you run it on all namespaces of someone with 50k edits.
			else:
				# If the timestamp of the rev being processed is older than the "oldest" cutoff:
				# Set this to 0 to make the current iteration the last one.
				continueQuerying = 0
	

	return ob



def queryPage(ob, item, prefix="", category="misc"):

	# "Item" should look like:
	# [4, "Administrators'_noticeboard", "AN"]
	#ob['debug'] = ob['debug'] + "ns: " + str(item[0]) + " keys: " + str(ob["namespaces"].keys())
	if (item[0] in ob["namespaces"].keys()):
		pass
		# I had to debug this for about an hour and a half. Stick a fork in me...
	else:
		ob = queryNamespace(ob, item)
	if (category in ob) == False:
		ob[category] = {}

	prefixedName = prefix + item[1]
	# prefixedName = "Wikipedia:" + "Administrators'_noticeboard"

	ob[category][prefixedName] = {}
	# Something like this:
	# ob["noticeboards"]["Wikipedia:Administrators'_noticeboard"]

	ob[category][prefixedName]["name"] = [item[1], item[2]]
	# ob["noticeboards"]["Wikipedia:Administrators'_noticeboard"]["name"] = ["Administrators'_noticeboard", "AN"]


	#ob["debug"] = "queryPage is running"

	# The object has been initialized now, and queryNamespace has been run
	# (whether invoked by the page selection or by the namespace being itself selected)

	# Now we're going to go through the results and find just the ones from that page

	for key in ob["namespaces"][item[0]]["edits"]:
		value = ob["namespaces"][item[0]]["edits"][key]
		if (str(value["title"]).replace("_", " ") == str(prefixedName).replace("_", " ")):
			revisionId = value["revid"]
			ob[category][prefixedName][revisionId] = value


	return ob


def query(params):

	hotString = "*/ new section"

	"""Main entry point for views.py: uses parseParams.py output to query en.wp API on namespaces, and filter by individual pages."""
	output = {
	"username": params["username"],
	"startdate": params["startdate"], 
	"enddate":  params["enddate"], 
	"namespaces": {
		},
	"hotstring": hotString,
	"debug": ""
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




	return params, "<br/>--------------------------------------------------<br/>", output


if __name__ == "__main__":
	print(docstring)
