# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_nums = [numb for numb in numbers if numb >= 0]
negative_nums = [numb for numb in numbers if numb < 0]
even_nums = [numb for numb in numbers if numb % 2 == 0]
odd_nums = [numb for numb in numbers if numb % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)