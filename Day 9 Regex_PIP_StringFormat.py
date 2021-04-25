# PYTHON REGEX -> (REGEX - REGULAR EXPRESSION)
"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
"""

import re

txt1 = "Bucky knows where is Lucky"
x1 = re.search("^Bucky.*Lucky$", txt1)

print(x1)

# for more info - > https://www.w3schools.com/python/python_regex.asp
"""
findall ->	Returns a list containing all matches
search ->	Returns a Match object if there is a match anywhere in the string
split -> Returns a list where the string has been split at each match
sub -> 	Replaces one or many matches with a string
"""

txt2 = "Bucky knows where is Lucky"
x2 = re.findall("Vicky", txt2)
print(x2)

txt3 = "Bucky knows where is Lucky"
x3 = re.search("\s", txt3)
print("The first white-space character is located in position:", x3.start())

txt4 = "Bucky knows where is Lucky"
x4 = re.split("\s", txt4, 1)
print(x4)

txt5 = "Bucky knows where is Lucky"
x5 = re.sub("\s", "9", txt5, 2)  # replace first 2 occurrence
print(x5)

txt6 = "Bucky knows where is Lucky"
x6 = re.search("ky", txt6)
print(x6)  # this will print an object

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

txt7 = "Bucky knows where is Lucky"
x7 = re.search(r"\bL\w+", txt7)
print(x7.string)

# Validating Phone Number HackerRank Problem
"""
import re

N = int(input())

pattern = r"[7|8|9]{1}[0-9]{9}$"

for _ in range(N):
    if re.match(pattern, input()):
        print("YES")
    else:
        print("NO")
"""

# validating CARD NUMBER HackerRank Problem
"""
import re

pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:?\d{4}){3}'
    r'$')
for _ in range(int(input().strip())):
    print("Valid" if pattern.search(input().strip()) else "Invalid")
"""

# Detect Floating Point Number
"""
import re

N = int(input())

pattern = "^[-+]?[0-9]*\.[0-9]+$"

for _ in range(N):
    num = input()
    if re.match(pattern, num):
        print("True")
    else:
        print("False")
"""

# PIP (Python Index Packager)
# Package - > A package contains all the files you need for a module.
#             Modules are Python code libraries you can include in your project.

"""
For Downloading a package just type "pip install <package-name>"
For removing a specific package type "pip uninstall <package-name>"
Use the list command to list all the packages installed on your system: "pip list"
Find More Packages -> https://pypi.org/
"""

# PYTHON STRING FORMATTING
"""
The format() method allows you to format selected parts of a string.
Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
To control such values, add placeholders (curly {}) in the text, and run the values through the format() method:
"""

number = 15.2458745
print("we just consider upto 2 decimal places. so here's your score {:.2f}".format(number))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myname = "I have a {count} name, one is {name1} and another one is {name2}."
print(myname.format(count=2, name1="Bucky", name2="Alita"))
