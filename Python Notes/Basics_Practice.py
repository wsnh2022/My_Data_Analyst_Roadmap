print("Hello world")
print("*" * 10)
# python is case-sensitive language so it is sensitive to the lower and upper case letter(a-z, A-Z)


# ------------- data types in python
# integer: whole numbers
# float: decimal numbers
# boolean: True or False 
# string: sequence of characters enclosed in quotes (single or double)

age = 34           # integer value
price = 19.99      # float value
is_online = True   # true ❌ True ✅, false ❌ False ✅
first_name = "John" # string value

print(age, price, is_online, first_name)

# ------------- Input Function is used to take input from the user
name = input("what is your name?")
print("hello " + name)

# ------------- Type Conversion
birth_year = input("Enter your birth year: ")
age = 2025 - int(birth_year)
print(age)  # converting integer to string for concatenation

# int()     converts a string to an integer
# float()    converts a string to a float
# str()     converts an integer or float to a string
# bool()   converts a value to a boolean (True or False)

# excercise get two numbers and sum float or integer
# type conversion is necessary when we want to perform arithmetic operations on user input

first = float(input("Enter first number: "))  # converting string to float
second = float(input("Enter second number: "))  # converting string to float

sum_result = first + second  # sum of two float numbers
print(f"The Sum is: {str(sum_result)}")  # converting float to string for concatenation

# ------------- strings
# strings are immutable, meaning they cannot be changed after creation
# string methods
greeting = "Hello, World!"
print(greeting.upper())  # converts to uppercase
print(greeting.lower())  # converts to lowercase
print(greeting.replace("World", "Python"))  # replaces a substring
print(greeting.split(","))  # splits the string into a list at the comma
print(greeting.find("World"))  # finds the index of a substring


word = "Python"
print(word[::-1])
