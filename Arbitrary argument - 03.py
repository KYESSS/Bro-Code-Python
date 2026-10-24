# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguements
#            * unpacking operator
#            1. positional, 2. Default, 3. keyword, 4. ARBITRARY

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St",
              apt="100",
              city="Seaham",
              county="Durham",
              postcode="SR7 0HS")
