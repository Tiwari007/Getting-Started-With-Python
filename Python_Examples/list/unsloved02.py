# Write a Python program to change the position of every n-th value with the (n+1)th in a list


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("before changing position")
print(ls)
for l in range(len(ls)-1):
    ls[l] = ls[l+1]

print("after changing position")
ls.pop()
print(ls)