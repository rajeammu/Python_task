# #1.Calculate Square
# def square(num):
#     return num **2
# res=square(15)
# print(res)
# #2. calculate the area of a rectangle
# def rectangle(length,breadth):
#     return length*breadth
# area=rectangle(5,9)
# print(area)
# # 3.Check Even or Odd
# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# # number=int(input("Enter a number: "))    
# result=odd_even(8)
# print(result) 
# #4.Calculate Factorial  
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num * factorial(num-1)
# result=factorial(9)
# print(result)
# 5.Check Prime Number    
# 6. Reverse a string
# def reverse(string):
#     rev=""
#     for char in string:
#         rev=char +rev
#     return rev
# reverse=reverse("Welcome to All")  
# print(reverse)  
#7.Count Characters
# def character(char):
#     count={}
#     for chars in char:
#         if chars in count:
#             count[chars]+=1
#         else:
#             count[chars]=1
#     return count    
# result=character("enter a string value")            
# print(result)
# # 8.Sum of Squares  
# def square(number):
#     total=0
#     for num in number:
#         total+=num**2
#     return total
# number=[1,2,3,4,5,6]
# result=square(number)
# print(result) 
# 9.Check Palindrome
# def is_palindrome(s):
#     # Initialize the length of the string
#     length = len(s)
#     for i in range(length // 2):
#         # Compare characters from start and end
#         if s[i] != s[length - 1 - i]:
#             return False  # Not a palindrome if mismatch found
#     return True  # It's a palindrome if no mismatches found
# string = input("enter a value: ")
# result = is_palindrome(string)
# print(result)
# 10.Calculate Fibonacci 
# def fibonacci(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b  # Update values
#     return fib_sequence
# n = 10
# result = fibonacci(n)
# print(" Fibonacci numbers are: ",result) 
# 11.Check Armstrong Number
# def is_armstrong_number(num):
#     # Convert the number to a string to easily iterate over digits
#     digits = str(num)
#     power = len(digits)  # Number of digits
#     total = sum(int(digit) ** power for digit in digits)  # Sum of digits raised to the power of the number of digits
#     return total == num  # Check if the total equals the original number
# number = 153
# result = is_armstrong_number(number)
# print(f"the armstrong number",result) 
# 12.Check Leap Year
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # It's a leap year
            else:
                return False  # It's not a leap year
        else:
            return True  # It's a leap year
    else:
        return False  # It's not a leap year

year = 2024
result = is_leap_year(year)
print("The year" +" is " + ("a leap year" if result else "not a leap year.") + ".")


  

                        
    
