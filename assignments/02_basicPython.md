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

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

For example:

```
>>> list_mangler([1, 2, 3, 4])
[3, 4, 9, 8]
```

Present a short (no more than a couple of sentences) description of your solution approach. Show your source code and the output of three example runs.

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
>>> grade_calc([100, 90, 80, 95], 2)
'A'
```

Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the  output of three example runs.

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
