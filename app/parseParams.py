docstring = """
 JPxG, 2022 February 12
 This program does one of two things.
 The first thing
"""

from datetime import date
from datetime import datetime
from datetime import timedelta
# For validating timestamps.

def mapping(key="checkbox"):
	"""Return dictionary with checkbox IDs keyed to namespaces, long forms, and short forms.

	Items are "namespaces", "noticeboards", "refdesks", "villagepumps" and "misc".
	- Each item is a dict, with checkbox IDs from the input form as keys.
	-- Each value is an array of three items corresponding to that checkbox ID:
	--- Namespace ID (int, like 4)
	--- Full name (string, like "Wikipedia" or "Bots/Noticeboard")
	--- Abbreviation (string, like "WP" or "BOTN")
	"""
	mappingDict = {}

	mappingDict["namespaces"] = {
		"01":  [0,    "",                        "MAIN"],
		"01t": [1,    "Talk:",                   "T"],
		"02":  [2,    "User:",                   "U"],
		"02t": [3,    "User_talk:",              "UT"],
		"03":  [4,    "Wikipedia:",              "WP"],
		"03t": [5,    "Wikipedia_talk:",         "WT"],
		"04":  [6,    "File:",                   "F"],
		"04t": [7,    "File_talk:",              "FT"],
		"05":  [8,    "MediaWiki:",              "MW"],
		"05t": [9,    "MediaWiki_talk:",         "MWT"],
		"06":  [10,   "Template:",               "T"],
		"06t": [11,   "Template_talk:",          "TT"],
		"07":  [12,   "Help:",                   "H"],
		"07t": [13,   "Help_talk:",              "HT"],
		"08":  [14,   "Category:",               "C"],
		"08t": [15,   "Category_talk:",          "CT"],
		"09":  [100,  "Portal:",                 "P"],
		"09t": [101,  "Portal_talk:",            "PT"],
		"10":  [118,  "Draft:",                  "D"],
		"10t": [119,  "Draft_talk:",             "DT"],
		"11":  [710,  "TimedText:",              "TT"],
		"11t": [711,  "TimedText_talk:",         "TTT"],
		"12":  [828,  "Module:",                 "M"],
		"12t": [829,  "Module_talk:",            "MT"],
		"13":  [2300, "Gadget:",                 "G"],
		"13t": [2301, "Gadget_talk:",            "GT"],
		"14":  [2302, "Gadget_definition:",      "GD"],
		"14t": [2303, "Gadget_definition_talk:", "GDT"]
  	}
	mappingDict["noticeboards"] = {
		"01":  [4, "Administrators'_noticeboard",               "AN"],
		"02":  [4, "Administrators'_noticeboard/AN3",           "AN3"],
		"03":  [4, "Administrators'_noticeboard/Incidents",     "ANI"],
		"04":  [4, "Arbitration/Requests/Enforcement",          "AE"],
		"05":  [4, "Biographies_of_living_persons/Noticeboard", "BLPN"],
		"06":  [4, "Bots/Noticeboard",                          "BOTN"],
		"07":  [4, "Bureaucrats'_noticeboard",                  "BN"],
		"08":  [4, "Conflict_of_interest/Noticeboard",          "COIN"],
		"09":  [4, "Dispute_resolution_noticeboard",            "DRN"],
		"10":  [4, "External_links/Noticeboard",                "ELN"],
		"11":  [4, "Fringe_theories/Noticeboard",               "FTN"],
		"12":  [4, "No_original_research/Noticeboard",          "NORN"],
		"13":  [4, "Neutral_point_of_view/Noticeboard",         "NPOVN"],
		"14":  [4, "Reliable_sources/Noticeboard",              "RSN"]
	}
	mappingDict["refdesks"] = {
		"01": [4, "Reference_desk",               "RD"],
		"02": [4, "Reference_desk/Computing",     "RD/COMP"],
		"03": [4, "Reference_desk/Entertainment", "RD/ENT"],
		"04": [4, "Reference_desk/Humanities",    "RD/HUM"],
		"05": [4, "Reference_desk/Language",      "RD/LANG"],
		"06": [4, "Reference_desk/Mathematics",   "RD/MATH"],
		"07": [4, "Reference_desk/Science",       "RD/SCI"],
		"08": [4, "Reference_desk/Miscellaneous", "RD/MISC"]
	}
	mappingDict["villagepumps"] = {
		"01": [4, "Village_pump_(policy)",        "VP/P"],
		"02": [4, "Village_pump_(technical)",     "VP/T"],
		"03": [4, "Village_pump_(proposals)",     "VP/PR"],
		"04": [4, "Village_pump_(idea lab)",      "VP/IL"],
		"05": [4, "Village_pump_(WMF)",           "VP/WMF"],
		"06": [4, "Village_pump_(miscellaneous)", "VP/M"]
	}
	mappingDict["misc"] = {
		"helpdesk":     [4, "Help_desk", "HD"],
		"teahouse":     [4, "Teahouse", "TH"]
	}

	if (key == "checkbox"):
		return mappingDict

	if (key == "page"):
		pageKeyDict = {}
		for item in mappingDict:
			# for "namespaces", "noticeboards", etc
			pageKeyDict[item] = {}
			for subitem in item:
				# for "0", "1", etc
				pageKeyDict[item][subitem[1]] = [subitem[0], subitem[2]]
		return pageKeyDict

	if (key == "namespaces"):
		namespaceDict = {
		0:    ["",                        "MAIN"],
		1:    ["Talk:",                   "T"],
		2:    ["User:",                   "U"],
		3:    ["User_talk:",              "UT"],
		4:    ["Wikipedia:",              "WP"],
		5:    ["Wikipedia_talk:",         "WT"],
		6:    ["File:",                   "F"],
		7:    ["File_talk:",              "FT"],
		8:    ["MediaWiki:",              "MW"],
		9:    ["MediaWiki_talk:",         "MWT"],
		10:   ["Template:",               "T"],
		11:   ["Template_talk:",          "TT"],
		12:   ["Help:",                   "H"],
		13:   ["Help_talk:",              "HT"],
		14:   ["Category:",               "C"],
		15:   ["Category_talk:",          "CT"],
		100:  ["Portal:",                 "P"],
		101:  ["Portal_talk:",            "PT"],
		118:  ["Draft:",                  "D"],
		119:  ["Draft_talk:",             "DT"],
		710:  ["TimedText:",              "TT"],
		711:  ["TimedText_talk:",         "TTT"],
		828:  ["Module:",                 "M"],
		829:  ["Module_talk:",            "MT"],
		2300: ["Gadget:",                 "G"],
		2301: ["Gadget_talk:",            "GT"],
		2302: ["Gadget_definition:",      "GD"],
		2303: ["Gadget_definition_talk:", "GDT"]
		}
		return namespaceDict



