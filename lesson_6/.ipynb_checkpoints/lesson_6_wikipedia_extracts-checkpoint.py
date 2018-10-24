import requests
import json

article = input("Give an article: ").strip()
article = article.replace(" ", "_")
# url = "https://en.wikipedia.org/wiki/Hogeschool Utrecht"
print(article)

# for language in endpoint:

endpoint = "https://en.wikipedia.org/api/rest_v1/page/summary/"
url = endpoint + article
print(url)

req = requests.get(url)
print(req)

if req.status_code != 200:
	print("This website is not reachable! This program will automatically close.")
	exit()

req.text
print(req.text)

data = json.loads(req.text)
title = data["title"]
description = data["description"]
extract = data["extract"]
print(f'The title is: {title} "\n"The description is: {description} "\n"The extract is: {extract}"\n"')

# languages = {
# 	"en" : "English",
# 	"nl" : "Dutch",
# 	"es" : "Spanish"
# }

# for code, language in languages.items():
# 	print(code)
# 	print(language)


# language = ["en", "es", "nl"]
# for 




# for title in article:

# for description in article:

# for extract in article:




# req = requests.get()




# import requests
# import json

# url = "https://en.wikipedia.org/api/rest_v1/page/summary/Amsterdam"
# r =  requests.get(url)
# #print(type(r.text))

# data = json.loads(r.text)

# print(data["title"])


# for key, value in data.items():
# 	print(key)


# ____________________________

	# import requests
# import json

# url = "https://en.wikipedia.org/wiki/HU_University_of_Applied_Sciences_Utrecht"
# req  = requests.get(url)

# print(type(req.text))
# data = json.loads(req.text)
# print(data["title"])

# for key in data:
# 	value = data[key]
# 	print(key, value)