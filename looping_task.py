# Print numbers 1 to 10
# for loop:
# for i in range (1,11):
#     print(i)
    
# # while loop
# i =1
# while i <10:
#     print(i)
#     i+=1 
   
#Print the square of each number from 1 to 10
# for loop
# for i in range (1,11):
#     square=i ** 2
#     print(square)
#     print("the square of ",i, "is" ,square) 
# while loop
# i = 1
# while i <= 10:
#square = i ** 2
#print(f"The square of {i} is {square}")
# i += 1
# Print each character in a string
# for loop  
# var= "hello world"
# for j in var:
#     print(j)
# while loop 
# var="hello world"
# index = 0
# while index < len(var):
#     print(var[index])
#     index += 1
# Sum of numbers from 1 to 10 
#for loop
# total=0
# for i in range(1, 11):
#     total += i
# print(total)
# while loop
# total=0
# i=1
# while i<=10:
#     total += i
#     i+=1
# print(total)
#Print each element in a list 
#for loop  
# element =[1,2,3,4,5,6,7,8,9,10]
# for x in element:
#     print(x) 
#while loop 
# element =[1,2,3,4,5,6,7,8,9,10]
# index = 0
# while index < len(element):
#     print(element[index])  
#     index += 1 
#Print numbers from 10 to 1
#for loop
# for k in range(10,0,-1):
#     print(k)
#while loop  
#Print only even numbers from 10 to 20
#for loop  
# for j in range(10,21,2): 
#     print(j)  
# for k in range(10,21):
#     if k%2 == 0:
#       print(k)
#while loop
# j=10
# while j<=20:
#     print(j)
#     j+=2
#Print the multiples of 5 between 20 to 50
# for loop
# for i in range(20,51):
#     if i%5 ==0:
#         print(i)
#while loop
# Initialize the starting value
# i = 20
# while i <= 50:
#     if i % 5 == 0:
#         print(i)
#     i += 1

#Print numbers from a list that are greater than 10 
#for loop
# list =[12,9,8,3,90,6,2,90,100,56]
# for i in list:
#     if i >10:
#         print(i)
#while loop
# Define the list of elements
# numbers = [12, 9, 8, 3, 90, 6, 2, 90, 100, 56]
# index = 0
# while index < len(numbers):
#     if numbers[index] > 10:
#         print(numbers[index])
#     index += 1

#Print all prime numbers between 10 and 20
# for num in range(10, 21):
#     is_prime = True  # Assume the number is prime
#     if num > 1:  # Check only numbers greater than 1
#         for i in range(2, num):  # Check all numbers less than num
#             if num % i == 0:  # If num is divisible by i
#                 is_prime = False  # It's not prime
#         if is_prime:  # If it is still considered prime
#             print(num)  # Print the prime number

#while loop
# num = 10  # Start at 10
# while num <= 20:  # Loop until num is greater than 20
#     is_prime = True  # Assume the number is prime
#     if num > 1:  # Check only numbers greater than 1
#         i = 2  # Start checking for factors from 2
#         while i < num:  # Check all numbers less than num
#             if num % i == 0:  # If num is divisible by i
#                 is_prime = False  # It's not prime
#             i += 1  # Move to the next potential factor
#     if is_prime:  # If it is still considered prime
#         print(num)  # Print the prime number
#     num += 1  # Move to the next number

#Find the largest number in a list
# numbers=[1,5,6,8,9,4,78]
# largest=numbers[0]
# for num in numbers:
#     if num > largest:
#         largest=num
#         print("the largest number is: ",largest)
# while loop
# numbers = [12, 5, 8, 20, 15, 30, 25]
# largest = numbers[0]
# index = 1
# while index < len(numbers):
#     number = numbers[index]
#     if number > largest:
#         largest = number
#     index += 1 
# Print the largest number found
# print("The largest number is:", largest)
        
#Count the number of vowels in a string 
# for loop
# string ="Welcome All"
# for i in string:
#     if i=="a"or i=="e" or i=="o"or i=="u"or i=="i"or i=="A" or i=="E"or i=="O"or i=="U"or i=="I":
#         print(i)
#while loop
# Define the string
# string = "Welcome All"
# index = 0
# vowels = "aeiouAEIOU"
# while index < len(string):
#     if string[index] in vowels:
#         print(string[index]) 
#     index += 1 
        
#Print product of 1 to 5
# for loop
# product=1
# for i in range(1,6):
#     product*=i
# print(product)
# while Loop
# product = 1
# i = 1
# while i <= 5:
#     product *= i
#     i += 1
# print(product)

#Get a input from user like number until user enter zero after that have to print the product of numbers 
#for loop
# product = 1
# # Use a large range to simulate an indefinite loop
# for _ in range(10000):
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     product *= number
# print("The product of the numbers is:", product)
#while loop   
# product = 1
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break  
#     product *= number
# print("The product of the numbers is:", product)
#Get a input from user like number until user enter negative number after that have to print the sum of numbers.
# for loop
# sum = 0
# for _ in range(10000):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         break 
#     sum += number
# print("The sum of the numbers is:",sum)
#while loop
# sum = 0
# while True:
#     number = int(input("Enter a number : "))
#     if number < 0:
#         break
#     sum += number
# print("The sum of the numbers is:", sum)


     
              