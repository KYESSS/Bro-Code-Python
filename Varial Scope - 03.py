# variable scope = where a variable is visible and accessible
# scope resuoltion = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import e

def func1():
    print(e)

# e = 3

func1()

