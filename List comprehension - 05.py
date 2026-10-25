# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

grades = [85, 61, 90,45, 55, 77, 33]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)