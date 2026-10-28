# variable scope = where a variable is visible and accessible
# scope resuoltion = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    print(a)

def func2():
    print(b)

a = 1
b = 2
func1()
func2()

