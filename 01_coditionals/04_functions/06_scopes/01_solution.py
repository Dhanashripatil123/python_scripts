username  = "chaiaurcode"

def func():
    username= "chai"
    print(username)

print(username)
func()

x = 99
def func2(y):
    z = x+y
    return z
result = func2(4)
print(result)

x=99
def func3():
   global x
   x = 12
   
func3()
print(x) 


x = 99
def f1():
    x = 88
    def f2 ():
        print(x)
    #f2()    
    return f2
myresult = f1()
myresult()


def chaicoder(num):
        def actual(x):
           return x ** num
        return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))
