#
print("hello" + input("what is your name?"))
print(len(input("what is your name?")))
#
print(type("xyz"))
print(type(9876))
print(type(3.14))

print(int("123") + int("456"))
#
print("My age: " + str(20))
print(6*7+18/6-5+9)
#
score = 97
height = 5.5
print(f"your score is {score}, your height is {height}")
# tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
print(f"each person should pay: ${bill_per_person}")
