docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""

import json
from app import parseParams

def renderJSON(params, info):
	return {"params": params, "info": info}

def renderJSONTEXT(params, info):
	renderInput = [params, info]
	header =    """<!doctype html>"""
	header += """\n<html> """
	header += """\n<head> """
	header += """\n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> """
	header += """\n  <meta name=viewport content="width=device-width, initial-scale=1">"""
	header += """\n  <title>Startist: results</title>"""
	header += """\n  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/startist.css') }}">"""
	header += """\n  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/mw.ui.css') }}">"""
	header += """\n</head>"""
	header += """<body>"""

	footer =  """</body>"""
	footer += "\n</html>"

	try:
		dump = json.dumps(renderInput, indent=4)
		dump = dump.replace("\n", "<br />")
		dump = dump.replace("  ", "&nbsp; ")
		#dump = dump + " Didn't catch a TypeError in renderPage"
	except TypeError:
		dump = str(renderInput) + "Caught a TypeError in renderPage"

	dump = header + dump + footer

	return dump

def renderHTMLOld(params, info):

	def newRow (contents):
		"""Avoid crapping up the code by defining an add-row function"""
		newRowString =  """\n<tr>"""
		newRowString += """\n<tr>"""
		newRowString += """\n""" + contents
		newRowString += """\n</tr>"""
		return newRowString

	def newCell (contents):
		"""Avoid crapping up the code by defining an add-cell function"""
		newCellString  = """\n<td>"""
		newCellString += """\n""" + contents
		newCellString += """\n</td>"""
		return newCellString

	renderInput = [params, info]
	header =    """<!doctype html>"""
	header += """\n<html> """
	header += """\n<head> """
	header += """\n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/> """
	header += """\n  <meta name=viewport content="width=device-width, initial-scale=1">"""
	header += """\n  <title>Startist: results</title>"""
	header += """\n  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/startist.css') }}">"""
	header += """\n  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/mw.ui.css') }}">"""
	header += """\n</head>"""
	header += """<body>"""

	table =  """"""
	table += """\n<table>"""

	titles = {
	"namespaces":   "Namespaces",
	"noticeboards": "Noticeboards",
	"refdesks":     "Reference desks",
	"villagepumps": "Village pumps",
	"misc":         "Miscellaneous",
	}

	nsMapping = parseParams.mapping(key="namespaces")
	# e.g. nsMapping["14"] is ["Category:", "C"]

	for cat in ["namespaces", "noticeboards", "refdesks", "villagepumps", "misc"]:
		if cat in info:
			table += newRow(newCell("<center><b>" + titles[cat] + "</b></center>"))
			if cat == "namespaces":
				for ns in info["namespaces"]:
					if info["namespaces"][ns]["include"] != "false":
						nsString = str(nsMapping[ns][0]).replace("_", " ").replace(":", "")
						# Remove colons, underscores to render table row heading.
						if nsString == "":
							nsString = "(main)"
						rowToAdd = newCell("<center>" + nsString + "</center>")
						rowToAdd += newCell(str(info["namespaces"][ns]["count"]))
						table += newRow(rowToAdd)
			else:
				for item in info[cat]:
					heading = str(item)
					if (cat == "noticeboards") or (cat == "refdesks") or (cat == "villagepumps"):
						heading = heading[(heading.find(":")+1):].replace("_", " ")
						# Remove namespace from the heading, and replace "_" with " "
					newCells= newCell(heading) + newCell(str(info[cat][item]["count"]))
					table += newRow(newCells)

		pass

	table += """\n</table>"""

	# Okay, all the actual data has been added, we will now close everything up.
	footer =  """</body>"""
	footer += """\n</html>"""


	#try:
	#	dump = json.dumps(renderInput, indent=4)
	#	dump = dump.replace("\n", "<br />")
	#	dump = dump.replace("  ", "&nbsp; ")
	#	dump = dump + " Didn't catch a TypeError in renderPage"
	# except TypeError:
	#	dump = str(renderInput) + "Caught a TypeError in renderPage"

	dump = header + table + footer

	return dump

