# . Write a Python program to display the grade of a student based on marks:
# 90 and above → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → F
grade=int(input("Enter your grade:"))
if grade>=90 :
    print('A')
elif grade>=80 and grade<=89:
    print('B')    
elif grade>=70 and grade<=79:
    print('C')    
elif grade>=60 and grade<=69:
    print('D')   
else:
       print('F')    
