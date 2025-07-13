# Write a Python program to Reverse a String?

''' ----- 💡 With Indexing sample:
string[start:stop:step]
string[empty:empty:-1] 

start is empty → start from end of string
stop is empty → go until beginning of string
step is -1 → step backwards one character at a time

So [::-1] means: "Start from the end, move backwards, one step at a time, and include every character."
'''

print("Python"[::-1])  # Outputs: nohtyP

''' result:
P  y  t  h  o  n
0  1  2  3  4  5  →  forward index
-6 -5 -4 -3 -2 -1 →  backward index
'''

# Pseudocode
# 1. Define a function that takes a string as input.
# 2. Use slicing to reverse the string.
# 3. Return the reversed string.

def reverse_string(s):  # Function to reverse a string
    return s[::-1]  # Using slicing to reverse the string

# Example usage
input_string = "Hello, World!"                  # Input string to be reversed
reversed_string = reverse_string(input_string)  # Reverse the string using the function
print("Original string:", input_string)         # compare the original string
print("Reversed string:", reversed_string)      # with the reversed string


## ==========================================================================================

#💡 Without Indexing sample:
input_string = "Hello, World!"
reversed_string = ""

for char in input_string:                      # Iterate through each character in the input string 
    reversed_string = char + reversed_string   # Prepend the character to the reversed string

# print("Original string:", input_string)
print("Reversed string:", reversed_string)

