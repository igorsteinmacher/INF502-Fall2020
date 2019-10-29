# Using REST APIs as data sources

* Data is everywhere and it is generated constantly
* The number of datasources is amazingly huge
* Datasets are huge and can be used in many ways

* We may do amazing things using data made available by third-party:
    - [https://developer.walmartlabs.com/docs]
    - [https://developer.spotify.com/documentation/web-api/]
    - [https://earthquake.usgs.gov/fdsnws/event/1/]
    
    
We will have a nice and brief overview about how to consume data from REST APIs, mainly focusing on **JSON**.


### What is an API?

**Application Programming Interface** defines the methods for one software program to interact with the other. 

In the case of this lecture, we are dealing with a REST API, which sends data over a network: one type of Web service.

When we want to receive data from an Web service, we need to make a `request` to this service. When the server receives this request, it sends a `response`.

![request.png](request.png)




### Requests

Knowing that, we will not have to learn about making requests in Python

We do it by importing the module requests


```python
import requests
```

There are different types of requests. 

In our case we will use a `GET`, which is used to retrieve data. This is the type of request we use to collect data.

A response from the API contains 2 things (among others): 
* response code
* response data

To make a request, we use:


```python
response = requests.get('http://twitter.com/igorsteinmacher')
type(response)
```




    requests.models.Response



The `request.get(URL)` returns an object Response, which provides, among other things, the response code.


```python
response.status_code
```




    200



THe most common codes are:
* 200: Everything went okay, and the result has been returned (if any).
* 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
* 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
* 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
* 403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
* 404: The resource you tried to access wasn’t found on the server.
* 503: The server is not ready to handle the request.

More details about status codes list can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### What about getting the data?

First, read the documentation! Everytime you use an API, please read the documentation to understand how to use, the structure, etc.

We will use the [Open Notify API](http://api.open-notify.org/), which gives access to data about the international space station.

These APIs usually provide multiple endpoints, which are the ways we can interact with that service.

Let's try a request and see how it goes:


```python
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
```

    200


Now we can see the data...


```python
response.content
```




    b'{"people": [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}], "number": 6, "message": "success"}'




```python
response.text
```




    '{"people": [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}], "number": 6, "message": "success"}'




```python
response.json()
```




    {'people': [{'name': 'Christina Koch', 'craft': 'ISS'},
      {'name': 'Alexander Skvortsov', 'craft': 'ISS'},
      {'name': 'Luca Parmitano', 'craft': 'ISS'},
      {'name': 'Andrew Morgan', 'craft': 'ISS'},
      {'name': 'Oleg Skripochka', 'craft': 'ISS'},
      {'name': 'Jessica Meir', 'craft': 'ISS'}],
     'number': 6,
     'message': 'success'}



### Working with JSON 
JSON stands for JavaScript Object Notation. It is a way to encode data structures that ensures that they are easily readable. 

JSON output look like Python something with *dictionaries, lists, strings* and *integers*. And it is...

But, how to use it? Well, we used it in the last command.



```python
import json
```

json has two main functions:

* `json.dumps()` — Takes in a Python object and converts (dumps) to a string.
* `json.loads()` — Takes a JSON string and converts (loads) to a Python object.

The `dumps()` is particularly useful as we can use it to format the json, making it easier to understand the output


```python
json_response = response.json()
formatted_json = json.dumps(json_response, sort_keys=False, indent=2)

print(formatted_json)
```

    {
      "people": [
        {
          "name": "Christina Koch",
          "craft": "ISS"
        },
        {
          "name": "Alexander Skvortsov",
          "craft": "ISS"
        },
        {
          "name": "Luca Parmitano",
          "craft": "ISS"
        },
        {
          "name": "Andrew Morgan",
          "craft": "ISS"
        },
        {
          "name": "Oleg Skripochka",
          "craft": "ISS"
        },
        {
          "name": "Jessica Meir",
          "craft": "ISS"
        }
      ],
      "number": 6,
      "message": "success"
    }


### REST API with Query Parameters

In some cases, it is possible to pass parameters to filter the output of the API. 

The http://api.open-notify.org/iss-pass.json endpoint tells the next times that the international space station will pass over a given location on the earth.

It requires parameters


```python
response = requests.get("http://api.open-notify.org/iss-pass.json")
print("RESPONSE CODE:" + str(response.status_code))
print(response.json())

```

    RESPONSE CODE:400
    {'message': 'failure', 'reason': 'Latitude must be specified'}


Let's read the docs: 
* http://open-notify.org/Open-Notify-API/ISS-Pass-Times/


```python
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=51.1983&lon=111.6513")
print("RESPONSE CODE:" + str(response.status_code))
print(response.json())
#35.1983, 111.6513
```

    RESPONSE CODE:200
    {'message': 'success', 'request': {'altitude': 100, 'datetime': 1572331818, 'latitude': 51.1983, 'longitude': 111.6513, 'passes': 5}, 'response': [{'duration': 452, 'risetime': 1572377032}, {'duration': 630, 'risetime': 1572382697}, {'duration': 656, 'risetime': 1572388476}, {'duration': 655, 'risetime': 1572394283}, {'duration': 633, 'risetime': 1572400087}]}



```python
formatted_json = json.dumps(response.json(), sort_keys=False, indent=2)
print(formatted_json)
```

    {
      "message": "success",
      "request": {
        "altitude": 100,
        "datetime": 1572331818,
        "latitude": 51.1983,
        "longitude": 111.6513,
        "passes": 5
      },
      "response": [
        {
          "duration": 452,
          "risetime": 1572377032
        },
        {
          "duration": 630,
          "risetime": 1572382697
        },
        {
          "duration": 656,
          "risetime": 1572388476
        },
        {
          "duration": 655,
          "risetime": 1572394283
        },
        {
          "duration": 633,
          "risetime": 1572400087
        }
      ]
    }


#### Let’s deal with the pass times from our JSON object

Reading the docs (and looking at our JSON), we can see what we need to do


```python
times = []

for item in response.json()['response']:
    times.append(item['risetime'])
    
print(times)
```

    [1572377032, 1572382697, 1572388476, 1572394283, 1572400087]


Just to finish, what are these number?


```python

```


```python

```

### Let's play: your turn

Look at this API:
* https://earthquake.usgs.gov/fdsnws/event/1/

I want you to 
1. use filters to get the earthquakes from the previous 60 days, with magnitude between 5.8 and 7.
2. print the name, date, and magnitude of each of them
3. find the highest magnitude
4. using the ISSS API, show when the satelite will go through the place where the earthquake with the highest magnitude happened



```python

```


```python

```
