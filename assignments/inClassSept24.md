# In-class assignment

### Groups
* 2 or 3 people
### How to turn in:
* The code need to be placed in the GitHub of one of the members
* The file should be called ```Inclass1.py``` in the root folder
* Make sure to have the names of the group members in the beginning of your script
### Other instructions
* Do not overthink
* Yes, there may be missing details, please call me for clarifications.

## Re-arranging the dataset

After downloading a dataset with information about a given population,
a researcher noticed that the data was not organized as she expected.

The researcher needed a single file containing the information about each
person, in a comma separated (CSV) format.

The dataset was composed of multiple text files, each of them presenting
one characteristic of the population that she needed to analyze. At least,
each the data corresponding to each person was in the same line in all
files (i.e., the information in line 1 in all files belong to the same person).

[Download the dataset here](data.zip)

Your job is to create a program that reads the files inside data folder
and write them in a single file, in CSV format. There is no requirement about
the order of the fields, just make sure that the order appear in the
first line of your CSV file.

**EXAMPLE OF OUTPUT**
```
name, phone, city, state, age
John, 212-555-2211, Phoenix, Arizona, 30
Peter, 212-555-1300, Sacramento, California, 24
Anna, 212-555-8382, Cleveland, Ohio, 33
```

What you need to do:
* breakdown! bottom up approach, thinking about the steps/functions you will need to compose your solution. Solve one problem, then move to the next.
* read from files
* keep contents in collections
* do some processing
* write in files
