"""
Let's first talk about Variables - > Variables are nothing but reserved memory locations to store values.
This means that when you create a variable you reserve some space in memory.
Based on the data type of a variable, the interpreter allocates memory and decides
what can be stored in the reserved memory.
"""


# Variables and Data Types
IntegerValue = 786
FloatValue = 78.6
StringValue = "Hello Bucky"
AnotherStringValue = 'Hey Its cool'
Blah_Blah = True                                    # Boolean Value
list_of_numbers = [1, 2, 3, 4]                      # list
tuple_of_numbers = (1, 2, 3, 4)                      # Tuple
Dictionary_of_keyValue_Pair = {"Hey": 1, "Its": 2}  # Dictionary

# Working with strings - > As we all know string is set of character "Blah Blah Blah" this is an string.
string_value1 = "Welcome to StepIn Buddy"     # String Initialized
print(string_value1)

string_value2 = input()                       # String Given By user
print(string_value2)

print(string_value1 + string_value2)          # Addition of two string
print("abra" * 2)                             # Multiplication of string by integer gives repition of string.
# OUTPUT : - "abraabra"

# In_Place Operator - > In place operator allow you to write code more precise
x = 10
x = x + 15      # or we can write " x += 15 " both are same
print(x)


# There are so many function to operate with strings.
print(", ".join(["spam", "eggs", "ham"]))           # OUTPUT : - "spam, eggs, ham"
print("Hello ME".replace("ME", "world"))            # OUTPUT : - "Hello world"
print("This is a sentence.".startswith("This"))     # OUTPUT : - "True"
print("This is a sentence.".endswith("sentence."))  # OUTPUT : - "True"
print("This is a sentence.".upper())                # OUTPUT : - "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower())               # OUTPUT : - "an all caps sentence"
print("spam, eggs, ham".split(", "))                # OUTPUT : - "['spam', 'eggs', 'ham']"


# HACKERRANK PYTHON BASIC STRING QUESTIONS ANSWER HINTS

# 1 - Swap_Case.py
"""
s.swapcase()
"""

# 2 - Whats_Your_name.py
"""
# use string formatting
print("Hello {} {}! You just delved into python.".format(first_name,last_name))
"""

# 3 - Split_and_Join.py
"""
"-".join(line.split())
"""

# 4 - Capitalize!.py
"""
' '.join(word.capitalize() for word in s.split(' '))
"""

# 5 - Mutation.py
"""
def mutate_string(string, position, character):
    str1 = string[:position]
    str2 = string[position + 1:]
    return str1 + character + str2
"""

# 6 - String_Validators.py
"""
print(any([char.isalnum() for char in s]))
"""

# 7 - TextWrap.py
"""
Use of Textwrap.fill
"""





