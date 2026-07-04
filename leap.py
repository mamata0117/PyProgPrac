# year=int(input("Enter a year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")  
# 1qn  
# length=int(input('Enter length:')) 
# breadth=int(input('Enter breadth:'))
# area=length*breadth
# print('The area of rec is',area)
# 2qn
list1=[1,2,3,4,5]
print('max item:',max(list1))
print('min item:',min(list1))
#sum using built-in function
print('sum is',sum(list1))

#sum and multiplication without using built-in function
sum=0
mul=1
for num in list1:
    sum+=num
    mul*=num
print('sum:',sum)    
print('mul:',mul)    
#finding max and min in a list without using built-in functions
list1=[1,2,3,4,5]
maximum=list1[0]
minimum=list1[0]
for num in list1:
    if num>maximum:
        maximum=num
    if num<minimum:
        minimum=num
print('max is:',maximum)            
print('min is:',minimum)            