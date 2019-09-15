student = {'name':'John','age':25,'courses':['Math','CompSci']}

print(student)

print(student['courses'])

#print(student['phone']) #error because the key doesn't exist

print(student.get('name'))

print(student.get('phone','Not Found'))
#print(student.get(25))

#adding a new key
student['phone'] = '555-555-5555'
print(student)

#updating multiple key values
student.update({'name':'Jane','age':'23'})
print(student)

#deleting a specific key value
del student['age']
print(student)

#returning the number of key elements
print(len(student))

#returning the Keys
print(student.keys())

#returning the values
print(student.values())

#returning the key_values items
print(student.items())

#adding new keys
student = {'name':'Igor','age':30,'courses':['Math','CompSci']}

print(student)

#loop
for key in student:
    print(key)

#printing the items and values
for key,value in student.items():
    print(key,value)

