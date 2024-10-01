# 1.In a list of array store even and odd numbers in new list and print
# list=[1,2,3,4,5,6,7,8,9,10]
# # Lists to store even and odd numbers
# even_numbers=[]
# odd_numbers=[]
# for number in list:
#     if number %2==0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number) 
# print("the even number is",even_numbers)
# print("the odd number is",odd_numbers)           
# # 2.print sum of list
# list1=[1,5,7,6,7,9,3,2]
# total=sum(list1)
# print(total)
# 3.Product of list when zero in list it can't product that number
# list=[0,2,3,4,5,0,6,7,8,9]
# # Initialize the product
# product=1
# for number in list:
#     if number!=0:
#         product*=number
# print("the product is",product)
#4.find duplicate element in a array and print in new array 
# array =[1,2,3,4,5,6,6,7,8,9,1,2,3,9]
# Lists to track seen elements and duplicates
# seen=[]
# duplicates=[]
# for number in array:
#     if number in seen:
#         if number not in duplicates:
#             duplicates.append(number)  #add to duplicate list
#     else:
#         seen.append(number) #add to seen list
# print("the duplicate number is ",duplicates)               
# 5.largest & smallest number in a list
# list=[2,6,7,4,9,5,90,37]
# largest=max(list)
# smallest=min(list)
# print(largest)
# print(smallest)
# # 6.reverse a list.
# list=[2,6,7,4,9,5,90,37]
# list.reverse()
# print("the reverse number is ",list)
#Tuple Task 
# 1.add a new elements in tuple without using list constructor. I/P = (1,2,3,4,5)  O/P =(1,2,3,4,5,6,7,8,9,10).
# tuple1=(1,2,3,4,5)
# tuple2=(6,7,8,9,10)
# tuple=tuple1+tuple2
# print(tuple)
# 2.add a new elements in tuple without using list constructor . I/P =(“python”,”C”,”C++”) O/P = (“python”,”C”,”C++”,”java”,”java script”,”node js”).
# tuple1=("python", "C" ,"C++")
# tuple2=("java","java script","node js")     
# tuple=tuple1+tuple2
# print(tuple)
#Dictionary
# 1.Get a input from user as string, count character of string and output will be dictionary.
# string=input("enter a string: ")
# count={}
# for char in string:
#     if char in count:
#         count[char]+=1 # Increment count if character already in dictionary
#     else:
#         count[char]=1 # Initialize count if character not in dictionary
# print("the character count: ",count) 

  
