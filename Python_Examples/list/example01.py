numbers = [10, 12, 25, 48, 32, 18]
print(numbers[0])
print(numbers[3])
numbers[2] = 28
print(numbers)
print(numbers[9])
print(25 in numbers)
print(30 not in numbers)

sum = 0
for k in numbers:
    sum += k
print ("sum=", sum)