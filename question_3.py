# Assignment - 1

# 3. Write a Python program to count the number of even and odd numbers from a series of numbers

# By using For Loop

size = int(input("Enter size of the list :"))

lst = []

for i in range(size):
    element = int(input("Enter the element :"))
    lst.append(element)
print(lst)

even_num = 0
odd_num = 0

for i in lst:
    if i % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

print("Number of Even Numbers :", even_num)
print("Number of Odd Numbers :", odd_num)