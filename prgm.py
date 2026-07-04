# #1
# list1=['ram','hari','min','kim','om']
# print(list1)
# #2
# print(list1[0])
# print(list1[-1])
# print(list1[1:-1])
# #3
# list1=[1,2]
# list2=[3,2]
# list3=list1+list2
# print(list3)
# print(list1*3)
# #4
# list1=[1,3,4,5]
# list1[2]=99
# print(list1)
# #5append and insert
# listm=['a','b',1,3,4]
# listm.append('orange')
# listm.insert(2,'c')
# print(listm)
# #6 remove(),pop(),del
# listn=[3,6,7,77,8,999,3,99,2,33]
# listn.remove(3)
# listn.pop()
# listn.pop(4)
# del listn[1]
# print(listn)
# #7 sort()
# listq=[3,6,7,77,8,999,3,99,2,33]
# listq.sort()
# print(listq)
# #8 sorted() temporary sort
# listq=[3,6,7,77,8,999,3,99,2,33]
# print(sorted(listq))
# 9 Write a Python program to print a list in reverse order using the reverse() method.
list=[4,6,8,1,2,3]
list.reverse()
print(list)

# 10. Write a Python program to find the length of a list using the len() function.
print(len(list))
# 11.1 Write a Python program to demonstrate index error handling while accessing list elements.
list1 = [10, 20, 30]
index = 5
if index < len(list1):
    print(list1[index])
else:
    print("Index out of range")
#11.2
list1 = [10, 20, 30]

try:
    print(list1[5])
except IndexError:
    print("Index out of range")
# 12. Write a Python program to create a numerical list using the range() function.
list=[]
for i in range(1,5):
    list.append(i)
print(list)
    # 13. Write a Python program to generate a list of even numbers from 1 to 50 using range() .
for i in range(1,51):
    if i%2==0:
        print(i,end=' ')
        
# 14. Write a Python program to print all elements of a list using a loop.
list1=[1,2,3,4,6,88.888,99]
for num in list1:
    print(num)

# 15. Write a Python program to print only the first three elements of a list using slicing.
list1=[1,2,3,4,6,88.888,99]
print(list1[:3])
# 16. Write a Python program to extract and print a slice of a list from index 2 to index 5.
list1=[1,2,3,4,6,88.888,99]
print(list1[2:6])
# 17. Write a Python program to loop through a sliced portion of a list.
list1 = [1,2,3,4,6,88.888,99]

for i in list1[2:6]:
    print(i)
# 18. Write a Python program to create a copy of a list and demonstrate that modifying one list does not affect the other.
list1=[2,4,5,6]
list_copy=list1.copy()
list1[0]=9
print(list1)
print(list_copy)
# 19. Write a Python program to find the maximum and minimum values in a numerical list.
list1=[2,4,5,6]
print(max(list1),min(list1))
# 20. Write a Python program to count how many times a specific element appears in a list.
list8=[2,3,8,6,8,5,8,3,8,5,8]
count=0
for i in list8:
    if 8==i:
        count+=1
print(count)   
 #another way
list8=[2,3,8,6,8,5,8,3,8,5,8]
print(list8.count(8))
# 21. Write a Python program to define a tuple containing five colors and print all elements.
tuple1 = ('red', 'blue', 'green', 'yellow', 'purple')
for color in tuple1:
    print(color)
# 22. Write a Python program to access individual elements of a tuple using indexing.
tuple1 = ('red', 'blue', 'green', 'yellow', 'purple')
print(tuple1[0])  # Accessing the first element
print(tuple1[2])  # Accessing the third element
print(tuple1[-1])  # Accessing the last element
# 23. Write a Python program to loop through all values in a tuple using a for loop.
tuple1 = ('red', 'blue', 'green', 'yellow', 'purple')
for color in tuple1:
    print(color)
# 24. Write a Python program to demonstrate tuple immutability by attempting to modify a tuple element.
tuple1 = ('red', 'blue', 'green', 'yellow', 'purple')

try:
    tuple1[1] = 'brown'
except TypeError:
    print("Tuples are immutable and cannot be modified.")
 
# 25. Write a Python program to create a new tuple by rewriting an existing tuple with additional elements.
tuple1 = ('red', 'blue', 'green', 'yellow', 'purple')

tuple2 = tuple1 + ('green', 'white')

print(tuple2)
