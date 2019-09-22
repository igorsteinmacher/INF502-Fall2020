# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###### 1 
def pythagoreanTheorem(a, b):
    return((a**2 + b**2)**(1/2))
  
loop = True
# length_a = length_b = 2
while loop is True:
    length_a = input('Input side A: ')
    length_b = input('Input side B: ')
    try:
        print("Your input: a)", length_a, " - b)", length_b)
        print("Pythagorean Theorem is:", pythagoreanTheorem(float(length_a), float(length_b)))
        break
    except:
        print("Please make sure a & b are numbers!")


pythagoreanTheorem(2, 2)
pythagoreanTheorem(3, 3)
pythagoreanTheorem(4, 4)
###### 2
def list_mangler(list_in):
    res = [i * (2 + (i % 2 )) for i in list_in]
    #res = list(map(str.lower, test_list)) 
    return(res)

list_mangler([1, 2, 3, 4])
list_mangler([5, 6, 7, 8])
list_mangler([1, 2, 1, 2])

###### 3
from itertools import compress
Lett = ['A', 'B', 'C', 'D', 'F']
score = [90, 80, 70, 60, 0]

def grade_calc(grades_in, to_drop):
     gradesAv = sorted(grades_in)[to_drop:len(grades_in)]
     av = sum(gradesAv)/len(gradesAv)
     return(list(compress(Lett, [av >= i for i in score]))[0])
     

grade_calc([100, 90, 80, 95, 70], 2)
grade_calc([90, 80, 95, 70, 60], 1)
grade_calc([60, 80, 65, 65, 60], 1)

###### 4
from itertools import compress
def odd_even_filter(numbers):
    even = [(i % 2 ) == 0 for i in numbers]    
    ans = []
    ans.append( list(compress(numbers, even)) )
    ans.append( list(compress(numbers, [not i for i in even])) )
    return(ans)
    
odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_even_filter([3, 9, 43, 7])
odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])

odd_even_filter([1, 3, 5, 7, 2, 4, 6, 8])
odd_even_filter([10, 12, 14, 16, 11, 13, 15, 17])
odd_even_filter([1, 2, 1, 2, 1001, 1002])



