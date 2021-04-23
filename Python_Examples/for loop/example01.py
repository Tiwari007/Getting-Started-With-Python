ls = [1+7j, 1, 1.2, 0, "hello"]

for number in ls:
    if type(number) == type(1):
        print(number,"number is a Real Number...")
    elif type(number) == type(1.0):
        print(number," is a Float Number...")
    elif type(number) == type("Abc"):
        print(number," is a String....")
    elif type(number) == type(1 + 2j):
        print(number," is a complex number...")
    elif number == 0:
        print(number," is 0...")
    else:
        print("unknown type...")

    print("\n") 


# looping through for loop


for i in range(len(ls)):
    print(ls[i])

    