# Git/GitHub Assignment

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-9th 11:59PM
* **How to submit**: For each empty grey box, please provide with an answer to the item in a document. Do the following to *submit* the **Part 1** of your assignment:
1. Create a new repository under your GitHub account called *INF502*; 
2. create a file called *"Assignment1.md"* and paste your answers there (tip: click on *"Raw"* at the right-top of this file to get the markdown source); 
3. invite me to see your new repository. This will allow you to keep a private repository that 

For **Part 2** the pull request created will the submission (except for item 4, which you need to add to the end of the Assignemnt1.md).

* **Value**: Part of homework grade

## Description
This assignment is composed of two parts. 
- [Part 1](#Part-1-Dealing-with-git) consists of executing a sequence of commands and giving explanations about the commands you have to run. 
For each item in the assignment, please provide appropriate explanation and/or the details requested.
- [Part 2](#Part-2-Using-GitHub) consists of creating a Markdown file on a fork of this course and creating a pull request towards this repo.

### Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it.
handson folder is a git repository. Using the command line change the directory to "handson/"

The empty boxes
```
cd ./handson
```
represent the content you need to fill and post on your private repository


1. Draw a diagram of the commits and branches in repository.

- Use `git branch` to list the branches in this repository.
- Use `git checkout` to explore each branch.
- Use `git log --decorate` to explore the structure of commits.

```
> git branch
*master
 handson

> git checkout
Switched to branch ´handson'

> git log --decorate
Can't copy:
First commits. The creation of readmeMD file, and the assignment MD
70 messages or more
```

2. Try `git log --graph --all` to see the commit tree. What do you see?
```
The tree with changes, and adition of A.py

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
Summarize the difference from master to the other branch.

```
Supouse tu have de A.py and B.py. Nothing results

```

4. Write a command sequence to merge the non-master branch into `master`

```
git checkout master
git merge handson

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) 
and (ii) change to this branch

```
git checkout master
git branch math
git checkout math

```

6. Edit B.py adding the following source code below the content you have there
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes
```
git add B.py
git commit -m "add two lines in B.py on handson branch"
```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened
```
git checkout master
git add B.py
git commit -m "add one lines in B.py on master branch"
git merge handson
```

10. Write a set of commands to abort the merge
```
git merge --abort
```

11. Now repeat item 10, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure
```
No files copied :(
Don't see errors 

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```
git checkout master
git merge handson
git rebase

```

### Part 2: Using GitHub

The goal of this assignment is to put you in touch with the fork-pullrequest process, with an extra of dealing a little bit with Markdown. To learn more about Markdown [click here](https://guides.github.com/features/mastering-markdown/).

**You must fork this repo and submit a pull request back**

1. Into the students folder, create a file called LASTNAME_FIRSTNAME.md (please change LASTNAME_FIRSTNAME for your actual last and first names). 
2. Use Markdown to structure the following information about the last paper you've read (you can structure your markdown the way you want):
- Title
- Venue (journal name/conference)
- Number of pages
- 3 outcomes of the paper
- link to the paper online

3. Send your file back to this repository until creating a pull request (your pull request needs to appear [here](https://github.com/igorsteinmacher/CS502-Fall2019/pulls)).

4. Report your experience of making this submission, including the steps followed, commands used, and hurdles faced (within the file you created for the **Part 1**.
```


```