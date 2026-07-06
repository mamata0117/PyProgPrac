# #pattern1
for i in range(1,6):
    print('*'*i)
# #pattern2    
# for i in range(1,6):
#     print('*'*5)
# #pattern3   
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()     
# #pattern4
# for i in range(1,6):
#     print(str(i)*i)       
# #pattern5
# for i in range(1,6):
#     print(str(i)*(6-i))       
#pattern6
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end='')
        num+=1
    print()    
