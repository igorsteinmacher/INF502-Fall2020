list_of_numbers = [1,2,3,4,5]
len(list_of_numbers)
list_of_numbers[0]
print(list_of_numbers)
list_of_numbers[4]
print(list_of_numbers)
list_of_numbers[-2]
print(list_of_numbers)

#extending it
list_of_numbers.extend([6,7,8])
print(list_of_numbers)
#slicing it
piece = list_of_numbers[:4] #beginning to 4
print (piece)
piece = list_of_numbers[2:6] #from position 2 to 6
print (piece)

#shrinking it
del list_of_numbers [2:5]
print(list_of_numbers)

#merging
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)

#sorting
list1 = [-1,4,0,9,2,7]
list1.sort()
print (list1)