# Write a Python program to find the second smallest number in a list


ls = [5, 3, 2, 4, 9, 2, 5, 15, 12, 14, 19]

print(ls)
# first we have to remove all the duplicate values let's make simple just create a set as we all know set doesn't contain duplicate value and it also sort the array.
# then we again make set to a list for printing its last second index for second greatest number
set_to_list = list(set(ls))

print("after converting list -> set -> list")
print(set_to_list)
length_of_setA = len(set_to_list)
print(set_to_list[length_of_setA - 2])
