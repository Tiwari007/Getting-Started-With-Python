# Applications of List, Set, Tuple, and Dictionary.
"""
# List:
1 - Used in JSON format
2 - Useful for Array operations
3 - Used in Databases

# Tuple:
1 - Used to insert records in the database through SQL query at a time
2 - Ex: (1.’sravan’, 34).(2.’geek’, 35)
3 - Used in parentheses checker

# Set
1 - Finding unique elements
2 -Join operations

# Dictionary
1 - Used to create a data frame with lists
2 - Used in JSON
"""

# Let's first talk about List
"""
List is a non-homogeneous data structure which stores the elements in single row and multiple rows and columns.
It is ordered and allow duplicate elements donated by []. e.g. [1, 2, 3, 4 ]
"""

# Creating an empty List
l = []
list1 = ["abc", 34, True, 40, "male"]

# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)

# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # ['cherry', 'orange', 'kiwi']
print(thislist[::-1])  # ['mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple']
print(thislist[:5])  # ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(thislist[3:])  # ['orange', 'kiwi', 'melon', 'mango']
print((thislist[3:5:-1]))  # ['melon', 'kiwi']

# List Iterator
thislist1 = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
for fruit in thislist1:
    print(fruit)
thislist1.insert(2, "watermelon")
print(thislist1)

# Append, Insert, Extend
print(thislist.extend(thislist1))

# Remove, Pop, Del, Clear
print(thislist.remove("apple"))
print(thislist1.pop(1))
del thislist[0]
print(thislist)
thislist1.clear()
print(thislist1)

# Loops
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist.sort(reverse=True)  # For Descending order
thislist.reverse()  # Now It converting into ascending order
print(thislist)

# Now Let's talk about tuple

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Same rule as for accessing list through index.
print(thistuple[::-1])  # For reversing

# Unpacking Of tuples
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
# if asterisks is added to any variable Python will assign values to the variable
# until the number of values left matches the number of variables left.
print(green)
print(tropic)
print(red)

print(thistuple.count())
print(thistuple.index("cherry"))

# Now Let's talk about python Set
s = set()
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Set Update
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove, Discard, Pop, Del, Clear
thisset.remove("banana")
print(thisset)

thisset.discard("apple")
print(thisset)

x = thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset)

thistuple1 = ("Guava", "Grapes", "MuskMelon")
del thistuple1[0]
print(thistuple1)
del thistuple1
print(thistuple1)

# Join Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Join Two set using UPDATE
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Intersection which is common in these two
thisset1 = {"hey", "hi", "hello"}
thisset2 = {"hello", "Entry", "Kawaii"}
thisset1.intersection_update(thisset2)
print(thisset1)
thisset3 = thisset1.intersection(thisset2)
print(thisset3)

# Difference remove same element in both set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Now lastly talk about python dictionary
d = {}
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
# Removing key-value pair
del d[10]
print("Dictionary", d)

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict["colors"])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.values())
print(car.keys())
print(car.items())

# Adding
car["color"] = "blue"
# Update
thisdict.update({"color": "black"})

# Pop, PopItems ,Del, Clear
car.pop("year")
print(car)
car.popitem()
print(car)

Anime = {
    "name": "BuckyAlita",
    "company": "Alita",
    "season": "2",
    "year": 2025
}
del Anime["year"]
print(Anime)
Anime.clear()
print(Anime)

Anime2 = {
    "name": "BuckyAlita",
    "company": "Alita",
    "season": "2",
    "year": 2025
}

# Loop through Dictionary
for x, y in Anime2.items():
    print(x, y)

