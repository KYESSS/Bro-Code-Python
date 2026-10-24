# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguements
#            * unpacking operator
#            1. positional, 2. Default, 3. keyword, 4. ARBITRARY

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))

