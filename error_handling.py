#compile time error
# print("hello")
# print("hello")
# printt("hello") #syntax error
#logical error
# a=10
# b=20
# print(a+a) #logical error
#runtime error
# a=int(input("enter a value1: ")) #1
# b=int(input("enter a value2: ")) #hi
# print(a+b) 
# try,except block
# try:
#     # a=int(input("enter a number:"))
#     # b=int(input("enter a number:"))
#     a=input("enter a number:")
#     b=input("enter a number:")
#     print(a/b)
# except Exception as e:
#     print("something",e)
# finally:
#     print("done") 
# user defined exception
# class invaliddata(Exception):
#     pass
# marks=int(input("Enter a number: "))
# try:
#     if marks<0 or marks>100:
#         raise invaliddata
# except invaliddata:
#     print("Marks should be between 0 and 100") 
# error/exception handling task python
# 1.Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle 
# the exception if the user inputs zero
 
# try:
# number=int(input("Enter a number: ")) 
#    if  number==0:
#        raise ValueError("cannot reciprocal zero")
#    reciprocal = 1/number
#    print("the reciprocal of number: ",reciprocal)
# except ValueError as e:
#     print(e)   
# 2.Modify the above program to also handle the exception if the user inputs a non-numeric value  

# try:
      # number=int(input("enter a number: "))
#     if number==0:
#         raise ValueError("cannot reciprocal zero")
#     reciprocal =1/number
#     print("the reciprocal of number: ",reciprocal)
# except ValueError as e:
#     print(e)
# except Exception:
#     print("Invalid input.Please enter a numeric value")        
# 3.Write a program that reads a number from the user and prints its square. Use the else clause to print a success 
# message 
# try:
#  number=int(input("enter a number: "))
#  square =number **2
#  print("the square of number is ",square)
# except ValueError:
#  print("invalid input.Enter a numeric value")
# else:
#     print("completed successfully") 
# 4.Modify the program in Task 3 to include a finally clause that prints a message regardless of whether an 
# exception occurred or not
# try:
#     number=int(input("enter a number: "))
#     square =number **2
#     print("the square of number is ",square)
# except ValueError:
#  print("invalid input.Enter a numeric value")
# finally:
#     print("completed successfully") 
# 5.Write a function that raises a ValueError if the input number is negative 
# def check_non_negative(number):
#     if number < 0:
#         raise ValueError("Input is a non-negative number.")
# try:
#     input = int(input("Enter a number: "))  # Read user input
#     check_non_negative(input)                   # Check if the number is non-negative
#     print("The input is valid.")
# except ValueError as e:
#     print(e)
# 6.Write a program that repeatedly asks the user for a number and handles exceptions. 
# The program should continue asking until a valid number is entered
# while True:
#     try:
#         # Ask the user for a number
#         number = float(input("Please enter a number: "))
#         print("entered the number:", number)
#         break  # Exit the loop if the input is valid

#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")

# print("Thank you for providing a valid number!")

          
     

     
                 