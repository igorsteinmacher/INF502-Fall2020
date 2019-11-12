## Divide and conquer assignment

* **Individual Assignment**
* **Due:** Nov 21
* **Filename convention:** HW7.ipynb 


Two positive integers always have common factors. For example, the common factors 12 and 18 are 1, 2, 3, and 6, 
because we 12 and 18 are divisible by these numbers. 
The greatest common factor (GCF) of a number is the largest number by which both numbers are divisible. 
In the example, the number 6 is the GFC of 12 and 18.

There are at least two methods for calculating GDF of two numbers. 
One is the method of successive divisions. 
In this process we make several divisions until we reach an exact division. 
The divisor of this division is the GDF. For example, for the 48 and 30 we have:

Practical rule:
  1) we divide the largest number by the smallest number:
   48/30 = 1 (with remainder of 18)
  2) we divide 30 (the divisor of the previous division) by 18 (the rest of the previous division) and so on:
   - 30/18 = 1 (with remainder of 12)
   - 18/12 = 1 (with remainder of 6)
   - 12/6 = 2 (exact division)
3) The divisor of the exact division is 6. So the GDF of 48 and 30 is 6.

Implement a "divide and conquer" algorithm that solves the GDF problem for any two positive integers A and B.

You must implement a function called GDF(a,b): `def GDF(a,b):`


Provide the solution and an explanation of your solution in a notebook
