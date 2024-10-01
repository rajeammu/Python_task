import random
#python syntax
# print("hello world!")
# identation in python
# if 5 > 1:
#     print("5 is greater")
# # variables in python   
#     x = 5
#     y= "raje"
#     print(x)
# #specify the datatype of a variable using casting
#     a = str(8)
#     b = int(9)
#     c = float(10)
#     print(a)
#     print(b)
#     print(c)
# print(10 & 20)

# python input and output 
# name=input("Hello, Welcome")
# print(name)
#Implicit type conversion 
# x=9.0
# y=2
# z=x+y
# print(z)
# #Explicit type conversion
# x=5
# y=float(x)
# print(y)
# a=True
# b=False
# c=False
# d=True
# print(c)
# print(d)
# print(not a)
# print(not b)
# print(not c)
# print(not d)
# print(a and b)
# print(c and d)
# print(a or b)
# print(c or d)
# print(a and b or c)
# print(not(a and b and c))
# print(not a and not b and not c)
#if conditional statement
# a=6
# b=4
# if a>b:
#  print('a is greater')
# #elif conditional statement
# if a<b :
#  print("a is smaller")
# elif a>b:
#     print("a is larger")
# #else conditional statement
# if a>b:
#     print("a is greater")
# elif a<b:
#     print("b is smaller")
# else:
#     print("both are equal")        
# nested if.. else
# age =60

# # Determine the age group and senior discount eligibility
# if age >= 18:
#     if age >= 60:
#         print(f"At age {age}, you are a senior citizen and eligible for a senior discount.")
#     else:
#         print(f"At age {age}, you are an adult but not eligible for a senior discount.")
# else:
#     print(f"At age {age}, you are a minor.")
# #match case
# street =1
# match street: 
#     case 1:
#         print("street 1")
#     case 2:
#         print("street 2")
#     case 3:
#         print("street 3")
#     case _:
#         print("street is not present")
#For loop in python 

# Iterate over the string
# text ="input" 
# for char in text:
#     print(char)  
# # Iterate over the list
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# # Iterate over the range
# for i in range(9):
#     print(i) 
# # Initialize a variable
# count = 0
# # While loop with a condition
# while count < 5:
#     print(count)
#     count += 1  # Increment the count

# print("Loop has ended.")
# #break statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# String Manipulation
# string ="hello world"
# print(string)
# # length of the string
# substring=len(string)
# print(substring)
# # string slicing
# sub=string[1:7]
# print(sub)
# print(string[3])
# #list,tuple,set,dictionaries
# a={1,2,3,4,7,5,8,90,89,67,56}
# b={4,5,2,7,8}
# # a.add(9)
# # a.update([2,3,5])
# set_union=a.union(b)
# set_union=a.intersection(b)
# set_union=a.difference(b)
# a.remove(90)
# print(a)
# print(set_union)
# modules

# import random   
# # fruits = ['apple', 'banana', 'cherry']
# # print(random.choice(fruits))  # Output: A random fruit
# print(random.uniform(1, 10))  # Output: A random float between 1 and 10

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# print(p.x, p.y)  # Output: 10 20
# main.py
# read the file 
# f=open("file_handling.txt","r")
# print(f.read())
# f.close()
# write the file 
# f=open("file_handling.txt","w")
# f.write("apple\n")
# f.writelines(["line1\n", "line2\n"])
# f.close()   
# read & write the file 
# f=open("file_handling.txt","r+")
# print(f.read())
# f.write("pine\n")
# f.close()                                         
#write  & read the file 
# f=open("file_handling.txt","w+")
# f.write("all\n, welcome\n")
# f.seek(0)
# print(f.read())
# f.close()
#to remove the text file
# import os
# os.remove("file_handling.txt")
#using with statement 
# Step 1: Create the file_handling file and write content to it
# f = open("file.txt","x") - to create the new text file 
# with open('file_handling.txt', 'w') as file:
#     file.write("Hello, World!\n")
#     file.write("This is the content of the source file.\n")
 

# # Step 2: Create the file_handling1 file and copy content from the source file using a for loop
# with open('file_handling.txt', 'r') as file:  # Open the source file in read mode
#     with open('file_handling1.txt', 'w') as destination:  # Open the destination file in write mode
#         for line in file:  # Iterate over each line in the source file
#             destination.write(line)  # Write the line to the destination file

# # Step 3: Verify by reading the content of the file_handling1 file
# with open('file_handling1.txt', 'r') as destination:
#     copied_content = destination.read()
#     print(copied_content)

    

     