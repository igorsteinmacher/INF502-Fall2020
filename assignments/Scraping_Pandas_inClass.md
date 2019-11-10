```python
import requests
from bs4 import BeautifulSoup
import pandas
```


```python
result = requests.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density")
content = result.content
soup=BeautifulSoup(content, "html.parser")
```

By analyzing the HTML code, I found that the first table with class=sortable is the one I want

I converted the fields, and created a dict to make things easier. We would also have used a list


```python
table = soup.find('table',attrs={"class":"sortable"})

my_dict = {}

#I got the table that I want...
#Now I will navigate:
# For each row (<tr>), I will get the <td>s. 
for tr in table.findAll("tr"):
    td_list = tr.findAll("td")

    # JUST MAKING SURE THAT I AM GETTING THE TRs WITH TDs (not the THS)
    if (len(td_list) > 0):

        ### I USED THE EXISTENCE OF AN IMAGE (FLAG) TO FILTER THE LINES I WANT
        if(len(td_list[1].findAll("img")) > 0):

            ##Looking at the table I want the 2nd, 3rd, 4th, and 5th columns
            ### I know that se second column (second position in my list with the tds)
            country_name = td_list[1].text.strip()
            #for each field, I curated the numbers to remove the ',' so it is possible to convert to float/int
            areakm = td_list[2].text.replace(',','')
            areami = td_list[3].text.replace(',','')
            population = td_list[4].text.replace(',','')
            #created a dictionary to make it easier to work
            my_dict[country_name] = {'area_km2': float(areakm),
                                     'area_mi2': float(areami),  
                                     'population': int(population)  
            }
```

### Exercise 2
* It is facilitated because I converted the fields as I was scraping.


