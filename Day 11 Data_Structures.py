# SO LET'S FIRST TALK ABOUT DATA STRUCTURE FOR LIST
"""
As we know list has so many functions.
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))  # OUTPUT :- 2
print(fruits.count('tangerine'))  # OUTPUT :- 0
print(fruits.index('banana'))  # OUTPUT :- 3
print(fruits.index('banana', 4))  # Find next banana starting a position 4. OUTPUT :- 6
fruits.reverse()
print(fruits)  # OUTPUT :- ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits)  # OUTPUT :- ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits)  # OUTPUT :-['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop())  # OUTPUT :- pear

# USING LISTS AS STACK( LIFO )
"""
To add an item to the top of the stack, use append(). 
To retrieve an item from the top of the stack, use pop() without an explicit index.
"""
stack = [3, 4, 5, 6, 7]
print(stack)  # OUTPUT :- [3, 4, 5, 6, 7]
stack.pop()  # pop the last element that is 7
print(stack)  # OUTPUT :- [3, 4, 5, 6]
stack.pop()  # pop the last element that is 6
stack.pop()  # again pop the last element that is 5
print(stack)  # OUTPUT :- [3, 4]

# USING LISTS AS QUEUES( FIFO )
"""
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
"""
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
queue.popleft()  # The first to arrive now leaves which was 'Eric'
queue.popleft()  # The second to arrive now leaves which means 'John'
print(queue)  # Remaining queue in order of arrival OUTPUT :- deque(['Michael', 'Terry', 'Graham'])

# LIST COMPREHENSION
List_of_squares1 = []
for x in range(10):
    List_of_squares1.append(x ** 2)
print(List_of_squares1)  # OUTPUT :- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# OR WE CAN SIMPLY WRITE
List_of_squares2 = [x ** 2 for x in range(10)]
print(List_of_squares2)

# OR BY USING LAMBDA TOO
List_of_squares3 = list(map(lambda x: x ** 2, range(10)))
print(List_of_squares3)

# LET'S SEE SOME EXAMPLES
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)  # OUTPUT :- [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

# NESTED LIST COMPREHENSION
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# print the transpose of matrix
print([[row[i] for row in matrix] for i in range(4)])
# Using Zip() Function
print(list(zip(*matrix)))
