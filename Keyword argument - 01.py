# default argument = A default value for certain parameters
#                     default is used when the argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. Default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr", last="Williamson", first="Kye")