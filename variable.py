#local
def f():
    s='hi'
    print(s)
f()    
#global
s='hiiii'
def f():
    print(s)
f()
#nonlocal
def outer():
    a = 5
    b = 6

    print("Before:", a, b)

    def inner():
        nonlocal a, b
        a = 10
        b = 20
        print("Inside:", a, b)

    inner()

    print("After:", a, b)

outer() 
#globals()
name='py'
marks='99'
print(globals()['name'])  
print(globals()['marks'])
print(globals())  
print()
#locals
def func():
    x,y=49,50
    print(locals())
func()    