```python
# THis is the magical function I used to come from a dict to a dataframe
# the parameter orient. If dict keys are row, you use index. If the dict keys are columns, you don't need the param.
df = pandas.DataFrame.from_dict(my_dict, orient= 'index')
df
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
      <th>area_km2</th>
      <th>area_mi2</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abkhazia</th>
      <td>8660.00</td>
      <td>3344.00</td>
      <td>243206</td>
    </tr>
    <tr>
      <th>Afghanistan</th>
      <td>645807.00</td>
      <td>249347.00</td>
      <td>31575018</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>28703.00</td>
      <td>11082.00</td>
      <td>2862427</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>2381741.00</td>
      <td>919595.00</td>
      <td>42545964</td>
    </tr>
    <tr>
      <th>American Samoa (US)</th>
      <td>197.00</td>
      <td>76.00</td>
      <td>56700</td>
    </tr>
    <tr>
      <th>Andorra</th>
      <td>464.00</td>
      <td>179.00</td>
      <td>76177</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>1246700.00</td>
      <td>481354.00</td>
      <td>29250009</td>
    </tr>
    <tr>
      <th>Anguilla (UK)</th>
      <td>96.00</td>
      <td>37.00</td>
      <td>13452</td>
    </tr>
    <tr>
      <th>Antigua and Barbuda</th>
      <td>442.00</td>
      <td>171.00</td>
      <td>104084</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>2780400.00</td>
      <td>1073518.00</td>
      <td>44938712</td>
    </tr>
    <tr>
      <th>Armenia</th>
      <td>29743.00</td>
      <td>11484.00</td>
      <td>2962100</td>
    </tr>
    <tr>
      <th>Artsakh</th>
      <td>11458.00</td>
      <td>4424.00</td>
      <td>150932</td>
    </tr>
    <tr>
      <th>Aruba (Kingdom of the Netherlands)</th>
      <td>180.00</td>
      <td>69.00</td>
      <td>111309</td>
    </tr>
    <tr>
      <th>Australia</th>
      <td>7692024.00</td>
      <td>2969907.00</td>
      <td>25513109</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>83879.00</td>
      <td>32386.00</td>
      <td>8877036</td>
    </tr>
    <tr>
      <th>Azerbaijan</th>
      <td>86600.00</td>
      <td>33436.00</td>
      <td>10027874</td>
    </tr>
    <tr>
      <th>Bahamas</th>
      <td>13940.00</td>
      <td>5382.00</td>
      <td>386870</td>
    </tr>
    <tr>
      <th>Bahrain</th>
      <td>778.00</td>
      <td>300.00</td>
      <td>1543300</td>
    </tr>
    <tr>
      <th>Bangladesh</th>
      <td>143998.00</td>
      <td>55598.00</td>
      <td>167539272</td>
    </tr>
    <tr>
      <th>Barbados</th>
      <td>430.00</td>
      <td>166.00</td>
      <td>287025</td>
    </tr>
    <tr>
      <th>Belarus</th>
      <td>207600.00</td>
      <td>80155.00</td>
      <td>9465300</td>
    </tr>
    <tr>
      <th>Belgium</th>
      <td>30528.00</td>
      <td>11787.00</td>
      <td>11485729</td>
    </tr>
    <tr>
      <th>Belize</th>
      <td>22965.00</td>
      <td>8867.00</td>
      <td>398050</td>
    </tr>
    <tr>
      <th>Benin</th>
      <td>112622.00</td>
      <td>43484.00</td>
      <td>11733059</td>
    </tr>
    <tr>
      <th>Bermuda (UK)</th>
      <td>52.00</td>
      <td>20.00</td>
      <td>63779</td>
    </tr>
    <tr>
      <th>Bhutan</th>
      <td>38394.00</td>
      <td>14824.00</td>
      <td>819360</td>
    </tr>
    <tr>
      <th>Bolivia</th>
      <td>1098581.00</td>
      <td>424164.00</td>
      <td>11307314</td>
    </tr>
    <tr>
      <th>Bonaire (Netherlands)</th>
      <td>288.00</td>
      <td>111.00</td>
      <td>18905</td>
    </tr>
    <tr>
      <th>Bosnia and Herzegovina</th>
      <td>51209.00</td>
      <td>19772.00</td>
      <td>3511372</td>
    </tr>
    <tr>
      <th>Botswana</th>
      <td>581730.00</td>
      <td>224607.00</td>
      <td>2302878</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Thailand</th>
      <td>513120.00</td>
      <td>198117.00</td>
      <td>66431255</td>
    </tr>
    <tr>
      <th>Timor-Leste</th>
      <td>14919.00</td>
      <td>5760.00</td>
      <td>1167242</td>
    </tr>
    <tr>
      <th>Togo</th>
      <td>56600.00</td>
      <td>21853.00</td>
      <td>7538000</td>
    </tr>
    <tr>
      <th>Tokelau (NZ)</th>
      <td>10.00</td>
      <td>4.00</td>
      <td>1499</td>
    </tr>
    <tr>
      <th>Tonga</th>
      <td>720.00</td>
      <td>278.00</td>
      <td>100651</td>
    </tr>
    <tr>
      <th>Transnistria</th>
      <td>4163.00</td>
      <td>1607.00</td>
      <td>469000</td>
    </tr>
    <tr>
      <th>Trinidad and Tobago</th>
      <td>5155.00</td>
      <td>1990.00</td>
      <td>1359193</td>
    </tr>
    <tr>
      <th>Tunisia</th>
      <td>163610.00</td>
      <td>63170.00</td>
      <td>11551448</td>
    </tr>
    <tr>
      <th>Turkey</th>
      <td>783562.00</td>
      <td>302535.00</td>
      <td>82003882</td>
    </tr>
    <tr>
      <th>Turkmenistan</th>
      <td>491210.00</td>
      <td>189657.00</td>
      <td>5851466</td>
    </tr>
    <tr>
      <th>Turks and Caicos Islands (UK)</th>
      <td>497.00</td>
      <td>192.00</td>
      <td>37910</td>
    </tr>
    <tr>
      <th>Tuvalu</th>
      <td>26.00</td>
      <td>10.00</td>
      <td>10200</td>
    </tr>
    <tr>
      <th>Uganda</th>
      <td>241551.00</td>
      <td>93263.00</td>
      <td>40006700</td>
    </tr>
    <tr>
      <th>Ukraine [note 5]</th>
      <td>603000.00</td>
      <td>232820.00</td>
      <td>41990278</td>
    </tr>
    <tr>
      <th>United Arab Emirates</th>
      <td>83600.00</td>
      <td>32278.00</td>
      <td>9770529</td>
    </tr>
    <tr>
      <th>United Kingdom</th>
      <td>242910.00</td>
      <td>93788.00</td>
      <td>66435600</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>9833517.00</td>
      <td>3796742.00</td>
      <td>330195272</td>
    </tr>
    <tr>
      <th>United States Virgin Islands (US)</th>
      <td>352.00</td>
      <td>136.00</td>
      <td>104909</td>
    </tr>
    <tr>
      <th>Uruguay</th>
      <td>176215.00</td>
      <td>68037.00</td>
      <td>2990452</td>
    </tr>
    <tr>
      <th>Uzbekistan</th>
      <td>447400.00</td>
      <td>172742.00</td>
      <td>32653900</td>
    </tr>
    <tr>
      <th>Vanuatu</th>
      <td>12281.00</td>
      <td>4742.00</td>
      <td>304500</td>
    </tr>
    <tr>
      <th>Vatican City</th>
      <td>0.44</td>
      <td>0.17</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>Venezuela</th>
      <td>916445.00</td>
      <td>353841.00</td>
      <td>31828110</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>331212.00</td>
      <td>127882.00</td>
      <td>96208984</td>
    </tr>
    <tr>
      <th>Wallis &amp; Futuna (France)</th>
      <td>142.00</td>
      <td>55.00</td>
      <td>11700</td>
    </tr>
    <tr>
      <th>Western Sahara[note 7]</th>
      <td>252120.00</td>
      <td>97344.00</td>
      <td>567421</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>455000.00</td>
      <td>175676.00</td>
      <td>28915284</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>752612.00</td>
      <td>290585.00</td>
      <td>16405229</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>390757.00</td>
      <td>150872.00</td>
      <td>15159624</td>
    </tr>
    <tr>
      <th>Åland Islands (Finland)</th>
      <td>1552.00</td>
      <td>599.00</td>
      <td>28502</td>
    </tr>
  </tbody>
</table>
<p>250 rows × 3 columns</p>
</div>



### Exercise 3
* Summarizing our data


```python
df.describe()
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
      <th>area_km2</th>
      <th>area_mi2</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.500000e+02</td>
      <td>2.500000e+02</td>
      <td>2.500000e+02</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.454655e+05</td>
      <td>2.106154e+05</td>
      <td>3.047842e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.719106e+06</td>
      <td>6.637473e+05</td>
      <td>1.282811e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.400000e-01</td>
      <td>1.700000e-01</td>
      <td>5.600000e+01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.686550e+03</td>
      <td>7.362500e+02</td>
      <td>2.634935e+05</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.493100e+04</td>
      <td>2.507000e+04</td>
      <td>4.578766e+06</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.533760e+05</td>
      <td>1.364390e+05</td>
      <td>1.765074e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.712524e+07</td>
      <td>6.612093e+06</td>
      <td>1.399881e+09</td>
    </tr>
  </tbody>
