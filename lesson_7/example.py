article = {
	"title" : {
	"en" : "University of Applied sciences"
	"en" : Hogeschool Utrecht
	}
}



# ___________________

iPython:
titles = { "en : Lasagne" }
titles["en"]
titles.get("en")

if "nl" in titles:
	print(titles["nl"])
else: 
	print("Title not available")


titles = { "title" : { "en" : "An English title" }
titles["title"]

titles["titles"]["en"]

titles.get("title")
print(titles)

import pprint
pprint.pprint(titles)

import json
print(json.dumps(titles, indent = 4))

# print("") will print a new line






