# Classes and Object

"""
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""


class Person1:
    def __init__(self, name, age):  # All classes have a function called __init__(),
        self.name = name  # which is always executed when the class is being initiated.
        self.age = age


p1 = Person1("John", 36)
p2 = Person1("Bucky", 22)

print("{} and {}".format(p1.name, p1.age))
print("{} and {}".format(p2.name, p2.age))

# The Self Parameter
"""
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, 
but it has to be the first parameter of any function in the class:
"""


class Person2:
    def __init__(see_not_self, name, age):
        see_not_self.name = name
        see_not_self.age = age

    def myfunc(not_self):
        print("Hello my name is " + not_self.name)


p1 = Person2("John", 36)
p1.myfunc()


# The pass statement


class Hello:
    pass


# Python Inheritance
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""


class Person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person3):
    def __init__(self, fname, lname):
        Person3.__init__(self, fname, lname)


s = Student("Bucky", "Alita")
s.printname()


# Use of Super() Keyword


class Person4:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person4):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


s = Student("Vivek", "Bucky", 2021)
s.welcome()


# del s -> for deleting attribute and object


# Example for Inheritance
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def display_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.input_sides()
t.display_sides()
t.find_area()


# Overloading the + Operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)


# Overloading the < operator
# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = Point(1, 1)
p2 = Point(-2, -3)
p3 = Point(1, -1)

# use less than
print(p1 < p2)
print(p2 < p3)
print(p1 < p3)
