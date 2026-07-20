# checking if a number is even or odd
number_to_check = int(input("what is your number?\n"))

if number_to_check % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")
# welcome to the rollercoster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 100:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 6.99
        print("Please pay $6.99.")
    elif age <= 18:
        bill = 9.99
        print("Please pay $9.99.")
    else:
        bill = 15.99
        print("Please pay $15.99.")

    wants_photo = input("do you want a photo take? Type y for yes and n for no")
    if wants_photo == "y":
        bill += 5.99
    print(f"your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

# welcome to our pizza shop

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 13.99
elif size == "M":
    bill += 18.99
elif size == "L":
    bill += 22.99
else:
    print("you typed the wrong input")
if pepperoni == "Y":
    if size == "S":
        bill += 1.99
    else:
        bill += 2.99
if extra_cheese == "Y":
    bill += 0.99

print(f"your final bill is {bill}.")