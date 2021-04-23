scores = { "John":80, "Scott":50, "Ram": 70, "Ravi":90}

print(scores.keys())
print(scores.values())
klist = scores.keys()
print(type(klist))

print(sorted(scores))

del scores["Scott"]
print(scores)
scores.pop("Ram")        
print(scores)
