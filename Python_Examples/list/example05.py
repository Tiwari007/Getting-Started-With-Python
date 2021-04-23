
mylist = [10, 20, 30, 40]
mylist.append(50)
mylist.extend([60,70])
print(mylist)

print(len(mylist))
print(mylist.index(50))

mylist.insert(3,35)
print(mylist)

print(mylist.count(30))
mylist.reverse()

del mylist[2]
print(mylist)
del mylist[1:4]     # mylist[1:4]=[]
print(mylist)

# mylist.remove(60)
mylist.pop()
print(mylist)

# newlist = mylist
newlist = mylist.copy()  # newlist = mylist[:]
mylist.append(80)
newlist.append(90)
print(mylist)
print(newlist)

words = [ "hello", "abcd", "xyz", "pqr", "12"]

words.sort(reverse=True)
print(words)

words.sort(key=len)
print(words)

def keyfun(str):
    return str[-1]
words.sort(key=keyfun)
print(words)

# sort, key, reverse

data = [12, 25, 18, -48, 35, -72, 64, 55]
print (sum(data))
print (min(data))
print (max(data))
print( any(x>50 for x in data))
print( all(x%2==0 for x in data))
entries=[]
for entry in enumerate(data):
    entries.append(entry)
print(entries)
