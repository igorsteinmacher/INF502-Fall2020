# Web Scraping

### But first... what is HTML

**HyperText Markup Language**: it is NOT a programming language. As its name points it is a *markup language* is used to indicate to the browser how to layout content. 

HTML is based on tags, which indicates what should be done with the content.

The most basic tag is the `<html>`. Everything inside of it is HTML. **Important:** We need to use tags to delimit the scope, so we use open and close tags, like in the example:

``` 
<html>
...
</html>
```

Inside of an html tag, we can use other tags. Usually, a HTML page has two other scopes defined by tags: `head` and `body`. The content of the web page goes into the body. The head contains metadata about the page, like the title of the page (it sometimes stores JS, CSSs, etc.)

When scrapping, we usually focus on what is inside of the `<body>  <\body>`


<html>
    <head>
    </head>
    
   <body>
   </body>
</html>


There are many possible tags with different roles, for example `<p>` delimits a paragraph `<br>` breaks a line, `<a>` represents links

<html>
   <head>
   </head>

   <body>
      <p>
         Paragraph
         <a href="https://www.github.com">Link to GitHub</a>
      </p>
      <p>
         See the link below:
         <a href="https://www.twitter.com">Twitter</a> </p>
   </body>
</html>

In the above example, the `<a>` tag presents an `href` attribute, which determines where the link goes.

Elements (tags) may have multiple attributes to define its layout/behavior. The attribute `class`, for example, indicates the CSS that will be applied there. The attribute `id` is used sometimes to identify a tag

### Let's scrape

First, we need to import the module we are using... BeautifulSoup


```python
import requests
from bs4 import BeautifulSoup
```

Let's get a page... using requests


```python
result = requests.get("https://pythonprogramming.net/parsememcparseface/")
```

We use the content, to get ready to scrape

And we call/instantiate our BeautifulSoup object, using our response content.


```python
content = result.content
soup=BeautifulSoup(content, "html.parser")
soup
```

If we want, we can make it easier to read...


```python
print(soup.prettify())
```

We can use multiple attributes/methods depending on what we wanna scrape/get!


```python
print(soup.title)
```

We can deal with soup.title (which is a Tag object), getting name, content, parent, etc...


```python
print(soup.title.name)
```


```python
print(soup.title.string)
```


```python
print(soup.title.parent.name)
```


```python
print(soup.p)
```


```python
soup.p['class']
```


```python
print(soup.find_all('p'))
```


```python
for para in soup.find_all('p'):
    print(para.string)
    print(str(para.text))
    print("----")
```


```python
for url in soup.find_all('a'):
    print(url.text)
    print(url.get('href'))
    print("---")
```


```python
body = soup.find('div',attrs={"class":"body"})
print(body.prettify())

```


```python
print(footer.prettify())
```


```python
for child in body.children:
    print(child)
    print("---")
```


```python
len(list(body.children))
```


```python
body.find("a")

```


```python
for item in body.findAll("a"):
    print(item.string + " is a link to " + item.get('href'))
    if (item.has_attr('target')):
        print("target is: " + item.get("target"))
```


```python
body.findAll("div")
```


```python
body.findAll("img")
```


```python
len(list(body.descendants))
```


```python
print(body.a)
```


```python
for a in soup.findAll("a"):
    if (a.has_attr("data-delay")):
        print("YES: " + a.text)
    else:
        print("NO: " + a.text)

```


```python

```
