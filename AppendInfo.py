# Task 2: Write and append data to a file

# Taking input from user
data1 = input("Enter text to write into file: ")

# Writing to file
with open("output.txt", "w") as file:
    file.write(data1 + "\n")

# Appending more data
data2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(data2 + "\n")

# Reading final content
print("\nFinal content of file:")
with open("output.txt", "r") as file:
    print(file.read())