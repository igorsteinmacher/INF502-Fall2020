# Using REST APIs as data sources

* Data is everywhere and it is generated constantly
* The number of datasources is amazingly huge
* Datasets are huge and can be used in many ways

* We may do amazing things using data made available by third-party:
    - https://developer.walmartlabs.com/docs
    - https://developer.spotify.com/documentation/web-api/
    - https://earthquake.usgs.gov/fdsnws/event/1/
    
    
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
response = requests.get('http://www.nau.edu/')
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
type(response.content)
```




    bytes




```python
response.text
```




    '{"message": "success", "people": [{"name": "Sergey Ryzhikov", "craft": "ISS"}, {"name": "Kate Rubins", "craft": "ISS"}, {"name": "Sergey Kud-Sverchkov", "craft": "ISS"}], "number": 3}'




```python
response.json()
```




    {'message': 'success',
     'people': [{'name': 'Sergey Ryzhikov', 'craft': 'ISS'},
      {'name': 'Kate Rubins', 'craft': 'ISS'},
      {'name': 'Sergey Kud-Sverchkov', 'craft': 'ISS'}],
     'number': 3}



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
formatted_json = json.dumps(json_response, sort_keys=True, indent=3
                           )

print(formatted_json)
```

    {
       "message": "success",
       "number": 3,
       "people": [
          {
             "craft": "ISS",
             "name": "Sergey Ryzhikov"
          },
          {
             "craft": "ISS",
             "name": "Kate Rubins"
          },
          {
             "craft": "ISS",
             "name": "Sergey Kud-Sverchkov"
          }
       ]
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
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=35.1983&lon=111.6513")
print("RESPONSE CODE:" + str(response.status_code))
print(response.json())
#35.1983, 111.6513
```

    RESPONSE CODE:200
    {'message': 'success', 'request': {'altitude': 100, 'datetime': 1603836506, 'latitude': 35.1983, 'longitude': 111.6513, 'passes': 5}, 'response': [{'duration': 390, 'risetime': 1603841584}, {'duration': 520, 'risetime': 1603847415}, {'duration': 648, 'risetime': 1603853197}, {'duration': 542, 'risetime': 1603859036}, {'duration': 479, 'risetime': 1603907545}]}



```python
formatted_json = json.dumps(response.json(), sort_keys=False, indent=2)
#print(formatted_json)
print(response.json()["response"][0]["risetime"])
```

    1603841584


#### Let’s deal with the pass times from our JSON object

Reading the docs (and looking at our JSON), we can see what we need to do


```python
times = []

for item in response.json()['response']:
    times.append(item['risetime'])
    
print(times)
```

    [1603841584, 1603847415, 1603853197, 1603859036, 1603907545]



```python
from datetime import datetime

datetime.fromtimestamp(times[0]).strftime("%Y-%m-%d %I:%M:%S")
```




    '2020-10-27 04:33:04'




```python
response = requests.get("https://api.github.com/repos/rails/rails/pulls")
pulls = response.json()
print(json.dumps(pulls, indent=2))
```


```python
pulls[0]
```


### Let's play: your turn

Look at this API:
* https://earthquake.usgs.gov/fdsnws/event/1/

I want you to 
1. use filters to get the earthquakes from the previous 60 days, with magnitude between 5.8 and 7.
2. print the place, date, and magnitude of each of them
3. find the highest magnitude
4. using the ISS API, show when the satelite will go through the place where the earthquake with the highest magnitude happened



```python
import requests
response = requests.get("http://api.open-notify.org/iss-pass.json")
print("RESPONSE CODE:" + str(response.status_code))
print(response.json())
```

    RESPONSE CODE:400
    {'message': 'failure', 'reason': 'Latitude must be specified'}



```python
import requests
import json
from datetime import datetime

response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-08-27&maxmagnitude=7&minmagnitude=5.8")
json_response = response.json()
formatted_json = json.dumps(json_response, sort_keys=False, indent=2)

print(formatted_json)
```

    {
      "type": "FeatureCollection",
      "metadata": {
        "generated": 1603840328000,
        "url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-08-27&maxmagnitude=7&minmagnitude=5.8",
        "title": "USGS Earthquakes",
        "status": 200,
        "api": "1.10.3",
        "count": 40
      },
      "features": [
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "75 km NNE of Hihifo, Tonga",
            "time": 1603626457004,
            "updated": 1603816850040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000ccyh",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000ccyh&format=geojson",
            "felt": 9,
            "cdi": 4.1,
            "mmi": 3.887,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 539,
            "net": "us",
            "code": "6000ccyh",
            "ids": ",pt20299001,us6000ccyh,at00qira3f,",
            "sources": ",pt,us,at,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 5.014,
            "rms": 0.71,
            "gap": 62,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 75 km NNE of Hihifo, Tonga"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -173.4669,
              -15.3542,
              32.73
            ]
          },
          "id": "us6000ccyh"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.1,
            "place": "south of the Fiji Islands",
            "time": 1603436672004,
            "updated": 1603523312647,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000cbx8",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000cbx8&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 2.51,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 572,
            "net": "us",
            "code": "6000cbx8",
            "ids": ",pt20297001,us6000cbx8,",
            "sources": ",pt,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 4.045,
            "rms": 0.79,
            "gap": 25,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.1 - south of the Fiji Islands"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -179.9645,
              -25.6127,
              463.9
            ]
          },
          "id": "us6000cbx8"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6,
            "place": "West Chile Rise",
            "time": 1603417577475,
            "updated": 1603504452956,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000cbug",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000cbug&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 554,
            "net": "us",
            "code": "6000cbug",
            "ids": ",us6000cbug,pt20297000,",
            "sources": ",us,pt,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 13.888,
            "rms": 1.41,
            "gap": 47,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.0 - West Chile Rise"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -97.1352,
              -36.4011,
              10
            ]
          },
          "id": "us6000cbug"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "148 km WNW of Haveluloto, Tonga",
            "time": 1603355046992,
            "updated": 1603441663721,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000cb8b",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000cb8b&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.275,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "6000cb8b",
            "ids": ",pt20296000,us6000cb8b,",
            "sources": ",pt,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 5.927,
            "rms": 1.23,
            "gap": 33,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - 148 km WNW of Haveluloto, Tonga"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -176.6074,
              -20.8778,
              237.63
            ]
          },
          "id": "us6000cb8b"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "183 km ESE of Neiafu, Tonga",
            "time": 1603239753928,
            "updated": 1603326984040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000cafc",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000cafc&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.321,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "6000cafc",
            "ids": ",pt20295000,at00qiizpk,us6000cafc,",
            "sources": ",pt,at,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 7.413,
            "rms": 1.05,
            "gap": 26,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 183 km ESE of Neiafu, Tonga"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -172.3884,
              -19.3191,
              10
            ]
          },
          "id": "us6000cafc"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "117 km SSE of Sand Point, Alaska",
            "time": 1603143925888,
            "updated": 1603839758248,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c9lf",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c9lf&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.755,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "6000c9lf",
            "ids": ",us6000c9lf,pt20293006,ak020dgx8hsf,",
            "sources": ",us,pt,ak,",
            "types": ",ground-failure,internal-origin,losspager,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.51,
            "rms": 0.94,
            "gap": 65,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 117 km SSE of Sand Point, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -159.859,
              54.3459,
              24.45
            ]
          },
          "id": "us6000c9lf"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "Easter Island region",
            "time": 1602335697344,
            "updated": 1602422329581,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c7b1",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c7b1&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "6000c7b1",
            "ids": ",us6000c7b1,at00qhzm4y,",
            "sources": ",us,at,",
            "types": ",ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.901,
            "rms": 1.02,
            "gap": 50,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - Easter Island region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -112.3045,
              -28.5676,
              10
            ]
          },
          "id": "us6000c7b1"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "86 km ESE of Kimbe, Papua New Guinea",
            "time": 1602172729998,
            "updated": 1602261933332,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c6si",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c6si&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 5.526,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "6000c6si",
            "ids": ",pt20282001,at00qhw4ea,us6000c6si,",
            "sources": ",pt,at,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.152,
            "rms": 0.8,
            "gap": 28,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - 86 km ESE of Kimbe, Papua New Guinea"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              150.8349,
              -5.9004,
              30
            ]
          },
          "id": "us6000c6si"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.3,
            "place": "38 km ENE of Kainantu, Papua New Guinea",
            "time": 1602142532224,
            "updated": 1602317079636,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c6mu",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c6mu&format=geojson",
            "felt": 28,
            "cdi": 6.9,
            "mmi": 5.525,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 630,
            "net": "us",
            "code": "6000c6mu",
            "ids": ",at00qhvh38,pt20282000,us6000c6mu,",
            "sources": ",at,pt,us,",
            "types": ",dyfi,ground-failure,impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.413,
            "rms": 0.89,
            "gap": 15,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.3 - 38 km ENE of Kainantu, Papua New Guinea"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              146.1686,
              -6.114,
              103.49
            ]
          },
          "id": "us6000c6mu"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6,
            "place": "233 km E of Levuka, Fiji",
            "time": 1601979106688,
            "updated": 1603627571361,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c617",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c617&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 1.608,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 554,
            "net": "us",
            "code": "6000c617",
            "ids": ",at00qhryzm,pt20280000,us6000c617,",
            "sources": ",at,pt,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.316,
            "rms": 0.94,
            "gap": 24,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.0 - 233 km E of Levuka, Fiji"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -178.4762,
              -18.0101,
              633.92
            ]
          },
          "id": "us6000c617"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "68 km SE of Sand Point, Alaska",
            "time": 1601963690520,
            "updated": 1603490017028,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c5zm",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c5zm&format=geojson",
            "felt": 13,
            "cdi": 4.6,
            "mmi": 4.708,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 542,
            "net": "us",
            "code": "6000c5zm",
            "ids": ",at00qhrn3g,ak020cv5sgx1,ak020cv5s0vm,us6000c5zm,",
            "sources": ",at,ak,ak,us,",
            "types": ",dyfi,ground-failure,impact-link,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.157,
            "rms": 0.87,
            "gap": 122,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 68 km SE of Sand Point, Alaska"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -159.8598,
              54.8444,
              30.42
            ]
          },
          "id": "us6000c5zm"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "South Shetland Islands",
            "time": 1601633853188,
            "updated": 1601720347351,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c4p5",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c4p5&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 4.797,
            "alert": null,
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "6000c4p5",
            "ids": ",at00qhkkl9,pt20276001,us6000c4p5,",
            "sources": ",at,pt,us,",
            "types": ",internal-origin,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.243,
            "rms": 0.85,
            "gap": 73,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - South Shetland Islands"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -58.2326,
              -62.3735,
              10
            ]
          },
          "id": "us6000c4p5"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6,
            "place": "99 km W of Kandrian, Papua New Guinea",
            "time": 1601548488481,
            "updated": 1601916945040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c3td",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c3td&format=geojson",
            "felt": 8,
            "cdi": 3.8,
            "mmi": 4.443,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 557,
            "net": "us",
            "code": "6000c3td",
            "ids": ",us6000c3td,at00qhiqq0,pt20275002,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.615,
            "rms": 0.95,
            "gap": 19,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.0 - 99 km W of Kandrian, Papua New Guinea"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              148.6576,
              -6.0867,
              109.22
            ]
          },
          "id": "us6000c3td"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.4,
            "place": "39 km NE of Pangai, Tonga",
            "time": 1601514816524,
            "updated": 1603413261522,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c3kz",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c3kz&format=geojson",
            "felt": 9,
            "cdi": 5,
            "mmi": 5.878,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 635,
            "net": "us",
            "code": "6000c3kz",
            "ids": ",at00qhi0qn,pt20275000,us6000c3kz,",
            "sources": ",at,pt,us,",
            "types": ",dyfi,ground-failure,impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.988,
            "rms": 0.63,
            "gap": 20,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.4 - 39 km NE of Pangai, Tonga"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -174.1217,
              -19.5385,
              28
            ]
          },
          "id": "us6000c3kz"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.1,
            "place": "south of Africa",
            "time": 1601140222462,
            "updated": 1603818820081,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000c1np",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000c1np&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 572,
            "net": "us",
            "code": "6000c1np",
            "ids": ",us6000c1np,pt20270003,at00qh9zpe,",
            "sources": ",us,pt,at,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 13.767,
            "rms": 0.68,
            "gap": 18,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.1 - south of Africa"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              31.7404,
              -48.0249,
              10
            ]
          },
          "id": "us6000c1np"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "central East Pacific Rise",
            "time": 1600695435082,
            "updated": 1601216428974,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bqr4",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bqr4&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "7000bqr4",
            "ids": ",us7000bqr4,",
            "sources": ",us,",
            "types": ",losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 14.472,
            "rms": 0.78,
            "gap": 59,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - central East Pacific Rise"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -104.3789,
              -4.0426,
              10
            ]
          },
          "id": "us7000bqr4"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "53 km E of Cortes, Philippines",
            "time": 1600639995044,
            "updated": 1602113901051,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bql2",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bql2&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 4.001,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "7000bql2",
            "ids": ",us7000bql2,",
            "sources": ",us,",
            "types": ",losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.435,
            "rms": 0.56,
            "gap": 43,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - 53 km E of Cortes, Philippines"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              126.6799,
              9.2614,
              9
            ]
          },
          "id": "us7000bql2"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.9,
            "place": "central Mid-Atlantic Ridge",
            "time": 1600465438936,
            "updated": 1600639252455,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bq10",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bq10&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.454,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 732,
            "net": "us",
            "code": "7000bq10",
            "ids": ",pt20262001,at00qgvj1d,us7000bq10,",
            "sources": ",pt,at,us,",
            "types": ",impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 11.257,
            "rms": 0.66,
            "gap": 16,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.9 - central Mid-Atlantic Ridge"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -26.8408,
              0.9167,
              10
            ]
          },
          "id": "us7000bq10"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "12 km SSE of Arkaloch\u00f3ri, Greece",
            "time": 1600446497575,
            "updated": 1603035816375,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bpvt",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bpvt&format=geojson",
            "felt": 41,
            "cdi": 4.2,
            "mmi": 4.076,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 553,
            "net": "us",
            "code": "7000bpvt",
            "ids": ",us7000bpvt,pt20262000,",
            "sources": ",us,pt,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.421,
            "rms": 0.78,
            "gap": 35,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 12 km SSE of Arkaloch\u00f3ri, Greece"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              25.3034,
              35.0368,
              44
            ]
          },
          "id": "us7000bpvt"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6,
            "place": "157 km NNE of Labasa, Fiji",
            "time": 1600143136291,
            "updated": 1601952849577,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bndc",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bndc&format=geojson",
            "felt": 1,
            "cdi": 5.2,
            "mmi": 5.909,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 554,
            "net": "us",
            "code": "7000bndc",
            "ids": ",us7000bndc,",
            "sources": ",us,",
            "types": ",dyfi,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.159,
            "rms": 0.66,
            "gap": 34,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.0 - 157 km NNE of Labasa, Fiji"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              179.8689,
              -15.095,
              10
            ]
          },
          "id": "us7000bndc"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.4,
            "place": "18 km WNW of Esso, Russia",
            "time": 1600141288052,
            "updated": 1601955308893,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bnd1",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bnd1&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.196,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 630,
            "net": "us",
            "code": "7000bnd1",
            "ids": ",us7000bnd1,pt20259000,at00qgokx3,",
            "sources": ",us,pt,at,",
            "types": ",ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.898,
            "rms": 0.7,
            "gap": 25,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.4 - 18 km WNW of Esso, Russia"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              158.4171,
              55.9704,
              344
            ]
          },
          "id": "us7000bnd1"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "Vanuatu",
            "time": 1599899667322,
            "updated": 1601035870835,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bmcx",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bmcx&format=geojson",
            "felt": 1,
            "cdi": 2,
            "mmi": 3.84,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "7000bmcx",
            "ids": ",us7000bmcx,pt20256002,",
            "sources": ",us,pt,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 1.857,
            "rms": 0.7,
            "gap": 64,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - Vanuatu"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              167.6786,
              -17.2576,
              10
            ]
          },
          "id": "us7000bmcx"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.1,
            "place": "58 km SE of \u014cfunato, Japan",
            "time": 1599878651238,
            "updated": 1602210276695,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bm9m",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bm9m&format=geojson",
            "felt": 17,
            "cdi": 4.3,
            "mmi": 4.129,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 580,
            "net": "us",
            "code": "7000bm9m",
            "ids": ",us7000bm9m,at00qgiy9o,pt20256001,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.231,
            "rms": 1.01,
            "gap": 47,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.1 - 58 km SE of \u014cfunato, Japan"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              142.2499,
              38.7513,
              34
            ]
          },
          "id": "us7000bm9m"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.2,
            "place": "82 km NNE of Tocopilla, Chile",
            "time": 1599809757187,
            "updated": 1603402162848,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000blm2",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000blm2&format=geojson",
            "felt": 148,
            "cdi": 6.8,
            "mmi": 6.687,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 692,
            "net": "us",
            "code": "7000blm2",
            "ids": ",us7000blm2,at00qghh3w,pt20255000,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,ground-failure,impact-text,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.077,
            "rms": 0.88,
            "gap": 72,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.2 - 82 km NNE of Tocopilla, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -69.9096,
              -21.3968,
              51
            ]
          },
          "id": "us7000blm2"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "187 km SE of Sarangani, Philippines",
            "time": 1599635920225,
            "updated": 1602676811031,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bk82",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bk82&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 5.675,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "7000bk82",
            "ids": ",at00qgdqza,pt20253000,us7000bk82,",
            "sources": ",at,pt,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.054,
            "rms": 1.19,
            "gap": 32,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - 187 km SE of Sarangani, Philippines"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              126.6366,
              4.1837,
              17
            ]
          },
          "id": "us7000bk82"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "194 km SSE of Amahai, Indonesia",
            "time": 1599525920801,
            "updated": 1602820011330,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bjgb",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bjgb&format=geojson",
            "felt": 4,
            "cdi": 3.1,
            "mmi": 3.82,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 537,
            "net": "us",
            "code": "7000bjgb",
            "ids": ",us7000bjgb,pt20252000,at00qgbe3m,",
            "sources": ",us,pt,at,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.16,
            "rms": 0.81,
            "gap": 13,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 194 km SSE of Amahai, Indonesia"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              129.7559,
              -4.8828,
              172
            ]
          },
          "id": "us7000bjgb"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6,
            "place": "72 km NNE of Port-Vila, Vanuatu",
            "time": 1599459159710,
            "updated": 1601816992650,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bj6y",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bj6y&format=geojson",
            "felt": 3,
            "cdi": 3.4,
            "mmi": 6.063,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 555,
            "net": "us",
            "code": "7000bj6y",
            "ids": ",at00qg9yl1,pt20251000,us7000bj6y,",
            "sources": ",at,pt,us,",
            "types": ",dyfi,ground-failure,impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 2.065,
            "rms": 1.13,
            "gap": 41,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.0 - 72 km NNE of Port-Vila, Vanuatu"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              168.4935,
              -17.1086,
              10
            ]
          },
          "id": "us7000bj6y"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.3,
            "place": "17 km E of Talagutong, Philippines",
            "time": 1599405823148,
            "updated": 1601702084435,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000biyd",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000biyd&format=geojson",
            "felt": 38,
            "cdi": 7.2,
            "mmi": 4.468,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 638,
            "net": "us",
            "code": "7000biyd",
            "ids": ",at00qg8tfl,pt20250007,us7000biyd,",
            "sources": ",at,pt,us,",
            "types": ",dyfi,ground-failure,impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.832,
            "rms": 1.22,
            "gap": 29,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.3 - 17 km E of Talagutong, Philippines"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              125.8285,
              6.2693,
              120
            ]
          },
          "id": "us7000biyd"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.7,
            "place": "central Mid-Atlantic Ridge",
            "time": 1599375078848,
            "updated": 1602749682544,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000biu8",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000biu8&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 691,
            "net": "us",
            "code": "7000biu8",
            "ids": ",pt20250004,at00qg85pi,us7000biu8,",
            "sources": ",pt,at,us,",
            "types": ",impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 22.637,
            "rms": 0.71,
            "gap": 29,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.7 - central Mid-Atlantic Ridge"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -37.2043,
              7.6876,
              10
            ]
          },
          "id": "us7000biu8"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.2,
            "place": "Vanuatu",
            "time": 1599361156073,
            "updated": 1601603284050,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000birm",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000birm&format=geojson",
            "felt": 4,
            "cdi": 5,
            "mmi": 4.217,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 593,
            "net": "us",
            "code": "7000birm",
            "ids": ",pt20250002,at00qg7uyr,us7000birm,",
            "sources": ",pt,at,us,",
            "types": ",dyfi,ground-failure,impact-link,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 1.728,
            "rms": 1.19,
            "gap": 59,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.2 - Vanuatu"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              167.5321,
              -17.1562,
              10
            ]
          },
          "id": "us7000birm"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.3,
            "place": "39 km NW of Ovalle, Chile",
            "time": 1599355018850,
            "updated": 1603171112228,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000biqb",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000biqb&format=geojson",
            "felt": 111,
            "cdi": 5.1,
            "mmi": 6.256,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 667,
            "net": "us",
            "code": "7000biqb",
            "ids": ",us7000biqb,at00qg7q8a,pt20250001,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.344,
            "rms": 1.13,
            "gap": 32,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.3 - 39 km NW of Ovalle, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -71.4938,
              -30.3501,
              28.24
            ]
          },
          "id": "us7000biqb"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "133 km NW of Ternate, Indonesia",
            "time": 1599351670820,
            "updated": 1602129705229,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bipw",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bipw&format=geojson",
            "felt": 1,
            "cdi": 2,
            "mmi": 3.987,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "7000bipw",
            "ids": ",us7000bipw,pt20250000,at00qg7nne,",
            "sources": ",us,pt,at,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 1.2,
            "rms": 0.89,
            "gap": 20,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - 133 km NW of Ternate, Indonesia"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              126.5621,
              1.6686,
              30
            ]
          },
          "id": "us7000bipw"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.5,
            "place": "94 km NW of Vallenar, Chile",
            "time": 1598994557626,
            "updated": 1601919088040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bg4v",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bg4v&format=geojson",
            "felt": 52,
            "cdi": 5.3,
            "mmi": 6.056,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 678,
            "net": "us",
            "code": "7000bg4v",
            "ids": ",us7000bg4v,at00qg003e,pt20245003,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.39,
            "rms": 0.86,
            "gap": 49,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.5 - 94 km NW of Vallenar, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -71.3716,
              -27.9154,
              14.52
            ]
          },
          "id": "us7000bg4v"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.3,
            "place": "78 km NW of Vallenar, Chile",
            "time": 1598934602366,
            "updated": 1601935012065,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bfjx",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bfjx&format=geojson",
            "felt": 4,
            "cdi": 4.5,
            "mmi": 6.385,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 612,
            "net": "us",
            "code": "7000bfjx",
            "ids": ",us7000bfjx,pt20245001,",
            "sources": ",us,pt,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.248,
            "rms": 0.95,
            "gap": 69,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.3 - 78 km NW of Vallenar, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -71.28,
              -28.0355,
              17.65
            ]
          },
          "id": "us7000bfjx"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.8,
            "place": "86 km NW of Vallenar, Chile",
            "time": 1598933368475,
            "updated": 1601934923466,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bfjr",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bfjr&format=geojson",
            "felt": 260,
            "cdi": 5.4,
            "mmi": 6.77,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 1,
            "sig": 852,
            "net": "us",
            "code": "7000bfjr",
            "ids": ",at00qfyovo,pt20245000,us7000bfjr,",
            "sources": ",at,pt,us,",
            "types": ",dyfi,finite-fault,ground-failure,impact-link,impact-text,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 0.312,
            "rms": 0.87,
            "gap": 69,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.8 - 86 km NW of Vallenar, Chile"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -71.3086,
              -27.9705,
              21
            ]
          },
          "id": "us7000bfjr"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.9,
            "place": "Tristan da Cunha region",
            "time": 1598908682693,
            "updated": 1599455885689,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bfgl",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bfgl&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 536,
            "net": "us",
            "code": "7000bfgl",
            "ids": ",pt20244001,us7000bfgl,",
            "sources": ",pt,us,",
            "types": ",internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 3.122,
            "rms": 1.05,
            "gap": 31,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.9 - Tristan da Cunha region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -15.6138,
              -35.4385,
              10
            ]
          },
          "id": "us7000bfgl"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "Pacific-Antarctic Ridge",
            "time": 1598905688940,
            "updated": 1603838993040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bffs",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bffs&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "7000bffs",
            "ids": ",us7000bffs,",
            "sources": ",us,",
            "types": ",losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 31.196,
            "rms": 1.01,
            "gap": 53,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - Pacific-Antarctic Ridge"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -130.1777,
              -54.9769,
              10
            ]
          },
          "id": "us7000bffs"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.1,
            "place": "Chagos Archipelago region",
            "time": 1598894644946,
            "updated": 1599595993905,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bfbx",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bfbx&format=geojson",
            "felt": 7,
            "cdi": 4.3,
            "mmi": 0,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 575,
            "net": "us",
            "code": "7000bfbx",
            "ids": ",us7000bfbx,pt20244000,at00qfxuzz,",
            "sources": ",us,pt,at,",
            "types": ",dyfi,ground-failure,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 4.041,
            "rms": 1.28,
            "gap": 22,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.1 - Chagos Archipelago region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              70.1973,
              -4.0158,
              10
            ]
          },
          "id": "us7000bfbx"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 6.5,
            "place": "central Mid-Atlantic Ridge",
            "time": 1598822429757,
            "updated": 1599776581234,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000bf3k",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000bf3k&format=geojson",
            "felt": 2,
            "cdi": 4.3,
            "mmi": 4.817,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 651,
            "net": "us",
            "code": "7000bf3k",
            "ids": ",us7000bf3k,at00qfwba7,pt20243000,",
            "sources": ",us,at,pt,",
            "types": ",dyfi,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 15.394,
            "rms": 0.66,
            "gap": 31,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 6.5 - central Mid-Atlantic Ridge"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              -29.8656,
              0.7821,
              10
            ]
          },
          "id": "us7000bf3k"
        },
        {
          "type": "Feature",
          "properties": {
            "mag": 5.8,
            "place": "Bouvet Island region",
            "time": 1598581458132,
            "updated": 1603815033040,
            "tz": null,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000be5j",
            "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000be5j&format=geojson",
            "felt": null,
            "cdi": null,
            "mmi": 3.826,
            "alert": "green",
            "status": "reviewed",
            "tsunami": 0,
            "sig": 518,
            "net": "us",
            "code": "7000be5j",
            "ids": ",us7000be5j,",
            "sources": ",us,",
            "types": ",losspager,moment-tensor,origin,phase-data,shakemap,",
            "nst": null,
            "dmin": 17.048,
            "rms": 1.26,
            "gap": 40,
            "magType": "mww",
            "type": "earthquake",
            "title": "M 5.8 - Bouvet Island region"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              1.5112,
              -54.7928,
              10
            ]
          },
          "id": "us7000be5j"
        }
      ],
      "bbox": [
        -179.9645,
        -62.3735,
        9,
        179.8689,
        55.9704,
        633.92
      ]
    }



```python
max_magnitude = 0
max_long = 0
max_lat = 0
for earthquake in json_response["features"]:
    magnitude = earthquake["properties"]["mag"]
    print("----")
    print("Place:  " + earthquake["properties"]["place"])    
    print("Time:  " + str(earthquake["properties"]["time"]))    
    print("Mag:  " + str(magnitude))
    if (magnitude > max_magnitude):
        max_magnitude = magnitude
        max_long = earthquake["geometry"]["coordinates"][0]
        max_lat = earthquake["geometry"]["coordinates"][1]

print ("\nMaximum magnitude: " + str(max_magnitude))
    
```

    ----
    Place:  75 km NNE of Hihifo, Tonga
    Time:  1603626457004
    Mag:  5.9
    ----
    Place:  south of the Fiji Islands
    Time:  1603436672004
    Mag:  6.1
    ----
    Place:  West Chile Rise
    Time:  1603417577475
    Mag:  6
    ----
    Place:  148 km WNW of Haveluloto, Tonga
    Time:  1603355046992
    Mag:  5.8
    ----
    Place:  183 km ESE of Neiafu, Tonga
    Time:  1603239753928
    Mag:  5.9
    ----
    Place:  117 km SSE of Sand Point, Alaska
    Time:  1603143925888
    Mag:  5.9
    ----
    Place:  Easter Island region
    Time:  1602335697344
    Mag:  5.9
    ----
    Place:  86 km ESE of Kimbe, Papua New Guinea
    Time:  1602172729998
    Mag:  5.8
    ----
    Place:  38 km ENE of Kainantu, Papua New Guinea
    Time:  1602142532224
    Mag:  6.3
    ----
    Place:  233 km E of Levuka, Fiji
    Time:  1601979106688
    Mag:  6
    ----
    Place:  68 km SE of Sand Point, Alaska
    Time:  1601963690520
    Mag:  5.9
    ----
    Place:  South Shetland Islands
    Time:  1601633853188
    Mag:  5.8
    ----
    Place:  99 km W of Kandrian, Papua New Guinea
    Time:  1601548488481
    Mag:  6
    ----
    Place:  39 km NE of Pangai, Tonga
    Time:  1601514816524
    Mag:  6.4
    ----
    Place:  south of Africa
    Time:  1601140222462
    Mag:  6.1
    ----
    Place:  central East Pacific Rise
    Time:  1600695435082
    Mag:  5.8
    ----
    Place:  53 km E of Cortes, Philippines
    Time:  1600639995044
    Mag:  5.8
    ----
    Place:  central Mid-Atlantic Ridge
    Time:  1600465438936
    Mag:  6.9
    ----
    Place:  12 km SSE of Arkalochóri, Greece
    Time:  1600446497575
    Mag:  5.9
    ----
    Place:  157 km NNE of Labasa, Fiji
    Time:  1600143136291
    Mag:  6
    ----
    Place:  18 km WNW of Esso, Russia
    Time:  1600141288052
    Mag:  6.4
    ----
    Place:  Vanuatu
    Time:  1599899667322
    Mag:  5.9
    ----
    Place:  58 km SE of Ōfunato, Japan
    Time:  1599878651238
    Mag:  6.1
    ----
    Place:  82 km NNE of Tocopilla, Chile
    Time:  1599809757187
    Mag:  6.2
    ----
    Place:  187 km SE of Sarangani, Philippines
    Time:  1599635920225
    Mag:  5.8
    ----
    Place:  194 km SSE of Amahai, Indonesia
    Time:  1599525920801
    Mag:  5.9
    ----
    Place:  72 km NNE of Port-Vila, Vanuatu
    Time:  1599459159710
    Mag:  6
    ----
    Place:  17 km E of Talagutong, Philippines
    Time:  1599405823148
    Mag:  6.3
    ----
    Place:  central Mid-Atlantic Ridge
    Time:  1599375078848
    Mag:  6.7
    ----
    Place:  Vanuatu
    Time:  1599361156073
    Mag:  6.2
    ----
    Place:  39 km NW of Ovalle, Chile
    Time:  1599355018850
    Mag:  6.3
    ----
    Place:  133 km NW of Ternate, Indonesia
    Time:  1599351670820
    Mag:  5.9
    ----
    Place:  94 km NW of Vallenar, Chile
    Time:  1598994557626
    Mag:  6.5
    ----
    Place:  78 km NW of Vallenar, Chile
    Time:  1598934602366
    Mag:  6.3
    ----
    Place:  86 km NW of Vallenar, Chile
    Time:  1598933368475
    Mag:  6.8
    ----
    Place:  Tristan da Cunha region
    Time:  1598908682693
    Mag:  5.9
    ----
    Place:  Pacific-Antarctic Ridge
    Time:  1598905688940
    Mag:  5.8
    ----
    Place:  Chagos Archipelago region
    Time:  1598894644946
    Mag:  6.1
    ----
    Place:  central Mid-Atlantic Ridge
    Time:  1598822429757
    Mag:  6.5
    ----
    Place:  Bouvet Island region
    Time:  1598581458132
    Mag:  5.8
    
    Maximum magnitude: 6.9



```python
iss_response = requests.get("http://api.open-notify.org/iss-pass.json?lat="+str(max_lat)+"&lon="+str(max_lat))
time=iss_response.json()["response"][0]["risetime"]
print(datetime.fromtimestamp(time).strftime("%Y-%m-%d %I:%M:%S"))
```

    2020-10-27 05:40:15



```python

```
