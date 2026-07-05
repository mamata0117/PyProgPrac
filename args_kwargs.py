#args
def sum_num(*args):
  a=sum(args)
  return(a)
print(sum_num(3,7,8,9,1,2))
#without sum
def sum_num(*num):
  total=0
  for i in num:
   total+=i
  return(total)  
print(sum_num(3,7,8,9,1,2,3))
#example of kwargs
def student_info(**info):
  for key,value in info.items():
    print(key,':',value)    
student_info(name='ram',age=21,grade='A')    
#accessing specific values
def myfunc(**kwargs):
  print("Name:",kwargs['name'])
  print("age:",kwargs['age'])
myfunc(name='rita',age=23)  
#percentage of marks
def sub(**marks):
  total=sum(marks.values())
  subjects=len(marks)
  return(total / subjects)
result=sub(math=99,eng=95,phy=94)
print(result)