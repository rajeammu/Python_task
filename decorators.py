# decorator function
# def func2(fun):
#     def func3():
#         print("welcome everyone")
#         fun() #call the original function 
#         print("Thanks for visiting")
#     return(func3) #return the inner function 
# @func2        
# def func1():
#     print("welcome to ocean academy")
# func1=func2(func1)    
# func1()  #call the decorator function 
# decorators function with arguments 
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator_repeat

@repeat(num_times=2)  # Decorate the function to repeat it 2 times
def say_hello(name):
    print(f"Hello", name)

# Call the decorated function
say_hello("Alice")

# decorators function with  with arguments and more decorators 
# def decorator_one(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator One: Before the function.")
#         func(*args, **kwargs)
#         print("Decorator One: After the function.")
#     return wrapper

# def decorator_two(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator Two: Before the function.")
#         func(*args, **kwargs)
#         print("Decorator Two: After the function.")
#     return wrapper

# @decorator_one
# @decorator_two
# def greet(name):
#     print("Hello", name)

# # Call the decorated function
# greet("Alice")
