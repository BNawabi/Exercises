# This is a version of snacknames (lesson 3) that is written poorly
# on purpose, so you can refactor it into something better

names = []
snacks = []

ask_times = input("How many names would you like to add? ")

for times in range(3):
    loop_names = input("What is your name? ")
    names.append(loop_names)

for index, loop_names in enumerate(names):
    name_len = len(loop_names)
    favo_snack = input(f"{loop_names}, name your favo snack: ")
    snacks.append(favo_snack)
    print(f"{loop_names} has {name_len} characters and likes {favo_snack}")

print(f"")

# NEW (MY PREVIOUS EXAMPLE)
# names = ["Tinus", "Barrie", "Hans"]
# snacks = []

# for index, name in enumerate(names):
#     name_len = len(name)
#     favo_snack = input("Name your favo snack: ")
#     snacks.append(favo_snack)
#     print(f'{name} has {name_len} characters and likes {favo_snack}')

# OLD (HAY'S EXAMPLE)
# names = []
# names.append("Tinus")
# names.append("Barrie")
# names.append("Hans")
# snack1 = ""
# snack2 = None
# snack3 = 0

# index = 0
# while index < len(names):
#     name = names[index]
#     print(name)
#     name_len = len(name)
#     print(len(name))
#     print("the length of " + name)

#     if index == 0:
#         snack1 = input("What is your favourite snack?")
#     elif index == 1:
#         snack2 = input("What is your favourite snack?")
#     else:
#         snack3 = input("What is your favourite snack?")

#     index = index + 1

# new_index = 0
# for name in names:
#     if new_index == 0:
#         name1 = names[new_index]
#         print(name + " likes " + snack1)

#     if new_index == 1:
#         name2 = names[new_index]
#         print(name + " likes " + snack2)

#     if new_index == 2:
#         name3 = names[new_index]
#         print(name + " likes " + snack3)

#     new_index = new_index + 1