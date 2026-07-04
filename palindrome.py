n=int(input('Enter a num:'))
original=n
rev=0
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print("palindrome")    
else:
      print(" not palindrome") 
#2nd way
n=input("Enter data")
if n==n[::-1]:
     print("palindrome")    
else:
      print(" not palindrome") 