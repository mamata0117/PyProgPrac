#  Write a Python program to check login credentials using username and
# password with nested conditions
username=input("enter username:")
psw=input("enter psw:")
if username=='admin':
    if psw=='8888':
      print('Login succesfully')
    else:
         print('Incorrect psw')
else:
    print("invalid username")         