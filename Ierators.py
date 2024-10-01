# Iterators
# list=["apple","banana","orange","mango","lemon"]
# mylist=iter(list)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# Looping Through an Iterator
# list=["apple","banana","orange","mango","lemon"]
# for x in list:
#     print(x)
# # iterator methods in class and object
# class number:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a +=1
#         return x
# my_numbers=number()
# myiter=iter(my_numbers)
# print(next(myiter)) 
# print(next(myiter))       
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#stop iteration 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 50:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
