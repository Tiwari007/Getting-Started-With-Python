"""
Today we're discuss about python 3 important concept.
1 - Dates -> A date in Python is not a data type of its own, but we can import a
             module named datetime to work with dates as date objects.
2 - Math -> Python has a set of built-in math functions, including an extensive math module,
            that allows you to perform mathematical tasks on numbers.
3 - JSON
"""

# # # DATES # # #
import datetime

x = datetime.datetime.now()  # for current/Today's date
print(x)  # The date contains year, month, day, hour, minute, second, and microsecond.
print(x.day)
print(x.year)
print(x.month)
print(x.strftime("%A"))  # For more information goto - > https://www.w3schools.com/python/python_datetime.asp
print(x.strftime("%c"))  # Print a local version of date and time

# Example -> Calculate your age in number_of_days by your birth date
today = datetime.date.today()
badday = datetime.date(1998, 10, 6)
age_in_days = today - badday
print(age_in_days)

# Example -> Calculate your age in terms of years by your birth date
from datetime import date


def calculate_age(birthdate):
    today_date = date.today()
    age = today_date.year - birthdate.year - ((today_date.month, today_date.day) < (birthdate.month, birthdate.day))
    return age


print(calculate_age(date(1998, 10, 6)), "years")

# # # Math # # #
"""Math has so many functions like minimum , maximum, power, square root etc.,"""

ls = [4, 1, 8, 2, 5, 7, 0, 9]
print(max(ls))
print(min(ls))

print([x * 2 for x in ls])  # double
print([x ** x for x in ls])  # power
x = abs(-7.25)
print(x)

import math

print(math.sqrt(625))
print(math.log(10, 2))

print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)

# Find the Euclidean distance between one and two dimensional points:
p = [3]
q = [1]
print(math.dist(p, q))
p = [3, 3]
q = [6, 12]
print(math.dist(p, q))

# Convert from radians to degrees:
print(math.degrees(8.90))
# Convert different degrees into radians
print(math.radians(180))

# # # JSON # # #
"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
"""

# Convert from JSON to Python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])



# Convert from python to JSON

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Convert a Python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

