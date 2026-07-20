#creating files with python 

file = open("Surya_file.txt")
contents = file.read()
print(contents)
file.close()
#if we dont want to close the file maanually
with open("Surya_file.txt") as file:
    file = open("Surya_file.txt")
    contents = file.read()
    print(contents)
#for writting(it will delete the previous contents)
with open("Surya_file.txt", mode="w") as file:
    file.write("new Text.")
    print(file)
#for adding text without deleting the previous ones
with open("Surya_file.txt", mode="a") as file:
    file.write("\nHello my name is Surya.")
    print(file)
#creating files
with open("Surya2_file.txt", mode="w") as file:
    file.write("Hello my name is Surya.")