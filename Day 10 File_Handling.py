# PYTHON FILE HANDLING
"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.
"""

# The key function for working with files in Python is the open() function.

"""
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

f = open("data.txt", "r")
print(f.read())

f = open("data.txt", "r")
print(f.read(5))  # read the first 5 character

f = open("data.txt", "r")
print(f.readline())  # read the first line

f = open("data.txt", "r")
for x in f:
    print(x)

f.close()

# WRITING TO AN EXISTING FILE

"""
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

f = open("data1.txt", "w")
f.write("Whoops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("data1.txt", "r")
print(f.read())

# CREATING A NEW FILE
"""
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""

import os

if os.path.exists("data2.txt"):
    os.remove("data2.txt")
else:
    print("The file does not exist")

# READ JSON FILE USING PYTHON


import json

# Opening JSON file
f = open('data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['User_Details']:
    print(i)

# Closing file
f.close()


# WRITE IN TO JSON FILE
import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data1.json', 'w') as outfile:
    json.dump(data, outfile)

