movie_facts = { 
	"title" : "Venom",
	"release_year" : 2018,
	"duration" : 117,
	"director" : "Ruben Fleischer",
	"actors" : ["Harrison Ford", "Rutger Hauer", "Sean Young"]
}

movie_facts["duration"] = str(movie_facts["duration"]) + " minutes"
movie_facts["actors"] = ", ".join(movie_facts["actors"])

for key, movie in movie_facts.items():
	print(key, movie)
	# print(movie_facts["duration"])


# print(f'{movie_facts["title"]} has been released in {movie_facts["release_year"]}, has a duration of {movie_facts["duration"]} minutes and is been directed by {movie_facts["director"]}')



