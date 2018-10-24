from bs4 import Beautifulsoup
import pandas

with open("hu.html") as f:
	page = Beautifulsoup(f, "lxml")

page.select(title)[0].get_text() # .get_text() only takes the text, without h1 / h2 / etc
print(title) #.upper() / .lower()

headings = page.select("h2")
len(headings)

for heading in headings:
	print(heading.get_text().strip())

flyer_title = page.select(".flyer_content_title")

flyer_title[0].get_text() 

heading_title = flyer_title[0].get_text()
print(heading_title)

___

# PANDAS 

df = pd.DataFrame([{
	"title" : heading_title,
	"text" : text


	}])

df

___


