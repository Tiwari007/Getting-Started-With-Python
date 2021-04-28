cities = {101: "Pune", 102: "Mumbai", 105: "Delhi", 103: "Kolkatta", 104: "Bengaluru"}
print(cities)  # unordered
print(cities[102])
# val=cities[109]         # KeyError
print(cities.get(103, "NIL"))
print(cities.get(107, "NIL"))

print(104 in cities)
print(105 not in cities)

for k in cities:
    print(cities[k])
for kid, name in cities.items():
    print(kid, name)

print(len(cities))
