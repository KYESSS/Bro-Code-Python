# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguements
#            * unpacking operator
#            1. positional, 2. Default, 3. keyword, 4. ARBITRARY

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('city')},"
          f"{kwargs.get('county')}, {kwargs.get('post_code')}")

shipping_label("Mr", "Kye", "Williamson",
               street="123 Fake St.",
               city="Seaham",
               county="Durham",
               post_code="SR7 0HS")
