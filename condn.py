# Write a Python program to check whether a number is positive, negative, or zero using simple if statements.
num=int(input('Enter num:'))
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')    


# Write a Python program to determine whether a student has passed or failed based on marks entered by the user using if-else.
marks=int(input('Enter marks:'))
if marks>=42:
    print('pass')
else:    
    print('fail')

# Write a Python program to check whether a number is even or odd using conditional statements.
num=int(input('Enter num:'))
if  num%2==0:
    print('Even')
else:    
    print('Odd')

# Write a Python program to find the largest of two numbers using if-else.
n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
if n1>n2:
    print(f'{n1}is greatest')
else:    
    print(f'{n2}is greatest')

# Write a Python program to check whether a person is eligible to vote or not.
age=int(input('Enter age:'))
if age>=18:
    print('can vote')
else:
    print('cannot  vote')
"""Write a Python program to calculate bonus:

Salary above 50,000 → 10% bonus
Otherwise → 5% bonus"""
salary=int(input('Enter salary:'))
if salary>50000:
    bonus=0.1*salary
    print(salary)
else:    
    bonus=0.05*salary
    print(salary)
# Write a Python program to find the greatest among three numbers using the if-elif-else chain.
n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
n3=int(input('Enter n3:'))
if n1>n2 and n1>n3:
    print(f'{n1} is greatest')
elif n2>n1 and n2>n3:
    print(f'{n2} is greatest')
else:
    print(f'{n3} is greatest')

# Write a Python program to display the grade of a student based on marks:

# 90 and above → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F
marks=int(input('Enter marks:'))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("F")
    
# Write a Python program to determine whether a year is a leap year or not.
year=int(input('Enter year:'))
if (year%400==0)or(year%4==0 and year%100!=0):
    print("Leap Year")
else:    
    print("Not Leap Year")


# Write a Python program to check whether a character entered by the user is a vowel or consonant.
ch=input('Enter ch:').lower()
if ch in 'aeiou':
    print('Vowel')
else:    
    print('consonant')


# Write a Python program to create a simple calculator using if-elif-else for addition, subtraction, multiplication, and division.
n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
operator=input('choose :+,_,*,/')
if operator=='+':
    print(n1+n2)
elif operator=='-':
    print(n1-n2)
elif operator=='*':
    print(n1*n2)
elif operator=='/':
    print(n1/n2)
else:
    print('input valid operator')    


# Write a Python program to determine the type of triangle based on sides entered:

# Equilateral
# Isosceles
# Scalene
n1=int(input('Enter n1:'))
n2=int(input('Enter n2:'))
n3=int(input('Enter n3:'))
if n1==n2 or n2==n3 or n1==n3:
    print('isosceles')
elif n1==n2==n3:
    print('equilateral')    
else:
    print('scalene')
# Write a Python program to check whether a number is divisible by both 5 and 11.
n3=int(input('Enter n3:'))
if n3%11==0 and n3%5==0:
    print('Divisible')
else:    
    print(' not Divisible')

# Write a Python program to determine whether a person can get a driving license based on age and vision test result using multiple conditions.
age=int(input('Enter age:'))
vision=input('Vision test: pass/fail').lower()
if age>=18 and vision=='pass':
    print('Can get')
else:    
    print('Cannot get')


# Write a Python program to classify temperature:

# Below 0 → Freezing
# 0–15 → Cold
# 16–30 → Warm
# Above 30 → Hot
temp=int(input('Enter temp:'))
if temp<0:
    print('freezing')
elif temp>=0 and temp<=15:
    print("cold")
elif temp>=16 and temp<=30:
    print("warm")
else:
    print('hot')    
# Write a Python program to check login credentials using username and password with nested conditions.
username=input('Enter username:')
password=input('Enter password:')
if username=='admin':
    if password=='psw123':
        print('login successfull')
    else:
        print('Invalid psw')    
else:
    print('invalid username')
# Write a Python program to calculate electricity bill according to units consumed using multiple elif blocks.
# 100unit=5rs,above 100 to200=10rs ,above 200=20rs
unit=int(input('Enter unit:'))
if unit<=100:
    bill=unit*5
elif unit<=200:
    bill=100*5+(unit-100)*10
else:
    bill=100*5+100*10+(unit-200)*20  
print(bill)
"""Write a Python program to implement a menu-driven system using Python match-case (switch case equivalent) for:

Area of Circle
Area of Rectangle
Area of Triangle"""
import math
shape=input('enter circle,rectangle,triangle').lower()
match shape:
    case "circle":
        r=float(input('radius:'))
        print('area:',math.pi*r*r)
    case "rectangle":
        l=float(input('length:'))
        b=float(input('breath:'))
        print('area:',l*b)
    case "triangle":
        h=float(input('height:'))
        b=float(input('base:'))
        print('area:',0.5*b*h)
    case _:
        print('Invalid')
# Write a Python program using match-case to display the day name based on day number entered by the user.
operator=int(input('Enter from 1-7'))
match operator:
  case 1:
        print('Sunday')
  case 2:
        print('monday')
  case 3:
        print('tuesday')
  case 4:
        print('wednesday')
  case 5:
        print('thursday')
  case 6:
        print('friday')
  case 7:
        print('saturday')
  case _:
        print('Invalid')      

# Write a Python program using match-case to perform arithmetic operations based on operator entered (+, -, *, /).
num1=float(input('Enter first number:'))
num2=float(input('Enter second number:'))
operator=input('choose (+,_,*,/)')
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print('Invalid operator')
