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

''' ----- #💡 Without Indexing sample:


'''

#💡 Without Indexing sample:
input_string = "Hello, World!"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string  # Prepend each character

# print("Original string:", input_string)
print("Reversed string:", reversed_string)


# Pseudocode


def reverse_string(get_input):
    return get_input[::-2]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)