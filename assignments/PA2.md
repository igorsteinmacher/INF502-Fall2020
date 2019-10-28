# Programming Assignment 2

DUE DATE: DEC-5

You can arrange yourselves in groups of 2 or 3 students.

This assignment will give you some practice with writing complete applications that deal with data collection and analysis in Python structures.
The focus will be on using all the knowledge acquired in this course, from basic Python to Pandas, usign json, creating graphics, etc.

**IMPORTANT:** This assignment will evolve during the following weeks, after we learn other contents, and to count as your final.

I hope you enjoy this assignment.

## Context

We want to understand the context of GitHub. Analyzing projects and developers who contribute. 
Your application will have to consume the [GitHub REST API version 3](https://developer.github.com/v3/), 
to collect information about projects, pull requests, and users. 

Since we are interested in the social side of software development,  we will also scrape data from their GitHub profile.

The first requirement for this assignment is that you need to use object orientation to deal with the data you are collecting and analyzing.
The easy way to do is analyzing the structure of the `json` dictionary structure. When you have nested elements, a new object *may* be necessary.

So, about projects, we would like to keep the name, owner (login), description, homepage, license (can be another class), 
number of forks, watchers, and date_of_collection (the date you collect the data). When you request to print the object it should be like this:
* `Owner/ProjectName: Description (# of stars)`

Each project also needs to be related to a list of pull requests. Thus, for each project, collect the pull requests that 
are returned in the first page of a query like this:
* `https://api.github.com/search/issues?q=is:pr+repo:jabref/jabref` (using project jabref/jabref as an example)

For each pull request you need to keep: title, number, body, state, date of creation (created_at), 
closing date (if the state is different than open), user, number of commits, additions, deletions, changed_files. 

* For the last 4 fields, you will need to make another query using the following format (using the number of the pull requests
you found before):
* `https://api.github.com/repos/JabRef/jabref/pulls/5531`

Then, for each author (user) you find in the pull requests you need to keep: login, number of pull requests (calculated). 
Using the login, you are required to check if there is a 
and create a flag called has_a_twitter. You are also required to SCRAPE the following information from the user profile page on GitHub: 
Number of Repositories, Number of Projects, Number of Followers, Number of Following, Number of contributions in the last year.
**If you have repeated users, you only need to update the number of commits**


You need to have a function called `to_CSV` that can be reused to convert any object to a csv entry (row). 
You need to provide the file name and the object. If the file does not exist, you need to create the file (with the header). 
If the file  exists, you need to append a new line with the object in the CSV. To make it possible, you will need to have a method
in each of your classes with the very same name, which will return a string with the data already structured as a CSV.


Use this function to create/update the files as following (NO REPEATED ENTRIES):
* when you collect data from a project, you need to add it to a CSV called `projects.csv`
* when you collect the pull requests of a project, you need to store them in a file named after the owner and the name of project 
(projects/owner-project.csv) 
* when you collect data from users, you need to add it to a CSV called `users.csv` 


## Functions to the user
A user may be able to:
* request a project collection. By providing the owner and repository name, your program needs to start the collection of everything
(project, pull request, users -- including scraped data)
* list all projects collected
* list all pull requests from a project (please list the projects to help the user giving an existing option)
* list the summary of a project, containing:
   - number of pull requests in `open` state
   - number of pull requests in `closed` state
   - number of users
   - date of the oldest pull requested
   - number of users with a valid twitter account
   
* create graphics given a project:
   - boxplot comparing closed and open pull requests in terms of number of commits
   - boxplot comparing closed and open pull requests in terms of additions and deletions
   - boxplot comparing the number of changed files grouped by the author association
   - scatterplot: additions x deletions
   - histogram: number of commits per pull request
 
 * create graphics considering ALL pull requests from ALL projects:
   - line graph showing the total number of pull requests per day
   - line graph comparing number of open and closed pull requests per day
   - bars comparing the number of users per project
   - histogram: number of commits per pull request

* calculate the correlation between the data collected for a user 
(following, followers, number of pull requests, number of contributions, etc.)

* calculate the correlation between all the numeric data in the pull requests for a project


 ## Tests
 You need to write at least 5 unit tests 
    
   
   
