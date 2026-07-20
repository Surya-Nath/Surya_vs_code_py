#let's do more practice
fruits = ["banana", "mango", "cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits[-2])

fruits[1] = "orange"
print(fruits)

fruits.append("orange")
print(fruits)

fruits.extend(["apple", "banana", "cherry"])
print(fruits)

#check who will give the bill

import random
friends = ["Alice", "oggy", "Jack", "David", "Surya"]
print(random.choice(friends) + " will give the bill")