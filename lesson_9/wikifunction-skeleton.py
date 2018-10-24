import requests
import json

title = "Japanese cuisine"
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
req = requests.get(url)

if req.status_code != 200:
    print(f"We got an error: {req.status_code}")
    exit()

data = req.json()
print(data["extract"])
print(data["description"])


def wiki_api(title, value):



# import requests
# def lookup(title, value):
# 	# your code here
# 	return "Something"

# title = input("Give an article you want to lookup: ").strip()
# value = input("Do you want the description or extract? ").strip().lower()
# dta = lookup(title, value)
# print(f"here is the {value} for {title}: ")
# print(data)

