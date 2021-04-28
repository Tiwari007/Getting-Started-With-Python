# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice
# if user order even number of slices, price per slice is Rs 120.00
# Print the total price depending on how many slices user orders.

How_many_pizza = int(input("How many pizza slices you want ?? : "))
total = 0
if How_many_pizza % 2 == 0:
    total = How_many_pizza * 120.00
else:
    total = How_many_pizza * 123.00
print(total)
