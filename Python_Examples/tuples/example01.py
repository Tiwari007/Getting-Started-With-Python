t1 = (10, 20, 30)
print(t1)
a, b, c = t1
t2 = ()
print(t2)
print(type(t1))

t3 = (101, "abcd", [25, 60, 80])
print(t3[2][1])
t3[2][0] = 30
print(t3)
# t3[1]="xyz"     # TypeError

t4 = (10, 20, 30, 40, 50)
print(t4[-1])

# slicing same as list

print(t1 + t4)  # t5 = t1 + t4
print (t1 * 2)  # t6 = t1 * 2

del t3

print(len(t4))
# t4.count(30), t4.index(30)

print(30 in t4)
sum = 0
for x in t4:
    sum += x