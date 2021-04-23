# Write a python program to check if the input number is
# - real number
# - float numner
# - string
# - complex number
# - Zero (0)

# number= 1+7j
# number = 1
# number = 1.1
# number = "hello"
# number = 0

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



