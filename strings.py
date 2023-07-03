# Using print()

# print("Hello, World")
# print("Hello, World", "Goodnight, Moon")
# print("Hello World", "Goodnight Moon", "Welcome to Mars", sep=", ")
# print("Hello World", "Goodnight Moon", "Welcome to Mars", sep=", ", end="!!!!!!!!!!")
# print("Hello World", "Goodnight Moon", "Welcome to Mars", sep=", ", end="!!!!!!!!!!\n")


# len(): Returns the length (number of characters) of a string.
# print(len("Hello, World"))

# lower(): Converts all characters in a string to lowercase.
# print("We are the Knights that say 'Ni'!".lower())

# upper(): Converts all characters in a string to uppercase.
# print("We are the Knights that say 'Ni'!".upper())

# capitalize(): Converts the first character of a string to an uppercase letter and all other alphabets to lowercase.
# sentence = "we are the knights that say 'Ni!'"
# print(sentence.capitalize())

# title(): Returns a string with first letter of each word capitalized; a title cased string.
# print(sentence.title())
# problem with words with apostrophes - you need to write a separate function using regex to solve

# strip(): Removes leading and trailing whitespace characters from a string.
# print("         We are the Knights that say 'Ni'!              ".strip())

# split(): Splits a string into a list of substrings based on a delimiter (default delimiter is a space).
# names = "King Arthur, Sir Galahad, Sir Lancelot, Patsy"
# print(names.split(":"))
# print("\n")
# print(names.split(","))
# print("\n")
# print(names.split(", "))
# print("\n")
# print(names.split(", ", 2))
# print("\n")

# join(): Joins a list of strings into a single string using a specified delimiter.
# print(", ".join(['King Arthur', 'Sir Galahad', 'Sir Lancelot', 'Patsy']))
# print("\n")

# replace(): Replaces occurrences of a specified substring with another substring.
# print("Trojan Horse".replace("Horse", "Rabbit"))
# print("\n")
# print("Trojan Horse".replace("horse", "Rabbit")) # is it case sensitive?
# print("\n")

# knights = "We are now the knights who say ekki-ekki-ekki-ekki-ptang zoom-boing z'nourrwringmm!"
# print(knights.replace("ekki", "icky", 2))
# print("\n")

# startswith(): Checks if a string starts with a specified substring.
# greeting = "Welcome to Camelot!"

# print(greeting.startswith("Welcome"))
# print("\n")

# print(greeting.startswith("Welcome", 0, 5))
# print("\n")

# print(greeting.startswith("Camelot", 11))
# print("\n")


# endswith(): Checks if a string ends with a specified substring.
# greeting = "Welcome to Camelot!"

# print(greeting.endswith("Camelot"))
# print("\n")

# print(greeting.endswith("Camelot!"))
# print("\n")

# print(greeting.endswith("Camelot!", 11))
# print("\n")

# print(greeting.endswith("Camelot!", 11, 15))
# print("\n")

# find(): Searches for a substring within a string and returns the index of the first occurrence (or -1 if not found).
# demand = "We want...a shubbery!"

# print(demand.find("want")) # what if the substring is "Want"?

# count(): Counts the number of occurrences of a substring within a string.
# knights = "We are now the knights who say ekki-ekki-ekki-ekki-ptang zoom-boing z'nourrwringmm!"
# print("\n")
# print(knights.count("ekki"))


# isdigit(): Checks if all characters in a string are digits.
# number = "12345"
# print("\n")
# print(number.isdigit())

# number = "12three45"
# print("\n")
# print(number.isdigit())

# isalpha(): Checks if all characters in a string are alphabetic.
# letters = "abcdef"
# print("\n")
# print(letters.isalpha())

# letters = "ab3def"
# print("\n")
# print(letters.isalpha())

# islower(): Checks if all characters in a string are lowercase.
# name = "robin"
# print("\n")
# print(name.islower())

# name = "Robin"
# print("\n")
# print(name.islower())

# isupper(): Checks if all characters in a string are uppercase.
# name = "ROBIN"
# print("\n")
# print(name.isupper())

# name = "Robin"
# print("\n")
# print(name.isupper())

# String concatenation using the + operator
# quality = "Brave"
# title = "Sir"
# name = "Robin"
# greeting = quality + " " + title + " " + name
# print(greeting)
# print("\n")

# Using the += operator
# greeting = ""
# quality = "Brave"
# title = "Sir"
# name = "Robin"
# greeting += quality + " "
# greeting += title + " "
# greeting += name
# print(greeting)

# String interpolation
# Current standard way:
name = "John"
age = 30

# Using f-string
# message = f"My name is {name} and I'm {age} years old.\n"
# print(message)

# # Left alignment
# message = f"Name: {name:<10} Age: {age:<5}\n"
# print(message)
# # Right alignment
# message = f"Name: {name:>10} Age: {age:>5}\n"
# print(message)
# # Center alignment
# message = f"Name: {name:^10} Age: {age:^5}\n"
# print(message)

# # Using .format()
# name = "John"
# age = 30

# message = "My name is {} and I'm {} years old.".format(name, age)
# print(message) 

# # Using positional arguments (0 and 1 are indices)
# name = "John"
# age = 30

# message = "My name is {0} and I'm {1} years old.\n".format(name, age)
# print(message)

# message = "My name is {1} and I'm {0} years old.\n".format(name, age)
# print(message)

# # Keyword arguments

#note the use of a multiline comment here!

"""
You can use keyword arguments to specify values for placeholders based on their names. 
This allows you to provide values in any order and improves readability.
"""

# name = "John"
# age = 30

# message = "My name is {name} and I'm {age} years old.".format(name=name, age=age)
# print(message)

# # Left alignment
# message = "Name: {:<10} Age: {:<5}".format(name, age)
# print(message)  # Output: Name: John       Age: 30

# # Right alignment
# message = "Name: {:>10} Age: {:>5}".format(name, age)
# print(message)  # Output: Name:       John Age:   30

# # Center alignment
# message = "Name: {:^10} Age: {:^5}".format(name, age)
# print(message)  # Output: Name:   John    Age:  30


# # Indexing and Slicing
message = "Hello, World!"

# Accessing individual characters
print(message[0]) 
print(message[7])
print("\n")

# Slicing to extract subsequences
print(message[0:5])
print(message[7:12])
print("\n")

# Negative indexing
print(message[-1])
print(message[-6])
print("\n")

# Omitting start or end indices
print(message[:5])
print(message[7:])
print("\n")






