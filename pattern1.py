# Program Questions:
# 1. Write a Python program to create a list of five student names and print the list.
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
for i in student_names:
    print(i)
# 2. Write a Python program to access and print the first, last, and middle elements of a list.
student_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
print(student_names[0])
print(student_names[-1])
print(student_names[2])
# 3. Write a Python program to perform list concatenation and repetition operations.
list1=[1,2,3]
list2=[3,4,5]
list3=list1+list2
print(list3)
print(list1*3)
# 4. Write a Python program to change the value of a specific element in a list.
list1=[1,2,3,4,5,6]
list1[3]=91
print(list1)

# 5. Write a Python program to add elements to a list using `append()` and `insert()` methods.
list1=[1,2,3,4,5]
list1.append(6)
list1.insert(2,77)
print(list1)
# 6. Write a Python program to remove elements from a list using `remove()`, `pop()`, and `del`.
list1=[1,2,3,4,5]
list1.remove(3)
list1.pop()
del list1[0]
print(list1)
# 7. Write a Python program to sort a list permanently using the `sort()` method.
list1=[1,3,4,7,2,6]
list1.sort()
print(list1)
# 8. Write a Python program to sort a list temporarily using the `sorted()` function.
list1=[1,3,4,7,2,6]
print(sorted(list1))

# 9. Write a Python program to print a list in reverse order using the `reverse()` method.
list1=[1,3,4,7,2,6]
list1.reverse()
print(list1)
# 10. Write a Python program to find the length of a list using the `len()` function.
list1=[1,3,4,7,2,6]
print(len(list1))
# 11. Write a Python program to demonstrate index error handling while accessing list elements.
list1=[1,3,4,7,2,6]
idx=7
if idx<len(list1):
    print(list1[idx])
else:
    print('Index error')
#or
list1=[1,3,4,7,2,6]
try:
    print(list1[5])
except IndexError:

    print('Index out of range')            
# 12. Write a Python program to create a numerical list using the `range()` function.
num=list(range(1,11))
print(num)
# 13. Write a Python program to generate a list of even numbers from 1 to 50 using `range()`.
num=list(range(2,51,2))
print(num)
# 14. Write a Python program to print all elements of a list using a loop.
list1=[1,3,4,7,2,6]
for el in list1:
    print(el)
# 15. Write a Python program to print only the first three elements of a list using slicing.
list1=[1,3,4,7,2,6]
print(list1[:3])

# 16. Write a Python program to extract and print a slice of a list from index 2 to index 5.
list1=[1,3,4,7,2,6]
print(list1[2:6])

# 17. Write a Python program to loop through a sliced portion of a list.
list1=[1,3,4,7,2,6]
for el in list1[:4]:
    print(el)
# 18. Write a Python program to create a copy of a list and demonstrate that modifying one list does not affect the other.
list1=[1,3,4,7,2,6]
copylist1=list1.copy()
list1[2]=99
print(list1)
print(copylist1)
# 19. Write a Python program to find the maximum and minimum values in a numerical list.
list1=[1,3,4,7,2,6]
print(max(list1))
print(min(list1))
# 20. Write a Python program to count how many times a specific element appears in a list.
list1=[1,3,4,7,2,6,4,4,4,4]
print(list1.count(4))
# 21. Write a Python program to define a tuple containing five colors and print all elements.
tuple=('red','pink','blue','white','purple')
for el in tuple:
    print(el)
# 22. Write a Python program to access individual elements of a tuple using indexing.
print(tuple[0])
print(tuple[-1])
# 23. Write a Python program to loop through all values in a tuple using a `for` loop.
for el in tuple:
    print(el)
# 24. Write a Python program to demonstrate tuple immutability by attempting to modify a tuple element.
# tuple.append(7)
# print(tuple)
# 25. Write a Python program to create a new tuple by rewriting an existing tuple with additional elements.
tuple=('red','pink','blue','white','purple')
tuplenew=tuple+('black','brown')
print(tuplenew)