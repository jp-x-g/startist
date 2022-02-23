# 2022 February 20

docstring = """
JPxG, 2022 February 20
Basic diagnostic logging to measure server load and detect bugs.
Parses stuff out of params like total queries, total hits, total results, and runtime.
Inputs should be [params, output], from makeQueries.py (called by views.py).

"""
import json
import os
from pathlib import Path

def log(inputs):
	"""Inputs should be [params, output], from makeQueries.py (called by views.py)"""

	runstamp = inputs[0]["runstamp"]

	profile = {
	"sec": inputs[0]["elapsed"],
	"fmt": inputs[1]["format"],
	"qry": inputs[1]["totalQueries"],
	"res": inputs[1]["totalResults"],
	"hit": inputs[1]["totalHits"],
	"exp": inputs[1]["exceptions"]
	}

	# Now we try to write this out to a file.

	paths = ["data", "data/log"]
	# Descend into the log folder.

	logPath = paths[len(paths)-1]
	# Set logPath to be whatever the last item in this array is.

	logfileName = "startist.log"
	masterLogName = "master.log"
	# Names for the logfiles.

	for path in paths:
		path = Path(os.getcwd() + "/" + path)
		path.mkdir(mode=0o777, exist_ok=True)
		# If the paths don't exist already, create them.

	try:
		logFile = open(str(logPath + "/" + logfileName), "r")
		logContents = json.load(logFile)
		logFile.close()
		# Read the file and parse it.

		logContents[runstamp] = profile
		# Store profile for this search in the json.

		logFile = open(str(logPath + "/" + logfileName), "w")
		logFile.write(json.dumps(logContents, indent=1, ensure_ascii=False))
		logFile.close()
		# Write this out to the file.

	except (FileNotFoundError):
		logFile = open(str(logPath + "/" + logfileName), "w")
		logContents = {}
		logFile.write(json.dumps(logContents, indent=1, ensure_ascii=False))
		logFile.close()

	try:
		masterLogFile = open(str(logPath + "/" + masterLogName), "r")
		masterLogContents = json.load(masterLogFile)
		masterLogFile.close()

		masterLogContents["searches"]   += 1
		masterLogContents["queries"]    += int(inputs[1]["totalQueries"])
		masterLogContents["results"]    += int(inputs[1]["totalResults"])
		masterLogContents["hits"]       += int(inputs[1]["totalHits"])
		masterLogContents["exceptions"] += int(inputs[1]["exceptions"])

		masterLogFile = open(str(logPath + "/" + masterLogName), "w")
		masterLogFile.write(json.dumps(masterLogContents, indent=2, ensure_ascii=False))
		masterLogFile.close()

	except (FileNotFoundError):
		masterLogFile = open(str(logPath + "/" + masterLogName), "w")
		masterLogContents = {
			"searches": 0,
			"queries": 0,
			"results": 0,
			"hits": 0,
			"exceptions": 0
		}
		masterLogFile.write(json.dumps(masterLogContents, indent=2, ensure_ascii=False))
		masterLogFile.close()

	# Now we have made sure that logContents and masterLogContents exist.

	# params has stuff like:
	# username, startdate, enddate, format, runstamp
	# namespaces, noticeboards, refdesks, villagepumps, misc



	#import logging

	#logging.basicConfig(
	#filename=logPath + logfileName + ".log", encoding="utf-8", level=logging.DEBUG)





if __name__ == "__main__":
	print(docstring)