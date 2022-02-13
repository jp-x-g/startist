docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""

import json

def render(params):
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
		dump = json.dumps(params, indent=4)
		dump = dump.replace("\n", "<br />")
		dump = dump.replace("  ", "&nbsp; ")
	except TypeError:
		dump = str(params)
		
	dump = header + dump + footer




	return dump

if __name__ == "__main__":
	print(docstring)
