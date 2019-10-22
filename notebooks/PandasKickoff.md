## Exploring data using Pandas

![image.png](attachment:image.png)

So far we explored Python and a few native libraries. Now we will play a little to simplify our life with tools to conduct some **data analysis**.

**Pandas** is the most popular library (so far) to import and handle data in Python.

### Let's import some data from a CSV file


```python
import pandas
cpr = pandas.read_csv("commits_pr.csv")
```

It became this easy to read a CSV file!!!
And more... Look at what my `cpr` is:


```python
type(cpr)
```

Yes! A DataFrame. And it reads really nice, look:


```python
cpr
### We can use head() and tail() functions to see a bit less
```

Before moving forward... Explaining a little about this dataset.

This dataset represents a series of Pull Requests made to a subset of projects hosted by GitHub. We worked on this data to capture a specific type of contributor, which we called *casual contributor*. These contributors are known by having a single pull request accepted in a project and not coming back (i.e., they have no long-term commitment to the project).

In this specific dataset, you will find the following columns:

* `user`: represent a user in GitHub (anonymized here)
* `project_name`: the name of GitHub project in which the pull request was accepted
* `prog_lang`: programming language of the project
* `pull_req_num`: unique identifier of the pull request
* `num_commits`: number of commits sent within that specific pull request



### Some information about the dataframe

Dimensions/shape of the dataset (lines vs. columns)


```python
cpr.shape
```

What about the column names?


```python
cpr.columns
```

And the datatype per column?


```python
cpr.dtypes
```

Some more information: `info()` method prints information including the index dtype and column dtypes, non-null values and memory usage.


```python
cpr.info()
```

What is the type of a specific column???


```python
type(cpr["num_commits"])
```

A *serie* is a list, with one dimension, indexed. Each column of a dataframe is a series

Before moving ahead, we can use the types to filter some columns. 

Let's say we want only the columns that store `int`:


```python
int_columns = cpr.dtypes[cpr.dtypes == "int64"].index
int_columns
```

Now... I just want to see these columns... **BOOM**


```python
cpr[int_columns].head()
```

### What about statistical information about my DataFrame?

`describe()` method provides a summary of numeric values in your dataset: mean, standard deviation, minimum, maximum, 1st quartile, 2nd quartile (median), 3rd quartile of the columns with numeric values. It also counts the number of variables in the dataset (are there missing variables?)


```python
cpr.describe()
```

We can do it for a Series...


```python
cpr["num_commits"].describe
```


```python
#LOOK at this with a non-numeric column
cpr.prog_lang.describe() #either way work.
```

And we can get specific information per column


```python
cpr.num_commits.median()
```


```python
cpr.num_commits.mean()
```


```python
cpr.num_commits.std()
```

### --------------####
### Playing with the data: sorting

We can sort our data easily using pandas.

In this example, sorting by Programming Language


```python
cpr.sort_values("num_commits", ascending=False).head(10)
```

We can sort using *many columns*, by using a list (sort will happen from the first item to the last)


```python
cpr.sort_values(["prog_lang", "project_name", "num_commits"], ascending=False).head(10)
```


```python
cpr.head(10)
```

If you want to keep the sorted version, you can use the parameter `inplace`:


```python
cpr.sort_values(["prog_lang", "project_name", "num_commits"], ascending=False, inplace=True)
```


```python
cpr.head(10)
#cpr = pandas.read_csv("commits_pr.csv") #--> to return to the original order
```

### Counting the occurences of variables

So, to count the occurrences in a column we have to select the column first, and use the method `value_counts()`


```python
cpr.prog_lang.value_counts()
```

But... I just want to know what are the languages out there. Is there a way?

*Always*


```python
cpr["prog_lang"].unique()
```


```python

```

## OK! Let's do something else... Like, selecting columns and filtering data

Let's say that I just want to look at the columns programming language, project name and number of commits. 

I can select them and create a new DF


```python
selected_columns = ["prog_lang", "project_name", "num_commits"]
my_subset = cpr[selected_columns]
my_subset.head()
```

What if now I want to filter those projects written in `C` language?


```python
only_C = cpr[cpr["prog_lang"]=='C']
only_C.describe()
```

We can filter whatever we want:


```python
single_commit = cpr[cpr["num_commits"] == 1]
```

We can create filters in variables, and use whenever we want, as well


```python
one_commit = cpr["num_commits"]==1
language_C = cpr["prog_lang"]=="C"
multi_commit = cpr["num_commits"]==1
```


```python
cpr[one_commit].head(10)
```

And... we can use OR (|) and AND(&) to play!


```python
cpr[one_commit & language_C].head(10)
```

#### What if we want the pull requests with more than one commit for the projects written in "C" and those with 2 commits for the projects written in "typescript"???

Let's do it!



```python
#####











```

What if I wanted to convert number of commits into a feature by creating bands of values that we define:
* 1 commit = group 1
* 2 - 5 commits = group 2
* 6 - 20 commits = group 3
* > 20 = group 4


```python
cpr.loc[one_commit, "group_commit"] = 1
# ...
```


```python
cpr.describe()
```

### I challenge you:

What if: I wanted to know how the average of num_commits for those pull requests in group_commit 4???


```python





```

### I challenge you (2):

Can you do that average per language?



```python

```














### Some more... 


```python
cpr[cpr["prog_lang"] == "typescript"].quantile(0.75)
```


```python
for lang in cpr["prog_lang"].unique():
    print("Language %s: \t%0.3f"%(lang, cpr[cpr["prog_lang"]==lang]["num_commits"].median()))
```

### Can we play with graphics?


```python

```
