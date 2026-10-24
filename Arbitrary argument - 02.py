# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguements
#            * unpacking operator
#            1. positional, 2. Default, 3. keyword, 4. ARBITRARY

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Msc", "Kye", "Lewis", "Williamson")

