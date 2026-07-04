thisdict={
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
#showing the dictionary
print(thisdict)
#showing key el only and value only
print(thisdict.keys())
print(thisdict.values())
#showing key and value both
print(thisdict.items())

#2
car={
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
#adding new key value pair
car['color']='red'
car.update({'price':'50k$'})
car.update({'fuel':'petrol','engine':'hybrid'})
print(car)
#removing using pop(),popitem() and del  and clear()
car.pop('color')
print(car)
# using popitem() method
car.popitem()  #removes last item
print(car)
# using del keyword
del car['year']
print(car)
# del car  #deletes entire dictionary
# print(car)  #this will give error because dictionary is deleted
#using clear() method
car.clear()
print(car)
#3
house={
    'type':'bungalow',
    'rooms': 4,
    'location':'city center'

}
#copying dictionary using copy() method and dict() constructor
house_copy=house.copy()
print(house_copy)
new_house=dict(house)
print(new_house)