# class car:
#     number_of_wheels=5
#     airbags=3
#     color="black"

# def moveforward():
#     print("car is moving forward") 
# def movebackward():
#     print("car is moving backward")
# car1 = car()

# print(car1.airbags)
# print(car1.color)
# moveforward()
# movebackward()


# car2 =car()
# car2.number_of_wheels=9
# car2.color='white'
# print(car2.number_of_wheels) 
# print(car1.number_of_wheels)
# print(car2.color)  
#example for object and class           
# class bankaccount:
#     name="arun"
#     balance=50000           
#     account_number =123478996
# def withdraw():
#     print("cash is withdraw")    
# bankaccount1=bankaccount()
# bankaccount1.name='raghul'
# print(bankaccount1.name)
# print(bankaccount1.balance)
# withdraw()

# bankaccount2=bankaccount()
# bankaccount2.account_number=123456
# print(bankaccount2.account_number)
# print(bankaccount2.name)

#example of object and  class with constructor
# class dog:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         print(self.name,"dog is barking") 
#     def get_age(self):
#         print("the age is",self.age)
# dog1=dog("landu",5)
# print(dog1.name)
# dog1.get_age()
# dog1.bark()
#example for inheritance
#single inheritance
# class dad():
#     def phone(self):
#      print("dads phone")    
# class son(dad):
#     def laptop(self):
#         print("sons laptop")  
# arun=son()
# arun.laptop() 
# arun.phone()  
#multiple inheritance 
# class dad():
#     def phone(self):
#      print("dads phone")
# class mom():
#     def sweet(self):
#      print("moms sweet")     
# class son(dad,mom):
#     def laptop(self):
#         print("sons laptop")  
# arun=son()
# arun.laptop() 
# arun.phone()  
# arun.sweet() 
# Multilevel inheritance
# class grandpa():
#     def phone(self):
#         print("grandpas phone")
# class dad(grandpa):
#     def money(self):
#         print("dads money")
# class son(dad):
#     def laptop(self):
#         print("sons laptop")
# arun=son()
# arun.laptop()
# arun.money()
# arun.phone() 

# ram=dad()
# ram.phone() 

# heierachial inheritance
# class dad():
#     def money(self):
#         print("dads money")
# class son1(dad):
#     pass
# class son2(dad): 
#     pass
# class son3(dad):
#     pass
# ram =son3()
# ram.money()

# encapsulation in python
# public method
# class dog:
#     def __init__(self,name):
#         self.name=name
#     def bark(self):  # public method
#         print("dog is barking")
# landu=dog("buddy")
# print(landu.name)
# landu.bark() 
# protected method  
# class animal:
#     def __init__(self,name):
#         self._name=name # protected attribute
#     def sound(self): # protected method
#         print("some sound") 
# class cat(animal):
#     def meow(self):                
#         print(self._name,"sound is meow")
# Cat=cat("zappi")
# print(Cat._name)
# Cat.meow()  
# Cat.sound()
#private method

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):  # Public method to access the private attribute
#         return self.__balance

# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # Accessible
# polymorphism-method overriding will override the previous method 
# class animal:
#     def sound(self):
#         print("It gives sound ")
# class dog(animal):         
#     def sound(self):
#         print("the sound is meow")       
# d1=dog() 
# d1.sound()   
# data abstraction
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Derived Class for Car
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

# Derived Class for Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started!")

# Using the classes
car = Car()
motorcycle = Motorcycle()

car.start_engine() # Output: Car engine started!
motorcycle.start_engine()  # Output: Motorcycle engine started!
    


           
        
       

                      
       
        
               
        



    
        