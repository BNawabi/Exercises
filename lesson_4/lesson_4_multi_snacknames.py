# list of friends
friends = [
    ["Barrie"],
    ["Sjaak"],
    ["Hans"]
]

# loop the items in the list friends and gives the characters of each name individually
for friend in friends:
    name = friend[0]
    name_len = len(name)
    print("The name " + name + " consists " + str(name_len) + " characters" )
    
    # ask for favorite snack and add them to a new list
    favo_snack = input(name + ", What is your favo snack? ")
    friend.append(favo_snack)

# loop the items in the list friends and show what they like (based on their answer on favo_snack input in a new list)
for friend in friends:
    print(friend[0] + "'s favorite snack is: " + friend[1])



