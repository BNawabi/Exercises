# the names of the friends are listed below
names = ["Billy", "Karel", "Frank"]

# giving snacks an empty list
snacks = []

# loop the names (friends) inside the variable 'names'
for friends in names:
	
	#adding the empty list of snacks with an input question
	snacks.append(input(friends + ", what is your favourite snack? "))

# telling the system that it should start with the index of 0 in the list
index = 0

# calling the names of the names-list and make it print what their answer on the input was
for friends in names:
	print(friends + "'s favo snack is: " + snacks[index])
	
	# this makes the loop start from 0 and then add 1 with every loop
	index += 1

