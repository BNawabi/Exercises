import requests

ask_url = input("Fill in an URL: ").strip()
r = requests.get(ask_url)
r.status_code
r.headers
print(r.status_code)

if r.status_code != 200:
	print("Error! This website is not reachable")
	exit()

for key, value in r.headers.items():
	print(key, value)





# _________________________________________

# url = "https://en.wikipedia.org/wiki/List_of_Wikipedias"

# requests.get
# r = request.get(url)

# r.status_code

# r.headers

# r.url

# r.text

# curl

# curl -i