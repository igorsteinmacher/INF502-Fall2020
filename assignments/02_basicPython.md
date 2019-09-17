# Assignment 2: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-19th 11:59PM
* **How to submit**: For each item, provide an answer as requested in the item (usually the source code + explanations + iteractive shell output)
  - In your GitHub repository called *INF502* (same used for the Assignment 1) create a file called *"Assignment2.md"* with your answers (I will allow the answer in PDF format for those who prefer, but I strongly encourage using Markdown.)
  Remember to invite me to see your new repository (if you did not for Assignment 1). 
  - I will evaluate the latest commit before 11:59PM (Sept-19th)

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

For example:
```
>>> pythagoreanTheorem(2, 2)
2.8284271247461903

```
Present your source code and the output of three example runs.

### Answer:

```
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
Out[2]: 2.8284271247461903

pythagoreanTheorem(3, 3)
Out[3]: 4.242640687119285

pythagoreanTheorem(4, 4)
Out[4]: 5.656854249492381
```

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

For example:

```
>>> list_mangler([1, 2, 3, 4])
[3, 4, 9, 8]
```

Present a short (no more than a couple of sentences) description of your solution approach. Show your source code and the output of three example runs.


### Answer:
This function iterate into each element and multiplies by 2. In the case the number is odd, a `True` (i.e. 1) return and can be summed to the 2 (resulting  a 3). In the case of the number is even, a `False` (i.e. 0), the multiplier still as 2.
```
def list_mangler(list_in):
    res = [i * (2 + (i % 2 )) for i in list_in]
    return(res)

list_in = [1, 2, 3, 4]
list_mangler(list_in)
Out[1]: [3, 4, 9, 8]

list_mangler([1, 2, 3, 4])
Out[2]: [3, 4, 9, 8]

list_mangler([5, 6, 7, 8])
Out[3]: [15, 12, 21, 16]

list_mangler([1, 2, 1, 2])
Out[5]: [3, 4, 3, 4]

```


**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
>>> grade_calc([100, 90, 80, 95], 2)
'A'
```

Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the output of three example runs.

### Answer:
A list with grade letters and cuttofs is created outside the function. The function order the list and extract the requiered lower number of elements. The remaining elements are averaged an this value is compared with the grades cuttofs. The first element from grade list bigger or equal than the average is returned.
```
from itertools import compress
Lett = ['A', 'B', 'C', 'D', 'F']
score = [90, 80, 70, 60, 0]

def grade_calc(grades_in, to_drop):
     gradesAv = sorted(grades_in)[to_drop:len(grades_in)]
     av = sum(gradesAv)/len(gradesAv)
     return(list(compress(Lett, [av >= i for i in score]))[0])
     

grade_calc([100, 90, 80, 95, 70], 2)
Out[1]: 'A'

grade_calc([90, 80, 95, 70, 60], 1)
Out[2]: 'B'

grade_calc([60, 80, 65, 65, 60], 1)
Out[3]: 'D'
```


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
>>> odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
>>> odd_even_filter([3, 9, 43, 7])
[[], [3, 9, 43, 7]]
>>> odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the interactive shell output of three example runs.

### Answer:
This function create a boolean vector that indicates if number is even or not. This vector is used to subset the original vector of numbers. After that, an empty list is created, and even and odd number list are appended into empty list.

```
from itertools import compress
def odd_even_filter(numbers):
    even = [(i % 2 ) == 0 for i in numbers]    
    ans = []
    ans.append( list(compress(numbers, even)) )
    ans.append( list(compress(numbers, [not i for i in even])) )
    return(ans)
    
odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
Out[1]: [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

odd_even_filter([3, 9, 43, 7])
Out[2]: [[], [3, 9, 43, 7]]

odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
Out[3]: [[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]



odd_even_filter([1, 3, 5, 7, 2, 4, 6, 8])
Out[4]: [[2, 4, 6, 8], [1, 3, 5, 7]]

odd_even_filter([10, 12, 14, 16, 11, 13, 15, 17])
Out[5]: [[10, 12, 14, 16], [11, 13, 15, 17]]

odd_even_filter([1, 2, 1, 2, 1001, 1002])
Out[6]: [[2, 2, 1002], [1, 1, 1001]]
```
