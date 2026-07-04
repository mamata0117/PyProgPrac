side1=float(input("Enter the length of the first side of the triangle: "))
side2=float(input("Enter the length of the second side of the triangle: "))
side3=float(input("Enter the length of the third side of the triangle: "))
if side1==side2 and side2==side3:
    print('Equilateral')
elif side1==side2 or side2==side3 or side1==side3:
    print('Isosceles')
else:
    print('Scalene')

#num div by 5 and 11
num=int(input('enter num:'))
if num%5==0 and num%11==0:
    print('divisible')
else:
    print(' not divisible')
#. Write a Python program to determine whether a person can get a driving license
# based on age and vision test result using multiple conditions.
age=int(input('enter age:'))
vision_test=input('enter vision test result (pass/fail): ')
if age>=18 and vision_test.lower()=='pass':
    print('Eligible for driving license')
else:
    print('Not eligible for driving license')