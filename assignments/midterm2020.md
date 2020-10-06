## MIDTERM

**You are expected to work on these exercises with your group**

**Date:** The midterm will start on Tuesday (Oct 6) and needs to be turned in by Thursday (Oct 8) 11:59 PM. 

**How to submit:** One member of the group needs to create a notebook on their repository called `midterm.ipynb` (by the deadline) with the following structure:
 - The first cell needs to be a Markdown cell with ***the names of the students in the group*** followed by the exercises.
 - For some items below, you can choose a subset of the exercises to solve. 
 - For each item the first cell must be a markdown cell, with the header of the item and the choices
   - For each chosen exercise, please explain the solution and the rationale before presenting the text. 
   - If you solve more exercises than what was requested, I will only grade the first one(s).


*Enjoy! Here are the items:*

**0. I Expect you to treat AT LEAST one exception per exercise. This will account for 10% of the grade**

**1. Choose two of the following (10% - 5% each) - BASIC**

a. Write a program that asks the user to type an integer and outputs the number with the digits reversed. (for the input 12689, the output is 98621).

b. Write a program to calculate the following series, given the “n” input by the user. 
 <br/>![img](images/clip_image002.png)

 c. Write a function that tests whether a string is a palindrome or not. 

**2.**  **Choose one of the following (10%) – LOOPS 2** 

a. Ask the user to enter 5 integer values between 1 and 20. Create a horizontal bar graph (with the numbers entered by the user), using “*” to represent the value. For example, the user enters: 6, 9, 12, 1, 15:

The output is:

```
* * * * * *
* * * * * *
* * * * * * * * *
* * * * * * * * * * * *
*
* * * * * * * * * * * * * * *
```



b. Ask the user to enter 2 positive integer values (between 1 and 9) that will represent the position of a point and plot in a plane. The first value is the position in X, and the second in the Y axes. Each line of the output (screen) is one unit and each position in a line is one unit. Make sure that you show the axes (with | and _ )

For the inputs 7, 4,The output should be like this:
```
9|
8|
7|
6|
5|
4|...X
3|   .
2|   .
1|   .
  _________ `
  123456789
```

**3.**   **Pick three of these (24% - 8% each) - LISTS**

a. Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2] (the ones at the end, will move to the beginning). DO NOT USE A COPY OF THE LIST.

b. Write a function that, given a list, print all the elements that are repeated.

c. Write an algorithm that, given 2 lists containing integers only, present what are the values that appear in both of them.

d. Write a program that returns the nth smallest and the nth largest numbers in a list. “n” needs to be input by the user. 

e. Write a Python program to convert a list of positive integers into one integer, by merging them. Example: input: [4,12,43,10], output: 4124310

f. Write a function that receives a list of lists and returns a single ranked list with unique numbers (no repetitions). Examples:

* Input: ```[[1,4,5,7], [2,16], [4,8,9,1], [4,7,9]```  output: ```[1, 2, 4, 5, 7, 8, 9, 16]]``` 

* Input: ```[2, 10], [1, 7, 10], [1], [10, 2]]``` output: ```[1, 2, 7, 10]```

 

**4.**   **Pick 1 of the following (15%) – DICTIONARIES** 

a. Wikipedia has a list of the tallest mountains in the world [1] , with each mountain's elevation. Pick five mountains from this list.

   * Create a dictionary with the mountain names as keys, and the elevations as values.
   * Create a function that receives the dictionary as a parameter and prints out just the mountains' names and elevations, as a series of statements telling how tall each mountain is: *"Everest is 8848 m tall."*
   * Create a function that receives the dictionary and the name of a mountain, and removes it (please treat the exception triggered when a mountain is not found)
   * Create a function to list the top 2 mountains
<br>[1] https://en.wikipedia.org/wiki/List_of_highest_mountains_on_Earth

 

b. Given the dictionary below, create a program with the following 3 functions:
* add a new country to the dictionary, using the same structure
* add a new key to the ALL entries called ‘currency’ and all of them with “N/A"
* find the country with the largest population

```python
countries = {
  'USA':{
    'population': 328000000,
    'first language': 'English',
    'continent': 'North America',
  }
}
```
**5.**   **Pick 1 of the following (8%) – FILES** 

a. Write a program to delete a specific line (input by the users) from a file. 
Assume that the content of the file test.txt is : 
```
line 1 
line 2
line 3 
line 4 
```

If the user inputs 3, file.txt should have the following lines after running the program
```
line 1 
line 2
line 4 
```
 
b. Write a program to merge the content of two files and into a new third file.

**6.**   **Pick 1 of the following (10%) – FILES2**

a. Knowing that the first line of a csv file is the header, create a dictionary from this file considering that each row needs to be a nested dictionary, and the key of each of them is the number of the line. You need to write this dictionary to a .txt file.

For the sample file:
```
name, address, phone, dob
Peter, 17 Cherry Tree lane, 555-222-1111, Oct-12-1830
Jenny, 123 Slumber St., 555-102-9283, Sept-9-1845
Dante, 60 Araucaria Drive, 322-456-2020, Mar-15-1811
```
The dictionary should be:
```python
dictio= {
  1: {'name': 'Peter',
     'address': '17 Cherry Tree lane',
     'phone': ' 555-222-1111',
     'dob': 'Oct-12-1830'},
  2: {'name': 'Jenny',
     'address': '123 Slumber St.',
     'phone': '555-102-9283',
     'dob': 'Sept-9-1845'},
  3: {'name': 'Dante',
     'address': '60 Araucaria Drive',
     'phone': '322-456-2020',
     'dob': 'Mar-15-1811'}
}
```

b. Write a Python program that reads one csv file and creates a new csv file removing the first and last ‘columns’.

For the sample input:
```
name, address, phone, dob
Peter, 17 Cherry Tree lane, 555-222-1111, Oct-12-1830
Jenny, 123 Slumber St., 555-102-9283, Sept-9-1845
Dante, 60 Araucaria Drive, 322-456-2020, Mar-15-1811
```
The output should be:
```
address, phone, dob
17 Cherry Tree lane, 555-222-1111
123 Slumber St., 555-102-9283
60 Araucaria Drive, 322-456-2020
```

**7.**   **Mandatory exercise (13%):**

Please consider this CSV file [ant_species.csv](https://github.com/igorsteinmacher/INF502-Fall2020/blob/master/notebooks/ant_species.csv) This data is part of the [census of the ant community](https://github.com/weecology/PortalData/tree/master/Ants) occurred every year (1977-2009) over a two week period during July after the summer monsoons have begun. You are required to:

* map the CSV structure to a class in Python
* provide with a constructor method receiving all the attributes as parameter
* create a method that enables someone to print the objects
  - "genus species" (e.g., Camponotus festinatus)
* create a function (outside of the class, which will call the constructor) that receives the file and creates objects for each row of the file
