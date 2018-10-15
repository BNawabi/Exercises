# open the csv file
paintings = open("paintings.csv")

# open a textfile and make sure to "w"rite 
f = open("extrapainters.txt", "w")

# loop in the csv files, split them into a list and then create new variables from list-itmes
for artwork in paintings:
	artwork = artwork.split(",")
	name_art = artwork[0]
	name_painter = artwork[1]
	price_art = artwork[2]
	price_art = "$" + price_art + " million"

	# print the variables above into a new sentence
	print(name_painter + " has painted " + name_art + " and the current price is " + price_art)

# asking for a new painter and add it into the text file
extra_painter = input("Add one more painter: ")
extra_artwork = input("Name his/her artwork: ")
extra_price = input("What is the current price of this artwork (only digits)? ")
extra_price = "$" + extra_price + ", in other words: pricesle$$!"

#this writes it to the textfile in stead of printing and showing it on screen
f.write(extra_painter + " created " + extra_artwork + " has the current price of " + extra_price)

paintings.close()
f.close()