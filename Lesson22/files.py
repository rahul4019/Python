import os
# r = Read
# a = Append
# w = Write
# x = create

# Read - error if it doesn't exist

# file = open("names.txt", "r")
file = open("names.txt")

# print(file.read()) # reads the file

# print(file.read(5)) # reads only 5 characters

# print(file.readline())  # reads the first line
# print(file.readline()) # reads the first line
# print(file.readline()) # reads the first line
# print(file.readline()) # reads the first line

for line in file:
    print(line)

file.close()  # always close the file you open

try:
    # file = open("name_list.txt")
    file = open("names.txt")
    print(file.read())
except:
    print("The file you want to read doesn't exist.")
finally:
    file.close()

# Append - creates the file if it doesn't exist

file = open('names.txt', "a")  # append
file.write("Karan")
file.close()


file = open('names.txt')  # read
print(file.read())
file.close()

# Write (overwrite)

file = open("context.txt", "w")
file.write("I deleted all of the context")
file.close()

file = open("context.txt")
print(file.read())
file.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
file = open("names_list.txt", "w")
file.close()

# Creates the specified file, but returns an error if the file already exists.
if not os.path.exists("rahul.txt"):
    f = open("rahul.txt", "x")
    f.close()

# Delete a file
    
# avoid  an error if it does not exist
if os.path.exists("rahul.txt"):
    os.remove("rahul.txt")
else:
    print("The file you wish to delete, does not exist.")

with open("more_names.txt") as file:
    content = file.read()

with open("names.txt","w") as file:
    file.write(content)
    

