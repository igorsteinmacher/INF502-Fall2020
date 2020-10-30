# Programming Assignment 2

You can arrange yourselves in groups of 3 or 4 students.

This assignment will give you some practice with writing complete applications that deal with data collection and analysis in Python structures.
The focus will be on using all the knowledge acquired in this course, from basic Python to Pandas, usign json, creating graphics, etc.

**IMPORTANT:** This assignment will evolve during the following weeks, after we learn other contents, and to count as your final.

I hope you enjoy this assignment.

## Context

We want to understand the context of GitHub. Analyzing repositories and developers who contribute. 
Your application will have to consume the [GitHub REST API](https://docs.github.com/en/free-pro-team@latest/rest), 
to collect information about the repo, pull requests, and users. 

Since we are interested in the social side of software development,  we will also scrape data from their GitHub profile.

The first requirement for this assignment is that you need to use object orientation to deal with the data you are collecting and analyzing.
The easy way to do is analyzing the structure of the `json` dictionary structure. When you have nested elements, a new object *may* be necessary.

So, about repositories, we would like to keep the name, owner (login), description, homepage, license (can be another class), 
number of forks, watchers, and date_of_collection (the date you collect the data). When you request to print the object it should be like this:
* `Owner/RepositoryName: Description (# of stars)`

Each repository also needs to be related to a list of pull requests. Thus, for each repos, collect the pull requests that 
are returned in the first page of a query like this:
* `https://api.github.com/search/issues?q=is:pr+repo:jabref/jabref` (using repository jabref/jabref as an example)

For each pull request you need to keep: title, number, body, state, date of creation (created_at), 
closing date (if the state is different than open), user, number of commits, additions, deletions, changed_files. 

* For the last 4 fields, you will need to make another query using the following format (using the number of the pull requests
you found before):
* `https://api.github.com/repos/JabRef/jabref/pulls/5531`

Then, for each author (user) you find in the pull requests you need to keep: login and number of pull requests (calculated). 
You are also required to *scrape* the following information from the user profile page on GitHub: 
Number of Repositories, Number of Followers, Number of Following, Number of contributions in the last year.
**If you have repeated users, you only need to update the number of pull requests**


You need to have a function called `to_CSV` that can be reused to convert any object to a csv entry (row). 
You need to provide the file name and the object. If the file does not exist, you need to create the file (with the header). 
If the file  exists, you need to append a new line with the object in the CSV. To make it possible, you will need to have a method
in each of your classes with the very same name, which will return a string with the data already structured as a CSV.


Use this function to create/update the files as following (NO REPEATED ENTRIES):
* when you collect data from a repo, you need to add it to a CSV called `repos.csv`
* when you collect the pull requests of a repo, you need to store them in a file named after the owner and the name of repo 
(repos/owner-repo.csv) 
* when you collect data from users, you need to add it to a CSV called `users.csv` 


## Functions to the user
A user may be able to:
* request the system to collect data for a specific repository (from GitHub). By providing the owner and repository name, your program needs to start the collection of everything
(repository, pull request, users -- including scraped data)
* list all repos collected
* list all pull requests from a repo (please list the repos to help the user giving an existing option)
* list the summary of a repo, containing:
   - number of pull requests in `open` state
   - number of pull requests in `closed` state
   - number of users
   - date of the oldest pull requested
   
* create graphics given a repo:
   - boxplot comparing closed and open pull requests in terms of number of commits
   - boxplot comparing closed and open pull requests in terms of additions and deletions
   - boxplot comparing the number of changed files grouped by the author association
   - scatterplot: additions x deletions
 
 * create graphics considering ALL pull requests from ALL repos:
   - line graph showing the total number of pull requests per day
   - line graph comparing number of open and closed pull requests per day
   - bars comparing the number of users per repo

* calculate the correlation between the data collected for a user 
(following, followers, number of pull requests, number of contributions, etc.)

* calculate the correlation between all the numeric data in the pull requests for a repo

 ## Tests
 You need to write at least 5 unit tests 
    