def renderHTML(params, info):

	# Yeah, this is about to get absolutely brutal.
	# I had intended to just have this script render the output to a string, and pass that back to views.py.
	# It turns out what I needed to do was have views.py invoke a Jinja template with this program's output as an argument.
	# This didn't work well with how I'd designed the json from previous scripts, so this is hideous.

	html = """<a href="https://asdf.com">Asdf</a>"""
	html = {}
	html["summary"] = ["asdf", "qwer"]

	titles = {
	"namespaces":   "Namespaces",
	"noticeboards": "Noticeboards",
	"refdesks":     "Reference desks",
	"villagepumps": "Village pumps",
	"misc":         "Miscellaneous",
	}

	nsMapping = parseParams.mapping(key="namespaces")
	# e.g. nsMapping["14"] is ["Category:", "C"]

	jinjaInput = {}
	jinjaInput["summary"] = {}
	jinjaInput["profile"] = {
	"username":     params["username"],
	"startdate":    params["startdate"],
	"enddate":      params["enddate"],
	"format":       params["format"],
	"runstamp":     params["runstamp"],
	"finished":     params["finished"],
	"elapsed":      params["elapsed"],
	"totalQueries": info["totalQueries"],
	"totalResults": info["totalResults"],
	"totalHits":    info["totalHits"]
	}
	jinjaInput["wtf"] = 0
	jinjaInput["wtf2"] = 0


	for cat in ["namespaces", "noticeboards", "refdesks", "villagepumps", "misc"]:
		if cat in info:
			jinjaInput["summary"][titles[cat]] = []
			if cat == "namespaces":
				for ns in info["namespaces"]:
					if info["namespaces"][ns]["include"] != False:
						nsString = str(nsMapping[ns][0]).replace("_", " ").replace(":", "")
						# Remove colons, underscores to render table row heading.
						if nsString == "":
							nsString = "(main)"
						jinjaInput["summary"][titles[cat]].append([nsString, str(info["namespaces"][ns]["count"])])
						# Append a two-item array: the namespace string and the section count from it.
			else:
				for item in info[cat]:
					heading = str(item)
					if (cat == "noticeboards") or (cat == "refdesks") or (cat == "villagepumps"):
						heading = heading[(heading.find(":")+1):].replace("_", " ")
						# Remove namespace from the heading, and replace "_" with " "
					jinjaInput["summary"][titles[cat]].append([heading, str(info[cat][item]["count"])])
					# Same as above: heading and section count.

		pass
	# End of summary-generation code. Now moving on to the edits.

	jinjaInput["edits"] = {}
	for cat in ["namespaces", "noticeboards", "refdesks", "villagepumps", "misc"]:
		if cat in info:
			# If info has a ["namespaces"], ["noticeboards"], etc.
			if cat == "namespaces":
				for ns in info["namespaces"]:
					# For each namespace in info ("4", "5", etc)
					if info["namespaces"][ns]["include"] != False:
							for edit in info["namespaces"][ns]["edits"]:
								info["namespaces"][ns]["edits"][edit]["ns"] = nsMapping[info["namespaces"][ns]["edits"][edit]["ns"]][0].replace("_", " ")
								# Replace "3" with "User talk:", for example.
								if (info["namespaces"][ns]["edits"][edit]["title"].find(info["namespaces"][ns]["edits"][edit]["ns"]) == 0):
									info["namespaces"][ns]["edits"][edit]["title"] = info["namespaces"][ns]["edits"][edit]["title"].replace(info["namespaces"][ns]["edits"][edit]["ns"], "", 1)
									# Replace the first instance of the namespace string.
									# Talk:Dogs becomes Dogs, for example.
								try:
									revId = info["namespaces"][ns]["edits"][edit]["revid"]
									jinjaInput["edits"][revId] = (info["namespaces"][ns]["edits"][edit])

									sectionTitle = info["namespaces"][ns]["edits"][edit]["comment"]
									sectionTitle = sectionTitle.replace("/* ", "")
									sectionTitle = sectionTitle[0:sectionTitle.find(" */ new section")]
									# Strip section title from edit summary.
									articleTitle = info["namespaces"][ns]["edits"][edit]["title"]
									# Get article title.
									sectionTitle = "https://en.wikipedia.org/wiki/" + info["namespaces"][ns]["edits"][edit]["ns"] + articleTitle + "#" + sectionTitle
									# Construct URL.
									sectionTitle = sectionTitle.replace(" ", "_")
									# Put in underscores to make the URL work.
									jinjaInput["edits"][revId]["sectionlink"] = sectionTitle
								except KeyError:
									jinjaInput["wtf"] += 1
									# Stupid kludge. Do not deploy this.
			else:
				for item in info[cat]:
					# for everything in info["noticeboards"] or info ["refdesks"]...
					# i.e. item would be "Wikipedia:Teahouse" or "Wikipedia:Help_desk"
						if "edits" in info[cat][item]:
							for edit in info[cat][item]["edits"]:
								try:
									nameString = info[cat][item]["edits"][edit]["ns"]

									if nameString in nsMapping:
										nameString = nsMapping[nameString][0].replace("_", " ")

									info[cat][item]["edits"][edit]["ns"] = nameString

									# info[cat][item]["edits"][edit]["ns"] = "ooga booga"
								except KeyError:
									jinjaInput["wtf2"] += 1
									# Stupid kludge.
								# Replace "3" with "User talk:", for example.
								if (info[cat][item]["edits"][edit]["title"].find(info[cat][item]["edits"][edit]["ns"]) == 0):
									info[cat][item]["edits"][edit]["title"] = info[cat][item]["edits"][edit]["title"].replace(info[cat][item]["edits"][edit]["ns"], "", 1)
									# Replace the first instance of the namespace string.
									# Talk:Dogs becomes Dogs, for example.
								jinjaInput["edits"][info[cat][item]["edits"][edit]["revid"]] = (info[cat][item]["edits"][edit])

								sectionTitle = info[cat][item]["edits"][edit]["comment"]
								sectionTitle = sectionTitle.replace("/* ", "")
								sectionTitle = sectionTitle[0:sectionTitle.find(" */ new section")]
								# Strip section title from edit summary.
								articleTitle = info[cat][item]["edits"][edit]["title"]
								# Get article title.
								sectionTitle = "https://en.wikipedia.org/wiki/" + info[cat][item]["edits"][edit]["ns"] + articleTitle + "#" + sectionTitle
								# Construct URL.
								sectionTitle = sectionTitle.replace(" ", "_")
								# Put in underscores to make the URL work.
								jinjaInput["edits"][info[cat][item]["edits"][edit]["revid"]]["sectionlink"] = sectionTitle

	return jinjaInput

	# Note that this is being parsed with results.html.


def render(renderInput):
	params = renderInput[0]
	info = renderInput[1]

	if (info["format"] == "HTML"):
		return renderHTML(params, info)
	if (info["format"] == "HTMLbare"):
		return renderHTMLOld(params, info)
	elif (info["format"] == "JSON"):
		return renderJSON(params, info)
	elif (info["format"] == "JSONTEXT"):
		return renderJSONTEXT(params, info)
	elif (info["format"] == "CSV"):
		return renderCSV(params, info)
	elif (info["format"] == "TSV"):
		return renderTSV(params, info)




if __name__ == "__main__":
	print(docstring)