def valiDate(d):
	e = ""
	d = d.strip()
	print("")
	print("String: " + d)
	for char in d:
		if char in "1234567890":
			e = e + char
	# Remove everything that isn't a digit.
	# Check to see if it's a valid date FORMAT.

	if (len(e) > 14):
		return "INVALID: More than 14 digits in date. Could not parse."
	if (len(e) < 8):
		return "INVALID: More than 8 digits in date. Could not parse."
	if (len(e) > 8) and (len(e) < 14):
		return "INVALID: Timestamp did not use YYYY-MM-DD or YY-MM-DD HH:MM:SS. Could not parse date."

	#print("Formatted string: " + e)

	if (e == ""):
		return ""

	# Now we check to see if it's actually a valid date.
	#print("First four: " + e[0:4])
	year  =  int(e[0:4])
	month =  int(e[4:6])
	day   =  int(e[6:8])
	# 20221231 235959
	# 01234567 890123

	if year > 2112:
		return "INVALID: Year higher than 2099. Be less forward-thinking."
	if year < 2000:
		return "INVALID: Year lower than 2000. Be more forward-thinking."
	if month > 12:
		return "INVALID: Month higher than 12. Octember is a lie."
	if month < 1:
		return "INVALID: Month lower than 1. Zerouary is a lie."
	lengths = [420, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if day > lengths[month]:
		return "INVALID: Day higher than exists for that month. Try the knuckle-counting thing next time."
	if day < 1:
		return "INVALID: Day lower than 1. Dates aren't zero-indexed, buddy."

	if len(e) == 8:
		# If it's just YYYYMMDD, we're done.
		return e + "000000"

	else:
		# Otherwise, we validate the timestamp.
		hour   = int(e[8:10])
		minute = int(e[10:12])
		second = int(e[12:14])
		if hour > 23:
			return "INVALID: hour higher than 23. Check timestamp, or use YYYY-MM-DD."
		if minute > 59:
			return "INVALID: minute higher than 59. Check timestamp, or use YYYY-MM-DD."
		if second > 59:
			return "INVALID: second higher than 59. Check timestamp, or use YYYY-MM-DD."

	return e

def parse(params):
	"""Parses form selections and returns them as a structured dictionary.

	Output will be structured the same way as mapping().
	However, instead of a dictionary, each item is an array of the selected pages/namespaces/etc.
	For example, selecting BOTN and BN will cause the "noticeboards" item to look like:
	[[4, "Bots/Noticeboard", "BOTN"], [4, "Bureaucrats'_noticeboard", "BN"]]
	"""

	output = {}
	output["username"] = params["username"]
	output["startdate"] = ""
	output["enddate"] = ""
	output["format"] = params["format"]
	# Initialize metadata fields.

	output["namespaces"] = []
	output["noticeboards"] = []
	output["refdesks"] = []
	output["villagepumps"] = []
	output["misc"] = []
	# Initialize namespace/page search fields.

	m = mapping()
	#return m

	for item in params:
		if ("boxns" in item):
			number = item[5:]
			if (number in m["namespaces"]):
				output["namespaces"].append(m["namespaces"][number])
		if ("boxnb" in item):
			number = item[5:]
			if (number in m["noticeboards"]):
				output["noticeboards"].append(m["noticeboards"][number])
		if ("boxrd" in item):
			number = item[5:]
			if (number in m["refdesks"]):
				output["refdesks"].append(m["refdesks"][number])
		if ("boxvp" in item):
			number = item[5:]
			if (number in m["villagepumps"]):
				output["villagepumps"].append(m["villagepumps"][number])
		if ("boxhd" in item):
			output["misc"].append(m["misc"]["helpdesk"])
		if ("boxth" in item):
			output["misc"].append(m["misc"]["teahouse"])
	#return mapping()


	# Now we need to validate the start (oldest) dates and end (newest) dates, if they exist.

	if (params["startdate"]):
		output["startdate"] = valiDate(params["startdate"])

	if (params["enddate"]):
		output["enddate"] = valiDate(params["enddate"])

	today = datetime.today()
	daysOffset = 30 * 6
	offset = timedelta(
		days=daysOffset
	)
	backthen = today - offset
	backthenFormat = backthen.strftime("%Y%m%d") + "000000"

	if output["startdate"] == "":
		output["startdate"] = backthenFormat
		# If there's no oldest date provided, set it to the longest offset.

	oldestYYYYMMDD = output["startdate"][0:8]
	oldestDate = datetime.strptime(oldestYYYYMMDD, "%Y%m%d")
	# Create a datetime object from the oldest date.

	if oldestDate < backthen:
		output["startdate"] = backthenFormat
		# If oldest date is too far back, set it to the oldest allowed date.


	if (output["startdate"] != "") and (output["enddate"] != ""):
		if int(output["startdate"]) > int(output["enddate"]):
			output["startdate"] = "INVALID: Oldest date after newest date."
			output["enddate"]   = "INVALID: Oldest date after newest date."


	return output
	# This is being called from views.py.

if __name__ == "__main__":
	print(docstring)
