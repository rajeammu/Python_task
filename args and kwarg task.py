# 1: Sum of all arguments
#args
# def sum_all(*args):
#     return sum(args)
# result=sum_all(1,2,3,4,5,6,7)
# print(result)
#kwargs
# def sum_all(**kwargs):
#     return sum(kwargs.values())
# result=sum_all(a=1,b=9,c=8,d=5)
# print(result)
# 2: Multiply all arguments
#args
# def multiply_all(*args):
#     product=1
#     for num in args:
#       product*=num
#     return product
# result=multiply_all(1,2,3,4,5) 
# print(result)
# #kwargs
# def multiply_kwargs(**kwargs):
#     product = 1
#     for value in kwargs.values():
#         product *= value
#     return product

# result = multiply_kwargs(a=1, b=2, c=3)
# print(result) 
# 3: Concatenate all arguments
# args
# def concatenate_args(*args):
#     return "".join(args)
# result=concatenate_args('Welcome', ' ','all')
# print(result)
# kwargs
# def concatenate_args(**kwargs):
#     return "".join(str(value) for value in kwargs.values())
# result=concatenate_args(a="Welcome", b=" ", c="all!")
# print(result)
# 4.Print arguments and keywords
#*args
# def print_args(*args):
#     print("Positional Arguments:")
#     for index, arg in enumerate(args):
#         print(f"Argument {index + 1}: {arg}")

# print_args('apple', 'banana', 'cherry')
# #*kargs
# def print_arguments_and_keywords(*args, **kwargs):
#     # Print positional arguments
#     print("Positional Arguments:")
#     for index, arg in enumerate(args):
#         print(f"Argument {index + 1}: {arg}")

#     # Print keyword arguments
#     print("\nKeyword Arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_arguments_and_keywords('apple', 'banana', name='Alice', age=30)
# 5.Display dictionary contents
#args
# def display_args_as_dict(*args):
#     args_dict = {f'arg_{i + 1}': arg for i, arg in enumerate(args)}
#     print("Positional Arguments as Dictionary:")
#     print(args_dict)

# display_args_as_dict('apple', 'banana', 'cherry')
#kwargs
def display_kwargs_as_dict(**kwargs):
    print("Keyword Arguments as Dictionary:")
    print(kwargs)

display_kwargs_as_dict(name='Alice', age=30, city='New York')

    

