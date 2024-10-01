# functions in regex
import re
# #match()
# string="Welcome to ocean academy"
# x=re.match("Welcome",string)
# print(x)
# print(x.group())
# # search()
# string="Welcome to ocean academy"
# x=re.search("ocean",string)
# print(x)
# print(x.group())
# findall()
# string="Welcome to ocean academy to"
# x=re.findall("to",string)
# print(x)
# print(" ".join(x))
#split()
# string="Welcome to ocean academy"
# x=re.split("to",string)
# print(x)
# print(",".join(x))
#sub()
# string="Welcome to ocean academy"
# x=re.sub("to","for",string)
# print(x)
# print("".join(x))
# regular expression task
# Write a function that extracts dates in the format DD-MM-YYYY from a given text.
# import re

# def extract_dates(text):
#     date_pattern = r'\b\d{2}-\d{2}-\d{4}\b'
#     return re.findall(date_pattern, text)

# # Test the function
# text = "12-05-2023, 30-12-2024."
# print(extract_dates(text)) 
# Write a function that replaces all instances of a word in a string with another word.
# import re

# def replace_word(text, old_word, new_word):
#     pattern = re.escape(old_word)  # Escape any special characters in the old word
#     return re.sub(pattern, new_word, text)

# # Test the function
# text = "Hello world, welcome to the world."
# new_text = replace_word(text, "world", "universe")
# print(new_text)  # Output: 'Hello universe, welcome to the universe.'
# Write a function to extract phone numbers from a given text. Consider the format (123) 456-7890.      
# import re

# def extract_phone_numbers(text):
#     phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
#     return re.findall(phone_pattern, text)

# # Test the function
# text = "Call me at (123) 456-7890 or (987) 654-3210."
# print(extract_phone_numbers(text))  
# Write a function that validates whether a given string is a valid email address. The email must follow the general 
# pattern of local_part@domain.tld.
# import re
# def is_valid_email(email):
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     return bool(re.match(email_pattern, email))

# # Test the function
# print(is_valid_email("example@test.com"))  # Output: True
# print(is_valid_email("invalid-email.com"))  # Output: False







