#positional argument
# this is a function that takes two positional arguments and returns their sum.also, it has a default value for the second argument.
def add_numbers(a, b=0):
    return a + b
print(add_numbers(5))  # Output: 5 this is default argument
print(add_numbers(5, 10))  # Output: 15 This is positional argument
#keyword argument
print(add_numbers(a=5, b=10))  # Output: 15 This is keyword argument
print()
# keyword arguments can be passed in any order, as long as the parameter names are specified.
#position only all arg before / can be passed as pos only
def add(a,b,c,/):
    return(a+b+c)
print(add(3,4,5))
print()
# add(3,4,c=5) is wrong
 #keyword only
def greet(*,name,age):
    print(name,age)
greet(name='shyam',age='22')    
greet(age='22',name='ram')    
#both position only and keyword only
def add(a,b,/,c,d=9,*,e,f):
    addn=a+b+c+d+e+f
    print(addn)
add(2,3,4,e=-9,f=10)