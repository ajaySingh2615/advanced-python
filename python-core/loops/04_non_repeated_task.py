# Given a string, find the non - repeated characters

name = "mike eleven"

for char in name:
    if name.count(char) == 1:
        print("char is: ", char)
        break

