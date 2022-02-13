docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""
import requests
S = requests.Session()
apiUrl = "https://en.wikipedia.org/w/api.php" 

def queryNamespace(ob, item, include=False, debug=False):	
	ob["namespaces"][item[0]] = {}
	ob["namespaces"][item[0]]["include"] = include
	ob["namespaces"][item[0]]["count"] = -1
	ob["namespaces"][item[0]]["edits"] = "SELECT * FROM page WHERE baba_booey = TRUE"
	if (debug == True):
		ob["namespaces"][item[0]]["edits"] = "Wowzies!"
	# Initialize object for this namespace.

	# Now we're going to actually hit the API and get all edits from this namespace.

	continueQuerying = 1
	continueTimestamp = "20992359591234|10000000000"
	queryParams = {
		"action": "query",
		"format": "json",
		"list": "usercontribs",
		"ucuser": ob["username"],
		"ucnamespace": item[0],
		"uccontinue": continueTimestamp
		}
	ob["query"] = queryParams
	# 2099 December 31, 23:59, 1234 milliseconds. We want everything from then back to now.
	while (continueQuerying == 1):

		ob["query"] = queryParams
		continueQuerying = 0




	return ob



def queryPage(ob, item, prefix="", category="misc"):
	if ((str(item[0]) in ob["namespaces"]) == False):
		ob = queryNamespace(ob, item, debug=True)
	if (category in ob) == False:
		ob[category] = {}
	ob[category][prefix + item[1]] = {}
	ob[category][prefix + item[1]]["name"] = [item[1], item[2]]
	return ob


def query(params):
	output = {
	"username": params["username"],
	"startdate": params["startdate"], 
	"enddate":  params["enddate"], 
	"namespaces": {
		},
	"pages": {
		}
	}

	# This is a special case, because the entire namespace is being searched, not just one page.
	for item in params["namespaces"]:
		output = queryNamespace(output, item, include=True)
		pass
	# Everything in these categories is in namespace 4 (Wikipedia).
	for cat in ["noticeboards", "refdesks", "villagepumps"]:
		for item in params[cat]:
			output = queryPage(output, item, prefix="Wikipedia:", category=cat)
	for item in params["misc"]:
		output = queryPage(output, item, prefix="Wikipedia:", category="misc")
		pass

	return params, output


if __name__ == "__main__":
	print(docstring)
