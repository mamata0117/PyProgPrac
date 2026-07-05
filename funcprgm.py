'''#1 waf to print length of a list
def list_len(list1):
  a=len(list1)
  print(a)
  return(a)
list_len([3,4,5,6])
#1.1
color=['red','blue','pink']
def lencolor(lists):
  print('Length is:',len(lists))
lencolor(color)  
#2waf to print el of list in a single line
alpha=['a','4','b','o']
def sing_line(lista):
   for i in lista:
     print(i,end=' ')
    
sing_line(alpha)   
print()
#3waf to find fact of n
def fact_n(n1):
  fact=1
  for i in range(1,n1+1):
    fact=fact*i
  print(f'factorial of {n1} is {fact}')
a=int(input('Enter n:'))
fact_n(a)
fact_n(5)
# usd to npr 1$=118rs
#without return
def convert(usd):
  neprs=usd*118
  print(f'{usd} usd is {neprs}NPR')
convert (6) 
#with return
def convert(usd):
  neprs=usd*118
  return(neprs)
a=convert(8)
print(a)'''
#funcn for odd even
def num(n):
  if n%2==0:
    print(f'{n} is even')
  else:
    print(f'{n} is odd')
num(9)    
num(90)    