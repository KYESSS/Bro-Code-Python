# variable scope = where a variable is visible and accessible
# scope resuoltion = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

