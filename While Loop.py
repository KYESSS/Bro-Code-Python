# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Your name is {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")

food = input ("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter anbother food you like (q to quit): ")

print(f"You like {food}")

num = int(input("Enter a number between 1 and 100: "))

while num < 1 or num > 100:
      print(f"{num} is not valid")
      num = int(input("Enter a number between 1 and 100: "))

print(f"Your number is {num}")

print ("Cheerio")