# Git/GitHub Assignment

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: XXXXX
* **How to submit**: BBLearn
* **Value**: Part of homework grade

## Description
This assignment is composed of two parts. 
- [Part 1](#Part-1-Dealing-with-git) consists of executing a sequence of commands and giving explanations about the commands you have to run. 
For each item in the assignment, please provide appropriate explanation and/or the details requested.
- Part 2

### Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it.
handson folder is a git repository. Using the commandline change the directory to "handson/"


1. Draw a diagram of the commits and branches in repository.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```


```

2. Try `git log --graph --all` to see the commit tree. What do you see?
```


```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   Summarize the difference from master to the other branch.

```


```

4. Write a command sequence to merge the non-master branch into `master`

```


```


5. Write a command (or sequence) to (i) create a new branch called `feature-bar` (from the `master`) 
and (ii) change to this branch

```


```
   
6. Edit B.py adding the following source code below the content you have there
```code
print 'hello world!'
```

7. Write a command (or sequence) to commit your changes
```


```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'I know math, look:'
print 2+2
```

9. Write a command sequence to merge the `feature-bar` branch into `master` and describe what happened
```


```
   
10. Write a set of commands to abort the merge
```


```
   
11. Now repeat item 10, but proceed with the manual merge (Editing B.java). All implemented methods are needed. Explain your procedure
```


```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```


```

