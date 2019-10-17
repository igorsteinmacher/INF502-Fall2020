# (INF 502) Midterm

* **How to deliver:** Create a file called `midterm.ipynb` in the root folder of your GitHub repository. *Do not forget to commit and PUSH* (only one per group is enough)
     * REMEMBER to add your names in the beginning of the document
* **When to deliver:** This piece of your MidTerm needs to be PUSHED to your repo by Thursday (Oct. 17th) 2:20PM (**BEFORE OUR CLASS**)
* **The midterm can be done is pairs or individually. Clear copies or clones will be zeroed**

Please consider these two CSV files: [ant_bait.csv](https://github.com/igorsteinmacher/INF502-Fall2019/blob/master/notebooks/ant_bait.csv) and [ant_species.csv](https://github.com/igorsteinmacher/INF502-Fall2019/blob/master/notebooks/ant_species.csv)
This data is part of the [census of the ant community](https://github.com/weecology/PortalData/tree/master/Ants) occurred every year (1977-2009) over a two week period during July after the summer monsoons have begun. 

`ant_bait` includes data collected by leaving bait piles for ants to forage. species and abundance are recorded.

`ant_species` contains the ant species list and species codes used in `ant_bait`.

You are requested to (the items would help you to think step by step):
1. (**30%**) map each of the CSVs structure to classes in Python (each CSV should be mapped to a class)
 * Please provide with a constructor method receiving all the attributes as parameters
 * Create a method that enables someone to print the objects:
       - for the ant_species it should be "genus species (e.g., Camponotus festinatus)
       - for the ant_bait: "species id - month, year: + abundance (e.g., cono bico - July, 2009: 2)
2. (**40%**) for each CSV file, create a function that receives as a parameter the name of the file to be read and create an object for each of the rows of the file:
 - for each file, create a list to store the created objects (i.e., species_list would store the objects created from the ant_species csv; bait_list would store the objects created from the ant_bait csv) -- This list is what your function should return.
  - read a line; create an object; add to the list.
  - can be a method of the class, or a function outside. You choose.
3. (**30%**) you should replace the attribute `species` of `ant_bait` to an object of the class `ant_species` (In the file it maps to the `speciescode` column of `ant_species`)

4. (**10% extra**) Create a function that receive a collection of baits (dictionary, list, tuple) and the species_code as parameters; and returns the average abundance for that species.

Please provide textual explanation for your code (in markdown cells of your notebook). In case you prefer, you can keep the resulting code for each of the items in the list above.

**SLACK** to ask questions. Please ask in the channel called **#general**, so everybody can benefit from the answer.

Good luck
