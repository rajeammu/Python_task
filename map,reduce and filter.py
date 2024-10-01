import functools 

# # 1.Square all numbers in a list
# numbers=[1,3,5,7,9]
# square=list(map(lambda x:x**2,numbers))
# print("the squared numbers is ",square)
# 2.Convert all strings in a list to uppercase  
# Str =["hai","hello","place"] 
# uppercase=list(map(lambda x:x.upper(),Str))
# print("string in a list to uppercase is ",uppercase)
# 3.Add 10 to each number in a list
# number=[1,2,3,4,5]
# num=list(map(lambda a:a *10, number))
# print(num)
# 4.Double each number in a list
# 5.Capitalize the first letter of each string in a list
# string=["hai","hello","welcome","place"]
# str=list(map(lambda a:a.capitalize(),string))
# print(str)
# FILTER METHOD
# 6.Filter out even numbers from a list
# number=[1,2,3,4,5,6,8,90]
# even=list(filter(lambda a:a%2==0,number))
# print(even)
# # 7.Filter out words shorter than 4 characters
# string=["hi","hello","ram","lie","welcome"]
# words=list(filter(lambda a:len(a) <4,string))
# print(words)
# 8.Filter out numbers greater than 10
# number=[12,23,45,5,6,7,56,11,2]
# greater=list(filter(lambda a:a>10,number))
# print(greater)
# 9.Filter out strings containing the letter 'a'
# string=["hai","hello","ram","lie","raje"]
# result=list(filter(lambda x:"a" in x,string))
# print(result)
# 10. Filter out numbers that are not divisible by 3
# number=[2,4,3,6,9,12,7,5]
# result =list(filter(lambda a:a%3 !=0,number ))
# print(result)
# 11.Filter out negative numbers from a list
# str =[1,-2,3,-4,5,-6,7-9,]
# number=list(filter(lambda a: a<0 ,str))
# print(number)
#REDUCE
#11. Find the product of all numbers in a list
# from functools import reduce
# number=[2,3,4]
# result=reduce(lambda a,b:a*b,number)
# print(result)
#12.Compute the factorial of a number using reduce 
# from functools import reduce

# Function to compute factorial using reduce
def factorial(n):
    if n < 0:
        return "Invalid input"  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1  # Factorial of 0 and 1 is 1
    else:
        return functools.reduce(lambda x, y: x * y, range(1, n + 1))

# Example usage
number = int(input("enter a number: "))
result = factorial(number)

# Output the result
print("Factorial of", number, "is", result)  # Output: Factorial of 5 is 120