</table>
</div>



### Exercise 4
* Creating the correlation matrix


```python
df.corr(method='pearson').style.background_gradient(cmap='coolwarm')
```




<style  type="text/css" >
    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col0 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col1 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col2 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col0 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col1 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col2 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col0 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col1 {
            background-color:  #3b4cc0;
            color:  #f1f1f1;
        }    #T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col2 {
            background-color:  #b40426;
            color:  #f1f1f1;
        }</style><table id="T_edae2028_035e_11ea_b9a5_3af9d378f87b" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >area_km2</th>        <th class="col_heading level0 col1" >area_mi2</th>        <th class="col_heading level0 col2" >population</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_edae2028_035e_11ea_b9a5_3af9d378f87blevel0_row0" class="row_heading level0 row0" >area_km2</th>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col0" class="data row0 col0" >1</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col1" class="data row0 col1" >1</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow0_col2" class="data row0 col2" >0.458636</td>
            </tr>
            <tr>
                        <th id="T_edae2028_035e_11ea_b9a5_3af9d378f87blevel0_row1" class="row_heading level0 row1" >area_mi2</th>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col0" class="data row1 col0" >1</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col1" class="data row1 col1" >1</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow1_col2" class="data row1 col2" >0.458635</td>
            </tr>
            <tr>
                        <th id="T_edae2028_035e_11ea_b9a5_3af9d378f87blevel0_row2" class="row_heading level0 row2" >population</th>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col0" class="data row2 col0" >0.458636</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col1" class="data row2 col1" >0.458635</td>
                        <td id="T_edae2028_035e_11ea_b9a5_3af9d378f87brow2_col2" class="data row2 col2" >1</td>
            </tr>
    </tbody></table>



### Exercise 5
* Scatterplot 


```python
df.plot.scatter(x = "area_km2", y = "population")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11efdd358>




![png](output_11_1.png)



```python

```
