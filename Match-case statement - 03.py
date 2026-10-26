# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return ("Not a day of the week")

print(is_weekend("Saturday"))
print(is_weekend("Thursday"))
print(is_weekend("Pizza"))