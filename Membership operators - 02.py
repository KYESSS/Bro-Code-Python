# Membership operators = used to test whether a value or variable is found in a
#                        sequence (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

students = {"Jake", "Beth", "James"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"Student {student} is a student")
else:
    print(f"Student {student} is not a student")

