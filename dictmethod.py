laptop={
    'brand': 'Dell',
    'model': 'XPS 13',
    'price': 999.99
}
#using the get() method to access values in the dictionary
print(laptop.get('brand'))
print(laptop.get('model'))
print(laptop.get('price'))
dict={ }
age=dict.fromkeys(['age','name','city'],0)
print(age)
#fromkeys() method is used to create a new dictionary with specified keys and a default value. In this case, the keys are 'age', 'name', and 'city', and the default value is 0. The resulting dictionary will look like this: {'age': 0, 'name': 0, 'city': 0}.