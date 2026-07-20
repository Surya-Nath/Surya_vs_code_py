student_scores = [150, 132, 95, 140, 56, 78, 56, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_scores = sum(student_scores)
print(total_scores)
#now check max score
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#make your own function

def my_function():
    print("Hi")
    print("Surya")


my_function()