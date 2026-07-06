# Exercises Chapter 2
# 1. Write a Python program to calculate the length of an input string.
string=input("enter a string:")
print(f'The length of {string} is {len(string)}')
# 2. Write a Python program to calculate area of a rectangle in which user is asked to input length and breadth of the rectangle.
length=int(input('Length:'))
breadth=int(input('breadth:'))
area=length*breadth
print(area)
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, print empty string.
string=input("Enter string:")
if len(string)<2:
    print(" ")
else:
    print(string[:2]+string[-2:])    


# Sample String : 'college'
# Expected Result : 'coge'
# Sample String : 'co'
# Expected Result : 'coco'
# Sample String : 'e'
# Expected Result : Empty String
"""4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to "#", except the first char itself.
Sample String : 'restart'
Expected Result : 'resta#t'
use replace() function"""
stri=input('enter string:')
a=stri[0]
new=stri.replace(a,'#')
print(a+new[1:])
# 5. Write a Python program to calculate area and circumference of a circle in which user is asked to input radius of the circle.
# Use import math and also without use of math function.
import math
r=float(input('RADIUS:'))
print('Area is',math.pi*r*r)
print('Circum is',2*math.pi*r)
#without math
PI=3.14
r=float(input('RADIUS:'))
print('Area is',PI*r*r)
print('Circum is',2*PI*r)

# 6. Write a Python Program to Add Two Numbers.
a=int(input("enter n1"))
b=int(input("enter n2"))
print(a+b)
# 7. Write a Python Program to Find the Square Root.
import math
n=int(input('enter n:'))
print("sq root of",n,'is',math.sqrt(n))
# 8. Write a Python Program to Calculate the Area of a Triangle.
b=int(input("enter n1"))
h=int(input("enter n2"))
area=0.5*b*h
print(area)
# 9. Write a Python Progringam to Solve Quadratic Equation.
import math
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=b**2-4*a*c
if d==0:
    print('Real and Equal roots',-b/(2*a))
elif d>0:
    print('Real and distinct roots')
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print('Two roots are:',root1,'and',root2)
else:
    print('Imaginary root')
    real=-b/2*a
    img=math.sqrt(-d)/(2*a)
    print('R1=',real,'+',img,'i')    
    print('R2=',real,'-',img,'i')    
# 10. Write a Python Program to Swap Two Variables.
a=int(input("enter n1"))
b=int(input("enter n2"))
print('before:',a,b)
a,b=b,a
print('after:',a,b)
# 11. Write a Python Program to Generate a Random Number.
import random
num=random.randint(1,100)
print(num)
# 12. Write a Python Program to find Maximum of two numbers.
a=int(input("enter n1"))
b=int(input("enter n2"))
if a>b:
    print(a,'is max')
else:    
   print(b,'is max')