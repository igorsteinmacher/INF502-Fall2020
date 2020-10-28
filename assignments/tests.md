## In Class Assignment!!!

**How to Turn In:** Create a Python Notebook on your repository named InClassOct20.ipynb

*1 notebook per group is enough. Remember to add the name of all students in the group to your Notebook*

**Deadline:** Oct-20

Please, create unittests for the calculator code below. When a test case fails, please fix the code. 

Your deliverable (notebook) must show the evolution of the code (code with error --> test case failing --> code adjusted --> test case passing)

```python
class Calculator: 
   def add(x, y):
      return x + y 

   def subtract(x, y): 
      return x - y 

   def multiply(x, y): 
      return x * y 

   def divide(x, y): 
      return x / y

   def pow(x, y):
      res = 1
      for i in range(2,y):
         res = res*i
```
