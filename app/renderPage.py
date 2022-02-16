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
	html = """<a href="https://asdf.com">Asdf</a>"""
	html = {}
	html[""] = 



	return html


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
