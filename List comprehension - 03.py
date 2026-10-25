# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

fruits = ["apple", "banana", "cherry"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)