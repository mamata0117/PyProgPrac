# 3. WAP to print following series
# 1 4 9 16 25 36 49 64 81 100
for i in range(1,11):
    print(i*i,end=' ')
print()    
# 1/1 2/4 3/9 4/16 5/25 6/36 7/49 8/64 9/81 10/100
for i in range(1,11):
    print(f'{i}/{i*i}',end=" ")
print()
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
for i in range(1,11):
    if i<10:
     print(i,end=' + ')
    else:
        print(i)
#enter a  num and print its individual digits on sepr line
n=input('Enter a num:')        
for i in n:
   print(i)