### In Class Assignment!!! ###

**How to Turn In:** Create a Python Notebook on your repository named `InClassSep29.ipynb`

**1 notebook per group is enough. Remember to add the name of all students in the group to your Notebook**

**Deadline:** Oct-01

We want to manage our movie collection. To do so, we need to write a program that helps us. You need to use OO design and follow the constraints below:

1. A `Movie` needs to have a title, a genres (may be more than one), year, my review, a list of actors, and a watch counter (how many times I watched), borrowed (a flag - True/False - that says if this movie is currently with someone), borrower name.
2. We can interact with a movie by: 
  - watching the movie (increase the counter), 
  - writing a review about the movie, 
  - set any of the fields (except flag, borrower, and counter, which are changed by different actions)
  - borrowing the movie (set the borrower and change the flag)
  - returning the moving (set borrower to "" and flag to False)
  - list the details of the movie when printing it in the following format:
  ```
     Movie: The Godfather     Year: 1972
     Genre: Crime, Drama
     List of Actors:
         Marlon Brando
         Al Pacino
         Robert Duvall
  ```
  
3. The list of actors, need to have objects of type `Actor`, which are composed of name, date_of_birth, and nationality. You should be able to:
    - set the fields name, date_of_birth, and nationality.


***CHALLENGE:*** *change your classes to make it possible to list (from an object actor) all the movies that the actor participated.* 
