# Assignment 1

# 2. Write a python program that accepts a word from the user and reverse it

# By using while loop

str = input("Enter a word to reverse :")
print("Original string :", str)

reversed_str = ""
length = len(str)

while length > 0:
    reversed_str += str[length - 1]
    length = length - 1

print("Reversed string :", reversed_str)