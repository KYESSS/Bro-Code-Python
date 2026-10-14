# Logical operators AND

temp = 0
is_sunny = False

if temp >= 35 and is_sunny:
    print("It is a sunny day")
    print("It is hot outside")
elif temp <= 0 and is_sunny:
    print("It is a sunny day")
    print("It is cold outside")
elif temp > temp >0 and is_sunny:
    print("It is a cloudy day")
    print("It is a sunny day")
    print("It is warm outside")
if temp >= 35 and not is_sunny:
    print("It is a cloudy day")
    print("It is hot outside")
elif temp <= 0 and not is_sunny:
    print("It is a cloudy day")
    print("It is cold outside")
elif temp > temp >0 and not is_sunny:
    print("It is a cloudy day")
    print("It is warm outside")