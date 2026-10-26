# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _:
            return ("Not a valid day")

print(day_of_week(4))
