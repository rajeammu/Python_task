# 1. Print numbers from 1 to 10, but stop when the number is 5.
# for i in range(1,11):
#     if i==5:
#          break
#     print(i)
#2. Find the first negative number in a list.
# list=[2,7,8,-2,4,-9]
# for i in list:
#     if i<0 :
#         print(i)
#         break
# 3.Iterate over a list and stop if you encounter a zero.
# list=[1,9,80,0,9,7,6] 
# for i in list:
#     if i==0:
#         break
#     print(i)
# 4. Print numbers from 1 to 10, skipping 5 
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i) 
# 5. Print only even numbers from 1 to 10.
# for i in range(1,11):
#     if i%2==0:
#         print(i)
# 6.Iterate over a list and skip negative numbers.
# list=[3,-9,8,-5,6,2,-1,9]
# for i in list:
#     if i < 0:
#          continue
#     print(i)
# # 7.Print characters of a string, skipping vowels. 
# string ="Class in Ocean Academy"
# vowel ="aeoiuAEIOU"
# for i in string:
#     if  i in vowel:
#         continue
#     print(i, end=" ") #print thr character without a newline
# 8.Iterate over numbers from 1 to 20, but skip multiples of 3. 
# for i in range(1,21):
#     if i % 3 ==0:
#         continue
#     print(i)
# # 9. Iterate over a list and use pass for future implementation.
# list =[1,2,3,8,9,6,4,7]
# for i in list:
#     if i %2==0:  # Placeholder for future implementation
#         pass
#     else:
#         print(i,end=" ")  
#10. Iterate over numbers from 1 to 10, skip 5 and stop at 8. 
# for i in range(1,11):
#     if i==5:
#         continue
#     if i==8:
#         break
#     print(i)              
# 11.Print only odd numbers from 1 to 10, but use pass for even numbers.
# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i) 
# 12.Iterate over a list, skip negatives, print positives, stop at zero.
# list =[2,-7,9,8,-1,3,-4,0,6,-3,3] 
# for i in list:
#     if i<0:
#         continue
#     elif i == 0:
#         break
   
#     else:                
#         print(i) 
# # 13.Skip the first half of a list, process the second half, use pass for future.  
        
# list =[2,9,3,8,4,7,5,7] 
# midpoint = len(list) / 2
# for item in list:
#     if list.index(item) < midpoint:
#         pass  # Skip the first half; placeholder for future implementation
#     else:
#         # Future processing logic can go here
#         pass  # Placeholder for future implementation
#         print(item)  # For now, just print the item
# 14.Get a input from user like number until user enter zero after that have to print the product of numbers.
# product = 1
# Use a large range to simulate an indefinite loop
# for _ in range(10000):
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     product *= number
# print("The product of the numbers is:", product)      
#15. Get a input from user like number until user enter negative number after that have to print the sum of numbers.
# sum = 0
# for _ in range(10000):
#     number = int(input("Enter a number: "))
#     if number < 0:
#         break 
#     sum += number
# print("The sum of the numbers is:",sum)   

