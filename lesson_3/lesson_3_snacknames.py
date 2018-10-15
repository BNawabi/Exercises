names = [
    ["Tinus", "Twix"]
    ["Barrie", "Oreo"]
    ["Hans", "Pie"]
]

for index, person in enumerate(names):
    person = names[index]
    personlen = len(person) 
    print(person + " has " + str(personlen) + " characters.")
    favo_snack = input("What is your favourite snack? ")
    snacks = []
    snacks.append(favo_snack)
    print()