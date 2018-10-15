# asking the user for a sentence, counts the length of their answer 
sentence = input("What do you want to tell me? ")
sentence_len = len(sentence)
start = round(sentence_len * 0.25)
end = round(sentence_len + 0.75)
sentence_new = sentence[start:end]

# printing the new string (0.25% and 0,75% of the users sentence)
print(sentence_new)

# this splits the sentence into a list and counts the length
words_list = sentence.split(" ")
words_len = len(words_list)
start = round(words_len * 0.25)
end = round(words_len * 0.75)
new_list = words_list[start:end]

# this converts the list back to a string using join and prints it
print(" ".join(new_list))