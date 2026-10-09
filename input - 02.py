#input() = A FUNCTION THAT PROMTS THE USER TO ENTER DATA
#          RETURNS THE ENTERED DATA AS A STRING

name = input("What is your name?: ")
age = int(input("How old are you?: "))
age = age + 1

print(f"Hello {name}!")
print(f"HAPPY BIRTHDAY!")
print(f"You are {age} years old")