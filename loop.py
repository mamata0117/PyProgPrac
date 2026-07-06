 # Program Questions

# 1. Write a Python program to print numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i,end=' ')
    i+=1
print()
# 2. Write a Python program to calculate the sum of first n natural numbers using a for loop.
n=int(input('Enter n:'))
total=0
for i in range(1,n+1):
    total+=i
print(total) 
print()


# 3. Write a Python program to display the multiplication table of a number using a while loop.
n=int(input('ENTER N:'))
i=1
while i<=10:
    print(i*n)  
    i+=1
print()

# 4. Write a Python program to print all even numbers between 1 and 100 using a for loop.
for i in range(2,101,2):
    print(i,end='')
for i in range(1,101):
   if i%2==0:
      print(i,end=' ')   
print()

# 5. Write a Python program to simulate a do-while loop for password checking until the correct password is entered.
crt_psw='py1'
while True:
   psw=input('Enter psw:')
   if crt_psw==psw:
      print('access granted')
      break
   else:
      print('access not  granted')

# 6. Write a Python program to find the factorial of a number using a while loop.
i=1
fac=1
n=int(input('Enter n:'))
while i<=n:
    fac*=i
    i=i+1
print(fac)

# 7. Write a Python program to iterate through a list of student names using a foreach style loop (for item in list).
list1=['ram','sita','hari']
for st in list1:
   print(st)

# 8. Write a Python program to print numbers from 1 to 20 but stop when the number 15 is encountered using the break statement.
for i in range(1,21):
   if i==15:
      break
   print(i)
# 9. Write a Python program to print numbers from 1 to 20 but skip multiples of 3 using the continue statement.
for i in range(1,21):
   if i%3==0:
      continue
   print(i)

# 10. Write a Python program to search for a number in a list and terminate the loop when the number is found using break.
n=int(input('Enter the num to search:'))
list1=[1,2,4,5,6,7]
for num in list1:
   if num==n:
      print(num,'found at index',list1.index(num))
      break
# 11. Write a Python program to demonstrate the use of the pass statement inside an empty loop or conditional block.
for i in range(5):
   pass 
print('pass statement executed')

# 12. Write a Python program to print a pyramid pattern using nested for loops.

# 13. Write a Python program to count the number of digits in a number using a while loop.
num=1234
count=0
while num>0:
    num=num//10
    count+=1
print(count)    
# 
# 14. Write a Python program to reverse a number using a while loop.
n=int(input('enter n:'))
rev=0
org=n
while n!=0:
   temp=n%10
   rev=rev*10+temp
   n=n//10
print(rev)     
# 15. Write a Python program to print all prime numbers between 1 and 100 using nested loops.
for num in range(2,101):
  for i in range(2,num):
    if num%i==0:
       break
  else:
     print(num)

# n=int(input('enter n:'))
# if n<=1:
#     print('np')
# else:
#     prime=True
#     for i in range(2,n):
#         if n%i==0:
#             prime=False
#             break
#     if prime:
#         print('p')
#     else:
#         print('np')        
#2
# n=int(input('enter n:'))
# if n<=1:
#     print('np')
# else:

#     for i in range(2,n):
#         if n%i==0:
#             print('notp')
#             break
#     else:
#         print('prime')        
# 16. Write a Python program to display the Fibonacci series up to n terms using a for loop.
n=int(input('range for fibonacci:'))
a=0
b=1
for i in range(1,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    
# 17. Write a Python program to continuously ask the user for numbers and stop only when the user enters 0 using a loop and break.
num=int(input('Enter num:'))
while num!=0:
    num=int(input('Enter num:'))
    

# 18. Write a Python program to print all characters of a string except vowels using a for loop and continue statement.
string=input('enter string:').lower()
for char in string:
    if char in 'aeiou':
        continue
    print(char,end=' ')

# 19. Write a Python program to check whether a number is a palindrome using a while loop.
num=input('Enter num:')
if num==num[::-1]:
    print('palindrome')
else:    
    print('not palindrome')

# 20. Write a Python program to print numbers from 1 to 50, skipping numbers divisible by both 2 and 5 using the continue statement.
for i in range(1,51):
    if i%2==0 and i%5==0:
        continue
    print(i)
