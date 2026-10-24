# default argument = A default value for certain parameters
#                     default is used when the argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. Default, 3. KEYWORD, 4. arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=44, area=123, first=456, last=5653)

print(phone_num)