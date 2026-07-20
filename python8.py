#greet yourself

def greet(name):
    print(f"Hello {name}")
    print(f"how are you {name}")
    print("isn't the weather nice")
greet("surya")
greet("surya")

# Creating a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving a value from a dictionary
print(programming_dictionary["Function"])

# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary
empty_dictionary = {}


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#create your travell dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# print Lille
print(travel_log["France"][1])

# Nested dictionary in a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 8
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 4
   },
}

print(travel_log["Germany"]["cities_visited"][2])

