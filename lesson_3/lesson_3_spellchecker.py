wrong_spelled = ["fortnyte", "viva", "vallout", "destini", "minekraft", "battleveld"]
well_spelled = ["fortnite", "fifa", "fallout", "destiny", "minecraft", "battlefield"]
sentence = input("Name your favourite game: ")
sentence = sentence.split()
new_sentence = []

for word in sentence:
	if word in wrong_spelled:
		index = wrong_spelled.index(word)
		new_word = well_spelled[index]
		print("WARNING! " + word + " is spelled wrong. You should spell " + word + " as " + new_word + ".")