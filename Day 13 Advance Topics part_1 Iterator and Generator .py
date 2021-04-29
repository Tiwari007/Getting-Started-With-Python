# PYTHON ITERATORS
"""
Iterators are objects that can be iterated upon.
In Today's file, we will learn how iterator works and
how you we can build our own iterator using __iter__ and __next__ methods.
"""

my_list = [4, 7, 0, 3]
my_iter = iter(my_list)  # get an iterator using iter()

print(my_iter)  # <list_iterator object at 0x000001E575493FD0>
print(next(my_iter))  # iterate through it using next()  # Output: 4
print(next(my_iter))  # Output: 7

# next(obj) is same as obj.__next__()
print(my_iter.__next__())  # Output: 0  or we can use print(next(my_iter)) also

print(my_iter.__next__())  # Output: 3
# next(my_iter)                           # This will raise error, no items left

# OR WE CAN ITERATE BY USING LOOP
for element in my_list:
    print(element)

print("_______________________________________________________________")
# LET'S TAKE AN ANOTHER EXAMPLE
listA = [7, 5, 8, 6, 9, 15]
iterable = iter(listA)

for element in iterable:
    print(element)

# OR WE CAN USE LIKE THIS TOO
# infinite loop
while True:
    try:
        # get the next item
        element = next(iterable)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break


# BUILDING A CUSTOM ITERATOR
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max_val=0):
        self.max = max_val

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print("______________________________________________________________")
# GENERATORS
"""
There is a lot of work in building an iterator in Python. 
We have to implement a class with __iter__() and __next__() method, 
keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.
=> a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()  # It returns an object but does not start execution immediately.

# We can iterate through the items using next().
print(next(a))

# Once the function yields, the function is paused and the control is transferred to the caller.

# Local variables and theirs states are remembered between successive calls.
print(next(a))
print(next(a))

# Finally, when the function terminates, StopIteration is raised automatically on further calls.
next(a)


# ANOTHER EXAMPLE
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


# FIBONACCI NUMBER USING GENERATORS
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))
