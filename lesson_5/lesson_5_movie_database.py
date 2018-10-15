# import the Json library
import json

# opening & Loading json file as a file (f)
json.load
f = open("movies.json")

with open("movies.json") as f:
	movies = json.load(f)

ask_year = input("What year movies do you want to see? ")
for movie in movies:
	title = movie["title"]
	year = str(movie["year"])

	if year == ask_year:
		print(f'The movie {title} is from {year}')	

ask_duration = input("from what duration length (in minutes)? ")
for movie in movies:
	title = movie["title"]
	duration = str(movie["duration"])

	if duration >= ask_duration:
		print(f'{title} has a duration of {duration} minutes')
	 	# print(title)

ask_director = input("Do you want to see movies where the director is also an actor? ").lower()
for movie in movies:
	title = movie["title"]
	director = movie["director"]
	actors = movie["actors"]

	if ask_director == "yes":
		if director in actors:
			print(f'In the movie "{title}" the director is also an actor')

ask_genre = input("Choose a genre: \nDrama film \nComedy film \nHeist film \nCrime film \nComedy-drama \nNature documentary ")
for movie in movies:
	title = movie["title"]
	genres = movie["genres"]
		
	if ask_genre in genres:
		print(title)

specific_director = input("Do you want to see movies directed only by Mike Binder? ")
for movie in movies:
	title = movie["title"]
	director = movie["director"]

	if specific_director == "yes":
		if "Mike Binder" in director:
			print(f'"{title}" has been directed by Mike Binder.')

print("Thank you for using this filter! This program will now close automatically.")
exit()