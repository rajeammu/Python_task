# #1. print numbers 1-10
def numbers(n=1):
    if n>10:
        return
    print(n)
    numbers(n+1)
numbers()
# #2. fibonacci series
# def fibonacci(n):
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     return fibonacci(n - 1) + fibonacci(n - 2)

# # Example usage:
# for i in range(10): 
#     print(fibonacci(i))
#3.sum of List
# def sum(list):
#     if not list:
#         return 0
#     return list[0] + sum(list[1:])
# numbers=[1,2,3,4,5,6,7,8,9]
# result=sum(numbers)
# print(result)
# 4. Get a input from user as number. If user entered negative number. Throw message as invalid. If user entered  0 throw factorial of 0.  
# Else it has to act as recursive factorial function.
def factorial(n):
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
try:
    user_input = int(input("Enter a number: "))
    
    if user_input < 0:
        print("Invalid input: Factorial is not defined for negative numbers.")
    elif user_input == 0:
        print("Factorial of 0 is 1.")
    else:
        result = factorial(user_input)
        print("Factorial of", user_input, "is", result)
    
except ValueError:
    print("Invalid input: Please enter a valid integer.")

