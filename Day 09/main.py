dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(dict["Bug"])

# Adding new items to a dictionary.
dict ["Loop"] = "The action of doing something over and over again."
print(dict)

# Creating an empty dictionary
empty_dict = {}

# Wiping an existing dictionary
# dict = {}
# print(dict)

# Editing an item in a dictionary
dict["Bug"] = "A moth in your computer."
print(dict)

# Looping through a dictionary
for key in dict:
    print(key)
    print(dict[key])
