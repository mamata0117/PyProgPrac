'''8. Write a Python program to implement a menu-driven system using Python
match-case (switch case equivalent) for:
Area of Circle
Area of Rectangle
Area of Triangle'''

Area_shape=input('Enter the shape to calculate area (Circle/Rectangle/Triangle): ').lower()
match Area_shape:
    case 'circle':
        radius=float(input('Enter the radius of the circle: '))
        area=3.14*radius**2
        print(f'The area of the circle is: {area}')
    case 'rectangle':
        length=float(input('Enter the length of the rectangle: '))
        width=float(input('Enter the width of the rectangle: '))
        area=length*width
        print(f'The area of the rectangle is: {area}')
    case 'triangle':
        base=float(input('Enter the base of the triangle: '))
        height=float(input('Enter the height of the triangle: '))
        area=0.5*base*height
        print(f'The area of the triangle is: {area}')
    case _:
        print('Invalid shape entered. Please choose Circle, Rectangle, or Triangle.')