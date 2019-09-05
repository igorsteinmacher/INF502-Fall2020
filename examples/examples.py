###############EXAMPLE 1 #################
x = 2       #x is an integer
type (x)

y = 'Igor' #y is a String
type (y)
y = 2.5     #y is now a floating point
type (y)

z = [1,2,3] #z is a list
#each position in z is an integer
type (z)

x = y = z = 4 #chained assignment

print("this is x: ", x)
print("this is y: ", y)
print("this is z: ", z)

###############EXAMPLE 2#################

a = 2+3    #a is 5
print("a: ", a)
b = 7-4    #b is 3
print("b: ", a)
c = 2*2.5  #c is 5.0 (float!!)
print("c: ", a)
d = 2**4.  #d is 16
print("d: ", d)
e = 5%2    #e is 1
print("e: ", e)
f = 7/2    #f is 3.5
print("f: ", f)
g = 7//2   #g is ...
print("g: ", g)

###############EXAMPLE 3: Strings #################
single_quote = 'python'
double_quote = "python"
I_want_the_quote = 'It\'s python'
yes_the_quote = "It's python"
multi_line = 'this is a multi line \
sentence. It is possible to break it in \
multiple lines.’

#operations using strings
salutation = "Hello"
name = "John"
complete_salut = salutation + ', ' + name + '!'
print (complete_salut)

real_long_string = ('this is a long string. '
'It has multiple parts, '
'but all in one line.‘)


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


