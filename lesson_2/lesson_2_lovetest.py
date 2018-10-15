print("Welcome to the Love Test!")

my_name = input("What is your name? ")
lovers_name = input("What is your lovers name? ")

my_name_lower_strip = my_name.lower().strip()
lovers_name_lower_strip = lovers_name.lower().strip()

all_names = my_name_lower_strip + lovers_name_lower_strip 

names_len = len(all_names)

if names_len == 11:
	print("This is a 90% match!")
elif names_len == 17:
	print("This is a 100% perfect match!")
elif names_len >=17:
	print("You fit perfect together. You should marry... over 2-5 years.")
elif names_len <= 5:
	print("You can find better..")
else:
	print("Search for someone else.")



