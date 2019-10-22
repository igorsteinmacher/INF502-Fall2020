## Exploring data using Pandas

![Pandas](pandas.jpg)

***Want the Python Notebook??*** [Get it here](./PandasKickoff.ipynb)

***Look at it at nbviewer*** [Check it here](https://nbviewer.jupyter.org/github/igorsteinmacher/INF502-Fall2019/blob/master/notebooks/PandasKickoff.ipynb)

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




    pandas.core.frame.DataFrame



Yes! A DataFrame. And it reads really nice, look:


```python
cpr
### We can use head() and tail() functions to see a bit less
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>user1</td>
      <td>php-src</td>
      <td>C</td>
      <td>122</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>user2</td>
      <td>activeadmin</td>
      <td>ruby</td>
      <td>3325</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>user3</td>
      <td>YouCompleteMe</td>
      <td>python</td>
      <td>2128</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>user4</td>
      <td>requests</td>
      <td>python</td>
      <td>2663</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>user5</td>
      <td>ipython</td>
      <td>python</td>
      <td>7901</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>user6</td>
      <td>haste-compiler</td>
      <td>haskell</td>
      <td>407</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>user7</td>
      <td>select2</td>
      <td>javascript</td>
      <td>1987</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>user8</td>
      <td>django</td>
      <td>python</td>
      <td>8608</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>user9</td>
      <td>folly</td>
      <td>C++</td>
      <td>206</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>user10</td>
      <td>django</td>
      <td>python</td>
      <td>4745</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>user11</td>
      <td>homebrew-cask</td>
      <td>ruby</td>
      <td>5561</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>user12</td>
      <td>Chart.js</td>
      <td>javascript</td>
      <td>2116</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>user13</td>
      <td>react</td>
      <td>javascript</td>
      <td>3753</td>
      <td>115</td>
    </tr>
    <tr>
      <th>13</th>
      <td>user14</td>
      <td>codecombat</td>
      <td>coffeescript</td>
      <td>348</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>user14</td>
      <td>duckduckgo</td>
      <td>perl</td>
      <td>30</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>user15</td>
      <td>ReactiveCocoa</td>
      <td>objective-c</td>
      <td>3253</td>
      <td>250</td>
    </tr>
    <tr>
      <th>16</th>
      <td>user16</td>
      <td>angular.js</td>
      <td>javascript</td>
      <td>12671</td>
      <td>250</td>
    </tr>
    <tr>
      <th>17</th>
      <td>user17</td>
      <td>node</td>
      <td>javascript</td>
      <td>606</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>user18</td>
      <td>bacon.js</td>
      <td>coffeescript</td>
      <td>197</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>user19</td>
      <td>drone</td>
      <td>go</td>
      <td>2067</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>user20</td>
      <td>jenkins</td>
      <td>java</td>
      <td>1672</td>
      <td>5</td>
    </tr>
    <tr>
      <th>21</th>
      <td>user21</td>
      <td>SVProgressHUD</td>
      <td>objective-c</td>
      <td>663</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>user22</td>
      <td>youtube-dl</td>
      <td>python</td>
      <td>11866</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>user23</td>
      <td>godot</td>
      <td>C</td>
      <td>2395</td>
      <td>1</td>
    </tr>
    <tr>
      <th>24</th>
      <td>user24</td>
      <td>composer</td>
      <td>php</td>
      <td>4819</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25</th>
      <td>user25</td>
      <td>folly</td>
      <td>C++</td>
      <td>125</td>
      <td>2</td>
    </tr>
    <tr>
      <th>26</th>
      <td>user25</td>
      <td>netty</td>
      <td>java</td>
      <td>3923</td>
      <td>1</td>
    </tr>
    <tr>
      <th>27</th>
      <td>user26</td>
      <td>rails</td>
      <td>ruby</td>
      <td>28265</td>
      <td>1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>user27</td>
      <td>xbmc</td>
      <td>C++</td>
      <td>9635</td>
      <td>250</td>
    </tr>
    <tr>
      <th>29</th>
      <td>user28</td>
      <td>karma</td>
      <td>coffeescript</td>
      <td>1230</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>42062</th>
      <td>user36910</td>
      <td>three.js</td>
      <td>javascript</td>
      <td>10155</td>
      <td>2</td>
    </tr>
    <tr>
      <th>42063</th>
      <td>user36911</td>
      <td>sentry</td>
      <td>python</td>
      <td>375</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42064</th>
      <td>user36912</td>
      <td>jekyll</td>
      <td>ruby</td>
      <td>1837</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42065</th>
      <td>user36913</td>
      <td>Mobile-Detect</td>
      <td>php</td>
      <td>563</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42066</th>
      <td>user36914</td>
      <td>ipython</td>
      <td>python</td>
      <td>9386</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42067</th>
      <td>user36915</td>
      <td>laravel</td>
      <td>php</td>
      <td>3708</td>
      <td>7</td>
    </tr>
    <tr>
      <th>42068</th>
      <td>user36916</td>
      <td>Chart.js</td>
      <td>javascript</td>
      <td>1005</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42069</th>
      <td>user36917</td>
      <td>angular.js</td>
      <td>javascript</td>
      <td>8838</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42070</th>
      <td>user36918</td>
      <td>MBProgressHUD</td>
      <td>objective-c</td>
      <td>225</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42071</th>
      <td>user36919</td>
      <td>TrinityCore</td>
      <td>C++</td>
      <td>20139</td>
      <td>3</td>
    </tr>
    <tr>
      <th>42072</th>
      <td>user36920</td>
      <td>scikit-learn</td>
      <td>C</td>
      <td>4947</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42073</th>
      <td>user36921</td>
      <td>scikit-learn</td>
      <td>C</td>
      <td>2847</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42074</th>
      <td>user36921</td>
      <td>jekyll</td>
      <td>ruby</td>
      <td>5959</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42075</th>
      <td>user36922</td>
      <td>fish-shell</td>
      <td>C++</td>
      <td>1639</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42076</th>
      <td>user36923</td>
      <td>node</td>
      <td>javascript</td>
      <td>3135</td>
      <td>2</td>
    </tr>
    <tr>
      <th>42077</th>
      <td>user36924</td>
      <td>meteor</td>
      <td>javascript</td>
      <td>3934</td>
      <td>8</td>
    </tr>
    <tr>
      <th>42078</th>
      <td>user36925</td>
      <td>react</td>
      <td>javascript</td>
      <td>5722</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42079</th>
      <td>user36926</td>
      <td>activeadmin</td>
      <td>ruby</td>
      <td>2735</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42080</th>
      <td>user36927</td>
      <td>fish-shell</td>
      <td>C++</td>
      <td>1748</td>
      <td>5</td>
    </tr>
    <tr>
      <th>42081</th>
      <td>user36928</td>
      <td>coffeescript</td>
      <td>coffeescript</td>
      <td>2011</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42082</th>
      <td>user36929</td>
      <td>Faker</td>
      <td>php</td>
      <td>1293</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42083</th>
      <td>user36930</td>
      <td>Slim</td>
      <td>php</td>
      <td>1684</td>
      <td>4</td>
    </tr>
    <tr>
      <th>42084</th>
      <td>user36931</td>
      <td>brackets</td>
      <td>javascript</td>
      <td>7876</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42085</th>
      <td>user36932</td>
      <td>angular.js</td>
      <td>javascript</td>
      <td>8799</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42086</th>
      <td>user36932</td>
      <td>backbone</td>
      <td>javascript</td>
      <td>3452</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42087</th>
      <td>user36933</td>
      <td>node</td>
      <td>javascript</td>
      <td>14285</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42088</th>
      <td>user36934</td>
      <td>react</td>
      <td>javascript</td>
      <td>8762</td>
      <td>2</td>
    </tr>
    <tr>
      <th>42089</th>
      <td>user36934</td>
      <td>rails</td>
      <td>ruby</td>
      <td>27508</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42090</th>
      <td>user36935</td>
      <td>cocos2d-x</td>
      <td>C++</td>
      <td>15047</td>
      <td>1</td>
    </tr>
    <tr>
      <th>42091</th>
      <td>user36936</td>
      <td>node</td>
      <td>javascript</td>
      <td>9508</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>42092 rows × 5 columns</p>
</div>



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




    (42092, 5)



What about the column names?


```python
cpr.columns
```




    Index(['user', 'project_name', 'prog_lang', 'pull_req_number', 'num_commits'], dtype='object')



And the datatype per column?


```python
cpr.dtypes
```




    user               object
    project_name       object
    prog_lang          object
    pull_req_number     int64
    num_commits         int64
    dtype: object



Some more information: `info()` method prints information including the index dtype and column dtypes, non-null values and memory usage.


```python
cpr.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 42092 entries, 0 to 42091
    Data columns (total 5 columns):
    user               42092 non-null object
    project_name       42092 non-null object
    prog_lang          42092 non-null object
    pull_req_number    42092 non-null int64
    num_commits        42092 non-null int64
    dtypes: int64(2), object(3)
    memory usage: 1.6+ MB


What is the type of a specific column???


```python
type(cpr["num_commits"])
```




    pandas.core.series.Series



A *serie* is a list, with one dimension, indexed. Each column of a dataframe is a series

Before moving ahead, we can use the types to filter some columns. 

Let's say we want only the columns that store `int`:


```python
int_columns = cpr.dtypes[cpr.dtypes == "int64"].index
int_columns
```




    Index(['pull_req_number', 'num_commits'], dtype='object')



Now... I just want to see these columns... **BOOM**


```python
cpr[int_columns].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>122</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3325</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2128</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2663</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7901</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### What about statistical information about my DataFrame?

`describe()` method provides a summary of numeric values in your dataset: mean, standard deviation, minimum, maximum, 1st quartile, 2nd quartile (median), 3rd quartile of the columns with numeric values. It also counts the number of variables in the dataset (are there missing variables?)


```python
cpr.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>42092.000000</td>
      <td>42092.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4452.145681</td>
      <td>3.824242</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6152.304478</td>
      <td>20.760123</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>628.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2007.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5534.250000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>38174.000000</td>
      <td>385.000000</td>
    </tr>
  </tbody>
</table>
</div>



We can do it for a Series...


```python
cpr["num_commits"].describe
```




    <bound method NDFrame.describe of 0          1
    1          1
    2          2
    3          1
    4          1
    5          1
    6          1
    7          3
    8          1
    9          2
    10         1
    11         1
    12       115
    13         1
    14         1
    15       250
    16       250
    17         1
    18         1
    19         1
    20         5
    21         1
    22         1
    23         1
    24         1
    25         2
    26         1
    27         1
    28       250
    29         1
            ... 
    42062      2
    42063      1
    42064      1
    42065      1
    42066      1
    42067      7
    42068      1
    42069      1
    42070      1
    42071      3
    42072      1
    42073      1
    42074      1
    42075      1
    42076      2
    42077      8
    42078      1
    42079      1
    42080      5
    42081      1
    42082      1
    42083      4
    42084      1
    42085      1
    42086      1
    42087      1
    42088      2
    42089      1
    42090      1
    42091      2
    Name: num_commits, Length: 42092, dtype: int64>




```python
#LOOK at this with a non-numeric column
cpr.prog_lang.describe() #either way work.
```




    count     42092
    unique       17
    top        ruby
    freq       8147
    Name: prog_lang, dtype: object



And we can get specific information per column


```python
cpr.num_commits.median()
```




    1.0




```python
cpr.num_commits.mean()
```




    3.8242421362729258




```python
cpr.num_commits.std()
```




    20.76012335707578



### --------------####
### Playing with the data: sorting

We can sort our data easily using pandas.

In this example, sorting by Programming Language


```python
cpr.sort_values("num_commits", ascending=False).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>38987</th>
      <td>user34165</td>
      <td>three.js</td>
      <td>javascript</td>
      <td>7832</td>
      <td>385</td>
    </tr>
    <tr>
      <th>705</th>
      <td>user640</td>
      <td>cocos2d-x</td>
      <td>C++</td>
      <td>6866</td>
      <td>364</td>
    </tr>
    <tr>
      <th>7335</th>
      <td>user6426</td>
      <td>redis</td>
      <td>C</td>
      <td>3506</td>
      <td>315</td>
    </tr>
    <tr>
      <th>19587</th>
      <td>user17126</td>
      <td>jenkins</td>
      <td>java</td>
      <td>2718</td>
      <td>307</td>
    </tr>
    <tr>
      <th>35826</th>
      <td>user31347</td>
      <td>redis</td>
      <td>C</td>
      <td>3230</td>
      <td>290</td>
    </tr>
    <tr>
      <th>13300</th>
      <td>user11672</td>
      <td>cocos2d-x</td>
      <td>C++</td>
      <td>16576</td>
      <td>281</td>
    </tr>
    <tr>
      <th>3601</th>
      <td>user3214</td>
      <td>three.js</td>
      <td>javascript</td>
      <td>7808</td>
      <td>277</td>
    </tr>
    <tr>
      <th>13873</th>
      <td>user12167</td>
      <td>spring-framework</td>
      <td>java</td>
      <td>642</td>
      <td>273</td>
    </tr>
    <tr>
      <th>26360</th>
      <td>user23077</td>
      <td>Faker</td>
      <td>php</td>
      <td>660</td>
      <td>259</td>
    </tr>
    <tr>
      <th>18632</th>
      <td>user16293</td>
      <td>libgdx</td>
      <td>java</td>
      <td>814</td>
      <td>258</td>
    </tr>
  </tbody>
</table>
</div>



We can sort using *many columns*, by using a list (sort will happen from the first item to the last)


```python
cpr.sort_values(["prog_lang", "project_name", "num_commits"], ascending=False).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14351</th>
      <td>user12556</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>678</td>
      <td>11</td>
    </tr>
    <tr>
      <th>40943</th>
      <td>user35906</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1609</td>
      <td>10</td>
    </tr>
    <tr>
      <th>35890</th>
      <td>user31404</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>565</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1800</th>
      <td>user1614</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1179</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20245</th>
      <td>user17684</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1559</td>
      <td>3</td>
    </tr>
    <tr>
      <th>29167</th>
      <td>user25562</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>30</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4780</th>
      <td>user4214</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>44</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5142</th>
      <td>user4533</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>185</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7862</th>
      <td>user6897</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1515</td>
      <td>2</td>
    </tr>
    <tr>
      <th>32077</th>
      <td>user28045</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>428</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
cpr.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>user1</td>
      <td>php-src</td>
      <td>C</td>
      <td>122</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>user2</td>
      <td>activeadmin</td>
      <td>ruby</td>
      <td>3325</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>user3</td>
      <td>YouCompleteMe</td>
      <td>python</td>
      <td>2128</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>user4</td>
      <td>requests</td>
      <td>python</td>
      <td>2663</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>user5</td>
      <td>ipython</td>
      <td>python</td>
      <td>7901</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>user6</td>
      <td>haste-compiler</td>
      <td>haskell</td>
      <td>407</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>user7</td>
      <td>select2</td>
      <td>javascript</td>
      <td>1987</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>user8</td>
      <td>django</td>
      <td>python</td>
      <td>8608</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>user9</td>
      <td>folly</td>
      <td>C++</td>
      <td>206</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>user10</td>
      <td>django</td>
      <td>python</td>
      <td>4745</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



If you want to keep the sorted version, you can use the parameter `inplace`:


```python
cpr.sort_values(["prog_lang", "project_name", "num_commits"], ascending=False, inplace=True)
```


```python
cpr.head(10)
#cpr = pandas.read_csv("commits_pr.csv") #--> to return to the original order
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14351</th>
      <td>user12556</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>678</td>
      <td>11</td>
    </tr>
    <tr>
      <th>40943</th>
      <td>user35906</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1609</td>
      <td>10</td>
    </tr>
    <tr>
      <th>35890</th>
      <td>user31404</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>565</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1800</th>
      <td>user1614</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1179</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20245</th>
      <td>user17684</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1559</td>
      <td>3</td>
    </tr>
    <tr>
      <th>29167</th>
      <td>user25562</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>30</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4780</th>
      <td>user4214</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>44</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5142</th>
      <td>user4533</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>185</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7862</th>
      <td>user6897</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1515</td>
      <td>2</td>
    </tr>
    <tr>
      <th>32077</th>
      <td>user28045</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>428</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Counting the occurences of variables

So, to count the occurrences in a column we have to select the column first, and use the method `value_counts()`


```python
cpr.prog_lang.value_counts()
```




    ruby            8147
    javascript      7052
    python          4092
    php             4069
    C++             2785
    java            2596
    C               2196
    go              2103
    coffeescript    2066
    scala           1823
    objective-c     1801
    haskell          950
    clojure          882
    perl             663
    erlang           500
    typescript       343
    Perl              24
    Name: prog_lang, dtype: int64



But... I just want to know what are the languages out there. Is there a way?

*Always*


```python
cpr["prog_lang"].unique()
```




    array(['typescript', 'scala', 'ruby', 'python', 'php', 'perl',
           'objective-c', 'javascript', 'java', 'haskell', 'go', 'erlang',
           'coffeescript', 'clojure', 'Perl', 'C++', 'C'], dtype=object)




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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>prog_lang</th>
      <th>project_name</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14351</th>
      <td>typescript</td>
      <td>winjs</td>
      <td>11</td>
    </tr>
    <tr>
      <th>40943</th>
      <td>typescript</td>
      <td>winjs</td>
      <td>10</td>
    </tr>
    <tr>
      <th>35890</th>
      <td>typescript</td>
      <td>winjs</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1800</th>
      <td>typescript</td>
      <td>winjs</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20245</th>
      <td>typescript</td>
      <td>winjs</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



What if now I want to filter those projects written in `C` language?


```python
only_C = cpr[cpr["prog_lang"]=='C']
only_C.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2196.000000</td>
      <td>2196.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3340.718124</td>
      <td>6.885246</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3113.785559</td>
      <td>31.142637</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>704.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2427.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5143.500000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>13040.000000</td>
      <td>315.000000</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>535</th>
      <td>user491</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>106</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2368</th>
      <td>user2125</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1610</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3644</th>
      <td>user3247</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>207</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6174</th>
      <td>user5419</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1356</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9288</th>
      <td>user8154</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1342</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9851</th>
      <td>user8644</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>31</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14019</th>
      <td>user12267</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1596</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17979</th>
      <td>user15728</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>27</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20726</th>
      <td>user18101</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1151</td>
      <td>1</td>
    </tr>
    <tr>
      <th>25046</th>
      <td>user21934</td>
      <td>winjs</td>
      <td>typescript</td>
      <td>1628</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



And... we can use OR (|) and AND(&) to play!


```python
cpr[one_commit & language_C].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>project_name</th>
      <th>prog_lang</th>
      <th>pull_req_number</th>
      <th>num_commits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1625</th>
      <td>user1464</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>284</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1696</th>
      <td>user1526</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>224</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2259</th>
      <td>user2025</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>398</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2522</th>
      <td>user2268</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>387</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3210</th>
      <td>user2872</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>311</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3946</th>
      <td>user3515</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>366</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4774</th>
      <td>user4209</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>291</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5802</th>
      <td>user5103</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7326</th>
      <td>user6419</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>58</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7811</th>
      <td>user6850</td>
      <td>twemproxy</td>
      <td>C</td>
      <td>217</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pull_req_number</th>
      <th>num_commits</th>
      <th>group_commit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>42092.000000</td>
      <td>42092.000000</td>
      <td>29655.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4452.145681</td>
      <td>3.824242</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6152.304478</td>
      <td>20.760123</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>628.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2007.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5534.250000</td>
      <td>2.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>38174.000000</td>
      <td>385.000000</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



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




    pull_req_number    8213.5
    num_commits           2.0
    group_commit          1.0
    Name: 0.75, dtype: float64




```python
for lang in cpr["prog_lang"].unique():
    print("Language %s: \t%0.3f"%(lang, cpr[cpr["prog_lang"]==lang]["num_commits"].median()))
```

    Language typescript: 	1.000
    Language scala: 	1.000
    Language ruby: 	1.000
    Language python: 	1.000
    Language php: 	1.000
    Language perl: 	1.000
    Language objective-c: 	1.000
    Language javascript: 	1.000
    Language java: 	1.000
    Language haskell: 	1.000
    Language go: 	1.000
    Language erlang: 	1.000
    Language coffeescript: 	1.000
    Language clojure: 	1.000
    Language Perl: 	1.000
    Language C++: 	1.000
    Language C: 	1.000


### Can we play with graphics?


```python

```
