# Tuples and Sequences

t = 12345, 54321, 'hello!'
print(t[0])  # OUTPUT : - 12345
print(t)  # OUTPUT : - (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)  # OUTPUT : - (12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)  # OUTPUT : - ([1, 2, 3], [3, 2, 1])


empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))          # OUTPUT : - 0
print(len(singleton))      # OUTPUT : - 1
print(singleton)           # OUTPUT : - ('hello',)


# SETS

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
# OUTPUT : - {'orange', 'banana', 'pear', 'apple'}
print('orange' in basket)                 # fast membership testing   OUTPUT : - True
print('crabgrass' in basket)              # OUTPUT  - False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a # OUTPUT : - {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # letters in a but not in b   # OUTPUT : - {'r', 'd', 'b'}
print(a | b)                        # letters in a or b or both   # OUTPUT : - {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # letters in both a and b # OUTPUT : - {'a', 'c'}
print(a ^ b)                              # letters in a or b but not both  # OUTPUT : - {'r', 'd', 'b', 'm', 'z', 'l'}


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)        # OUTPUT : - {'r', 'd'}


# DICTIONARY

tel = {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel)      # OUTPUT : - {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])          # OUTPUT : - 4098
del tel['sape']
tel['irv'] = 4127
print(tel)          # OUTPUT : - {'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))        # OUTPUT : - ['jack', 'guido', 'irv']
sorted(tel)
print('guido' in tel)      # OUTPUT : - True
print('jack' not in tel)    # OUTPUT : - False


dictionary = {x: x**2 for x in (2, 4, 6)}
print(dictionary)
