
###############EXAMPLE 4: Inputs #################
#input() function waits for an input from the keyboard
salutation = "Hello"
name = input("Tell me your name: ")
complete_salut = salutation + ', ' + name + '!'
print (complete_salut)

weight = input("Enter your weight in lb: ")
weight = int(weight) #what am I doing here???
weight_kg = weight/2.205
print (weight_kg)

###############EXAMPLE 5: Conditionals #################
if (x > y):
   print ("x is greater than y")
elif (y < x):
   print ("y is greater than x")
else:
   print ("they are equal!")

###############EXAMPLE 6: Functions #################
def BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def convert_lb_to_kg (weight_lb):
    weight_kg = weight_lb/2.205
    return weight_kg

def convert_ft_in_to_m(feet, inches):
    meters = feet*0.305 + inches*0.0254
    return meters

print (BMI(convert_lb_to_kg(210),convert_ft_in_to_m(6,0)))


###############EXAMPLE 7: Lists #################
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


