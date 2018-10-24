ask_currency = input("what currency? ")

def convert_euro(ask_much, ask_currency):
	if ask_currency == "dollar":
		return ask_much * 1.14590
	if ask_currency == "yen":
		return ask_much * 128.487

print(convert_euro(2, 'dollar'))

print(convert_euro(5, 'yen'))




# ask_currency = input("What currency? ")
# ask_euro = input("How much ")
# ask_euro =  float(ask_euro)

# def convert_euros(ask_euro, ask_currency):

# 	if ask_currency == "dollar":
# 		return ask_euro * 1.14590
# 	if ask_currency == "yen":
# 		return ask_euro * 128.487

# print(convert_euros(ask_euro, ask_currency))


# euro = convert_euros(1.00)
# print(convert)





# # FAHRENHEIT TO CELCIUS

# # def convert(c):
# # 	return c * 1.8 + 32

# # f = convert(-2.5)
# # print(f)



# # print(convert_euros(12, "pound"))
# # print(convert_euros(43, "yen"))
# # print(convert_euros(9.32, "dollar"))
# # print(convert_euros(5, "oreo"))


# # eur -> usd: 1.14590
# # eur -> gbp: 0.88311
# # eur -> yen: 128.487





# # def convert(temp, input_type):
# # 	if input_type == "c":
# # 		return temp * 1.8 + 32
# # 	elif input_type == "f":
# # 		return (temp - 32) * (5/9)





# # def c_to_f(c):
# # 	return c * 1.8 + 32

# # def f_to_c(f):
# # 	return (f - 32) * (5/9)

# # f = c_to_f(-2.5)
# # print(f)

# # c = f_to_c(f)
# # print(c)




# # FAHRENHEIT TO CELCIUS

# # def convert(c):
# # 	return c * 1.8 + 32

# # f = convert(-2.5)
# # print(f)