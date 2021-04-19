"""
A program’s control flow is the order in which the program’s code executes.
The control flow of a Python program is regulated by conditional statements, loops, and function calls.
"""

# --------------------------------------------------------------- #

# Let's First talk about Boolean
my_boolean = True
print(my_boolean)

# Boolean Comparison
print("Annie" > "Andy")
print(7 <= 8)
print(9 >= 9.0)

# Boolean Logic
print(1 == 1 and 2 == 2)
print(1 == 1 or 2 == 3)
print(not 1 != 1)

# --------------------------------------------------------------- #

# If Statement
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")


# If else Statement
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")


# --------------------------------------------------------------- #

# While loop
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

# --------------------------------------------------------------- #

# For loop or for in loop (Iterator)
str = "testing for loops"
count = 0
for x in str:
   if x == 't':
    count += 1
print(count)

# For Range
numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

# Let's solve a problem of FizzBuzz
n = int(input())

for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


"""
Let's Talk About Exception - >
Different exceptions are raised for different reasons.
Common exceptions:
ZeroDivisionError: when we divide a number by zero.    # 10/0, 50/0
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""

# Exception Handling
try:
    variable = 10
    print(variable + "Bucky")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")
finally:
    print("done")

# Raise an Exception
name = "007"
raise NameError("Invalid name!")

# Assertion - > An assertion is a sanity-check that you can turn on or turn off
# when you have finished testing the program.

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)







