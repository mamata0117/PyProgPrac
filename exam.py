# waqp to take num input from user and print its ind digit on sepr line
n=int(input("Enter a number: "))
while n!=0:
    digit=n%10
    print(digit)
    n=n//10
#max value and min value in dict
dict={ 
    'a':10,
    'b':50,
    'c':4
}
for key,value in dict.items():
    print(key,":",max(dict.value))
    print(key,":",min(dict.value))
    #check whether given key already exist in a dict
dict2={
    'name':'ram',
    "age":29,
    'height':'180cm'
}    
key1=input("enter key u want to search:").lower()
for key in dict2:
    if(key1==key):
        print('exist')
        break
else:
    print('doesnt exist')    