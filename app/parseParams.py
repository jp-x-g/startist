docstring = """
 JPxG, 2022 February 12
 (Placeholder)
"""

def mapping():
	mappingDict = {}
	mappingDict["namespaces"] = {
		"01":  [0,    "",                       "MAIN"],
		"01t": [1,    "Talk",                   "T"],
		"02":  [2,    "User",                   "U"],
		"02t": [3,    "User_talk",              "UT"],
		"03":  [4,    "Wikipedia",              "WP"],
		"03t": [5,    "Wikipedia_talk",         "WT"],
		"04":  [6,    "File",                   "F"],
		"04t": [7,    "File_talk",              "FT"],
		"05":  [8,    "MediaWiki",              "MW"],
		"05t": [9,    "MediaWiki_talk",         "MWT"],
		"06":  [10,   "Template",               "T"],
		"06t": [11,   "Template_talk",          "TT"],
		"07":  [12,   "Help",                   "H"],
		"07t": [13,   "Help_talk",              "HT"],
		"08":  [14,   "Category",               "C"],
		"08t": [15,   "Category_talk",          "CT"],
		"09":  [100,  "Portal",                 "P"],
		"09t": [101,  "Portal_talk",            "PT"],
		"10":  [118,  "Draft",                  "D"],
		"10t": [119,  "Draft_talk",             "DT"],
		"11":  [710,  "TimedText",              "TT"],
		"11t": [711,  "TimedText_talk",         "TTT"],
		"12":  [828,  "Module",                 "M"],
		"12t": [829,  "Module_talk",            "MT"],
		"13":  [2300, "Gadget",                 "G"],
		"13t": [2301, "Gadget_talk",            "GT"],
		"14":  [2302, "Gadget_definition",      "GD"],
		"14t": [2303, "Gadget_definition_talk", "GDT"]
  	}
	mappingDict["noticeboards"] = {
		"01":  [4, "Administrators'_noticeboard",               "AN"],
		"02":  [4, "Administrators'_noticeboard/AN3",           "AN3"],
		"03":  [4, "Administrators'_noticeboard/Incidents",     "ANI"],
		"04":  [4, "Arbitration/Requests/Enforcement",          "AE"],
		"05":  [4, "Biographies_of_living_persons/Noticeboard", "BLPN"],
		"06":  [4, "Conflict_of_interest/Noticeboard",          "COIN"],
		"07":  [4, "Dispute_resolution_noticeboard",            "DRN"],
		"08":  [4, "External_links/Noticeboard",                "ELN"],
		"09":  [4, "Fringe_theories/Noticeboard",               "FTN"],
		"10":  [4, "No_original_research/Noticeboard",          "NORN"],
		"11":  [4, "Neutral_point_of_view/Noticeboard",         "NPOVN"],
		"12":  [4, "Reliable_sources/Noticeboard",              "RSN"],
		"13":  [4, "Bureaucrats'_noticeboard",                  "BN"],
		"14":  [4, "Bots/Noticeboard",                          "BOTN"]
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

	return mappingDict


def parse(params):
	output = {}
	output["namespaces"] = []
	output["noticeboards"] = []
	output["villagepumps"] = []
	output["refdesks"]: []
	output["helptea"]: []

	for item in params:
		pass


	return mapping()
	#return output















if __name__ == "__main__":
	print(docstring)