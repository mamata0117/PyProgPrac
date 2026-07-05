#funcn with parameter and returns value
print('Avg of three nums')
#funcn defn
def avg_num(a,b,c):
  sum=a+b+c
  avg=sum/3
  print(avg)
  return(avg)
#funcn call
avg_num(3,9,1)
#funcn without para or return
def print_hi():
  print('HI')
#funcn call
print_hi()  
print_hi() 
#since it doesnt return value o/p is NONE 
out=print_hi()
print(out)
  #1
def greet(name):
    print('Hello',name)
    print('Hi'+' '+name)
greet('Mamata')   
#2
def my_fun(fname,lname):
      print(fname+" "+lname)
my_fun('Patrick','Jane')
my_fun(input('First name:'),input('Last name:'))      