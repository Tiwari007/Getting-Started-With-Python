# Let's talk about Function in Python
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""


# Firstly let's see how we can writing a empty function using pass
def func():
    pass  # Now it doesn't give any error.


# Example 1
def my_function(name="Vivek Tiwari"):  # definition of function. Here "name is argument" and Vivek is Default argument.
    print("Welcome" + name)  # print using simple concatenation
    print("Welcome {}".format(name))  # print using format


my_function("Bucky")  # Calling a function with parameters
my_function("Alita")
my_function("Hinata")


# Example 2
def my_function(*child):
    print("The Oldest child is " + child[2])


my_function("Bucky", "Alita", "Hinata")


# Example 3
# Python program to display the Fibonacci sequence


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n_terms = int(input())

# check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibonacci(i))

# Python Lambda
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

# Example 1
sum_of_numbers = lambda a, b, c: a + b + c
print(sum_of_numbers(5, 6, 2))


# Example 2
def myfunc1(n):
  return lambda a : a * n


mydoubler = myfunc1(2)
mytripler = myfunc1(3)

print(mydoubler(11))
print(mytripler(11))


# Some question on function

# Write a Python program to detect the number of local variables declared in a function.
def abc():
    x = 1
    y = 2
    str1= "w3resource"
    print("Python Exercises")


print(abc.__code__.co_nlocals)


# How to run a code when string containing your desired code
mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""
exec(mycode)
exec(code)


# Write a Python function to create and print a list where the values are square of
# numbers between 1 and 30 (both included).

def print_values():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l)


print_values()
