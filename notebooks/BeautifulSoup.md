# Web Scraping with BeautifulSoup

### But first... what is HTML

**HyperText Markup Language**: it is NOT a programming language. As its name points it is a *markup language* is used to indicate to the browser how to layout content. 

HTML is based on tags, which indicates what should be done with the content.

The most basic tag is the `<html>`. Everything inside of it is HTML. **Important:** We need to use tags to delimit the scope, so we use open and close tags, like in the example:

```html
<html>
...
</html>
```

Inside of an `html` tag, we can use other tags. Usually, a HTML page has two other scopes defined by tags: `head` and `body`. The content of the web page goes into the body. The head contains metadata about the page, like the title of the page (it sometimes stores JS, CSSs, etc.)

When scrapping, we usually focus on what is inside of the `<body>  <\body>`

```html
<html>
   <head>
        ...
   </head>
   <body>
       ...
   </body>
</html>
```

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




    <html>
    <head>
    <!--
    		palette:
    		dark blue: #003F72
    		yellow: #FFD166
    		salmon: #EF476F
    		offwhite: #e7d7d7
    		Light Blue: #118AB2
    		Light green: #7DDF64
    		-->
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Python Programming Tutorials</title>
    <meta content="Python Programming tutorials from beginner to advanced on a massive variety of topics. All video and text tutorials are free." name="description"/>
    <link href="/static/favicon.ico" rel="shortcut icon"/>
    <link href="/static/css/materialize.min.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
    <meta content="3fLok05gk5gGtWd_VSXbSSSH27F2kr1QqcxYz9vYq2k" name="google-site-verification">
    <link href="/static/css/bootstrap.css" rel="stylesheet" type="text/css"/>
    <!-- Compiled and minified CSS -->
    <!-- Compiled and minified JavaScript -->
    <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js"></script>
    <style>
    		@media (min-width:992px) {
    		#aside {
    			width:250px;
    		}
    		pre { tab-size: 4;}
    		.btn {background-color:#FFD166;
    			  color:#000;
    		      height:auto;
    			  font-color:#000;
    			  }
    		.btn:hover {background-color:#FFD166;
    					}
    
    
    		</style>
    <!-- Google Tracking -->
    <script>
    			  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    			  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    			  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    			  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
                  ga('config', 'UA-51891827-1', {'anonymize_ip': true});﻿
    			  ga('create', 'UA-51891827-1', 'auto');
    			  ga('send', 'pageview');
    
    		</script>
    <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
                             (adsbygoogle = window.adsbygoogle || []).push({
                                  google_ad_client: "ca-pub-1579050400541873",
                                  enable_page_level_ads: true
                             });
                        </script>
    </meta></head>
    <body>
    <div class="navbar-fixed">
    <nav style="background-color:#003F72">
    <div class="nav-wrapper container">
    <a class="brand-logo" href="/"><img class="img-responsive" src="/static/images/mainlogowhitethick.jpg" style="width:50px; height;50px; margin-top:5px"/></a>
    <a class="button-collapse" data-activates="navsidebar" href="#"><i class="mdi-navigation-menu"></i></a>
    <ul class="right hide-on-med-and-down">
    <li><i class="material-icons">search</i></li>
    <li>
    <form action="/search/?l=hi" id="searchform" method="get" style="height:50px; padding-top:10px">
    <input id="search" name="q" placeholder="search" style="font-size:16px" type="search"/>
    </form>
    </li>
    <li><a href="/">Home</a></li>
    <li><a class="tooltipped" data-delay="50" data-position="bottom" data-tooltip="sudo apt-get upgrade" href="/+=1/">+=1</a></li>
    <!--<li><a href="/store/python-hoodie/">Store</a></li>-->
    <li><a href="/support/">Support the Content</a></li>
    <li><a href="https://goo.gl/7zgAVQ" target="blank"><!--<i class="material-icons">question_answer</i>-->Community</a></li>
    <li><a href="/login/">Log in</a></li>
    <li><a href="/register/">Sign up</a></li>
    </ul>
    <ul class="side-nav" id="navsidebar">
    <li>
    <form action="/search/?l=hi" id="searchform" method="get" style="height:50px; padding-top:10px">
    <input id="search" name="q" placeholder="search" style="font-size:16px" type="search"/>
    </form>
    </li>
    <li><a href="/">Home</a></li>
    <li><a class="tooltipped" data-delay="50" data-position="bottom" data-tooltip="sudo apt-get upgrade" href="/+=1/">+=1</a></li>
    <!--<li><a href="/store/python-hoodie/">Store</a></li>-->
    <li><a href="/support/">Support the Content</a></li>
    <li><a href="https://goo.gl/7zgAVQ" target="blank"><!--<i class="material-icons">question_answer</i>-->Community</a></li>
    <li><a href="/login/">Log in</a></li>
    <li><a href="/register/">Sign up</a></li>
    </ul>
    </div>
    </nav>
    </div>
    <!-- main content -->
    <div class="container" style="max-width:1500px; min-height:100%">
    <!--Notification:-->
    <!--<p style="font-size:80%">TensorFlow.js Livestream:  <a href="https://www.youtube.com/watch?v=NjSlj95lliM" target="blank"><strong>Deep Learning in the browser</strong></a></p>-->
    <!--End Notification:-->
    <script>Materialize.toast('Chat with us on Discord:<a href="https://discord.gg/sentdex" target="blank"><button style="margin-bottom:5px" class="btn btn-sm">Join</button></a>', 4000)</script>
    <div class="body">
    <p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>
    <p>The following table gives some general information for the following <code>programming languages</code>:</p>
    <ul>
    <li>Python</li>
    <li>Pascal</li>
    <li>Lisp</li>
    <li>D#</li>
    <li>Cobol</li>
    <li>Fortran</li>
    <li>Haskell</li>
    </ul>
    <table style="width:100%">
    <tr>
    <th>Program Name</th>
    <th>Internet Points</th>
    <th>Kittens?</th>
    </tr>
    <tr>
    <td>Python</td>
    <td>932914021</td>
    <td>Definitely</td>
    </tr>
    <tr>
    <td>Pascal</td>
    <td>532</td>
    <td>Unlikely</td>
    </tr>
    <tr>
    <td>Lisp</td>
    <td>1522</td>
    <td>Uncertain</td>
    </tr>
    <tr>
    <td>D#</td>
    <td>12</td>
    <td>Possibly</td>
    </tr>
    <tr>
    <td>Cobol</td>
    <td>3</td>
    <td>No.</td>
    </tr>
    <tr>
    <td>Fortran</td>
    <td>52124</td>
    <td>Yes.</td>
    </tr>
    <tr>
    <td>Haskell</td>
    <td>24</td>
    <td>lol.</td>
    </tr>
    </table>
    <p>I think it's clear that, on a scale of 1-10, python is:</p>
    <div class="card hoverable">
    <div class="card-content">
    <div class="card-title"></div>
    <img alt="omg batman" class="responsive-img" src="https://s-media-cache-ak0.pinimg.com/originals/e8/2a/ff/e82aff2876b080675449d0cef7685321.jpg">
    </img></div>
    </div>
    <p>Javascript (dynamic data) test:</p>
    <p class="jstest" id="yesnojs">y u bad tho?</p>
    <script>
         document.getElementById('yesnojs').innerHTML = 'Look at you shinin!';
      </script>
    <br/><br/>
    <pre>Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!</pre>
    <p>Whᶐt hαppéns now¿</p>
    <p><a href="/sitemap.xml" target="blank"><strong>sitemap</strong></a></p>
    </div></div></body>
    </html>
    
    <!--login modal-->
    <!--Register modal-->
    <script>
    			$(document).ready(function(){
    				$(".button-collapse").sideNav();
    				$('.modal-trigger').leanModal();
    				$('.collapsible').collapsible({
    				  accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    				});
    				$('#aside').pushpin({ top:110, bottom:500 });
    		  });
    		</script>
    <script>
    		  $(document).ready(function(){
    			$('.collapsible').collapsible({
    			  accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    			});
    			$('select').material_select();
    		  });
    	  </script>
    <script>
    		function goBack() {
    			window.history.back()
    		}
    	</script>
    <script src="/static/js/run_prettify.js" type="text/javascript"></script>
    
    <footer class="page-footer">
    <div class="container">
    <div class="row">
    <div class="col l6 s12">
    <h5 class="white-text">You've reached the end!</h5>
    <p class="grey-text text-lighten-4">Contact: Harrison@pythonprogramming.net.</p>
    <ul>
    <li><a class="grey-text text-lighten-3" href="/support-donate/">Support this Website!</a></li>
    <li><a class="grey-text text-lighten-3" href="/consulting/">Consulting and Contracting</a></li>
    <li><a class="grey-text text-lighten-3" href="https://www.facebook.com/pythonprogramming.net/">Facebook</a></li>
    <li><a class="grey-text text-lighten-3" href="https://twitter.com/sentdex">Twitter</a></li>
    <li><a class="grey-text text-lighten-3" href="https://instagram.com/sentdex">Instagram</a></li>
    </ul>
    </div>
    <div class="col l4 offset-l2 s12">
    <h6 class="white-text">Legal stuff:</h6>
    <ul>
    <li><a class="grey-text text-lighten-3" href="/about/tos/">Terms and Conditions</a></li>
    <li><a class="grey-text text-lighten-3" href="/about/privacy-policy/">Privacy Policy</a></li>
    </ul>
    </div>
    </div>
    </div>
    <a href="https://xkcd.com/353/" target="blank"><p class="grey-text right" style="padding-right:10px">Programming is a superpower.</p></a>
    <div class="footer-copyright">
    <div class="container">
                © OVER 9000! PythonProgramming.net
    
                </div>
    </div>
    </footer>




If we want, we can make it easier to read...


```python
print(soup.prettify())
```

    <html>
     <head>
      <!--
    		palette:
    		dark blue: #003F72
    		yellow: #FFD166
    		salmon: #EF476F
    		offwhite: #e7d7d7
    		Light Blue: #118AB2
    		Light green: #7DDF64
    		-->
      <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
      <title>
       Python Programming Tutorials
      </title>
      <meta content="Python Programming tutorials from beginner to advanced on a massive variety of topics. All video and text tutorials are free." name="description"/>
      <link href="/static/favicon.ico" rel="shortcut icon"/>
      <link href="/static/css/materialize.min.css" rel="stylesheet"/>
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
      <meta content="3fLok05gk5gGtWd_VSXbSSSH27F2kr1QqcxYz9vYq2k" name="google-site-verification">
       <link href="/static/css/bootstrap.css" rel="stylesheet" type="text/css"/>
       <!-- Compiled and minified CSS -->
       <!-- Compiled and minified JavaScript -->
       <script src="https://code.jquery.com/jquery-2.1.4.min.js">
       </script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.3/js/materialize.min.js">
       </script>
       <style>
        @media (min-width:992px) {
    		#aside {
    			width:250px;
    		}
    		pre { tab-size: 4;}
    		.btn {background-color:#FFD166;
    			  color:#000;
    		      height:auto;
    			  font-color:#000;
    			  }
    		.btn:hover {background-color:#FFD166;
    					}
       </style>
       <!-- Google Tracking -->
       <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    			  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    			  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    			  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
                  ga('config', 'UA-51891827-1', {'anonymize_ip': true});﻿
    			  ga('create', 'UA-51891827-1', 'auto');
    			  ga('send', 'pageview');
       </script>
       <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js">
       </script>
       <script>
        (adsbygoogle = window.adsbygoogle || []).push({
                                  google_ad_client: "ca-pub-1579050400541873",
                                  enable_page_level_ads: true
                             });
       </script>
      </meta>
     </head>
     <body>
      <div class="navbar-fixed">
       <nav style="background-color:#003F72">
        <div class="nav-wrapper container">
         <a class="brand-logo" href="/">
          <img class="img-responsive" src="/static/images/mainlogowhitethick.jpg" style="width:50px; height;50px; margin-top:5px"/>
         </a>
         <a class="button-collapse" data-activates="navsidebar" href="#">
          <i class="mdi-navigation-menu">
          </i>
         </a>
         <ul class="right hide-on-med-and-down">
          <li>
           <i class="material-icons">
            search
           </i>
          </li>
          <li>
           <form action="/search/?l=hi" id="searchform" method="get" style="height:50px; padding-top:10px">
            <input id="search" name="q" placeholder="search" style="font-size:16px" type="search"/>
           </form>
          </li>
          <li>
           <a href="/">
            Home
           </a>
          </li>
          <li>
           <a class="tooltipped" data-delay="50" data-position="bottom" data-tooltip="sudo apt-get upgrade" href="/+=1/">
            +=1
           </a>
          </li>
          <!--<li><a href="/store/python-hoodie/">Store</a></li>-->
          <li>
           <a href="/support/">
            Support the Content
           </a>
          </li>
          <li>
           <a href="https://goo.gl/7zgAVQ" target="blank">
            <!--<i class="material-icons">question_answer</i>-->
            Community
           </a>
          </li>
          <li>
           <a href="/login/">
            Log in
           </a>
          </li>
          <li>
           <a href="/register/">
            Sign up
           </a>
          </li>
         </ul>
         <ul class="side-nav" id="navsidebar">
          <li>
           <form action="/search/?l=hi" id="searchform" method="get" style="height:50px; padding-top:10px">
            <input id="search" name="q" placeholder="search" style="font-size:16px" type="search"/>
           </form>
          </li>
          <li>
           <a href="/">
            Home
           </a>
          </li>
          <li>
           <a class="tooltipped" data-delay="50" data-position="bottom" data-tooltip="sudo apt-get upgrade" href="/+=1/">
            +=1
           </a>
          </li>
          <!--<li><a href="/store/python-hoodie/">Store</a></li>-->
          <li>
           <a href="/support/">
            Support the Content
           </a>
          </li>
          <li>
           <a href="https://goo.gl/7zgAVQ" target="blank">
            <!--<i class="material-icons">question_answer</i>-->
            Community
           </a>
          </li>
          <li>
           <a href="/login/">
            Log in
           </a>
          </li>
          <li>
           <a href="/register/">
            Sign up
           </a>
          </li>
         </ul>
        </div>
       </nav>
      </div>
      <!-- main content -->
      <div class="container" style="max-width:1500px; min-height:100%">
       <!--Notification:-->
       <!--<p style="font-size:80%">TensorFlow.js Livestream:  <a href="https://www.youtube.com/watch?v=NjSlj95lliM" target="blank"><strong>Deep Learning in the browser</strong></a></p>-->
       <!--End Notification:-->
       <script>
        Materialize.toast('Chat with us on Discord:<a href="https://discord.gg/sentdex" target="blank"><button style="margin-bottom:5px" class="btn btn-sm">Join</button></a>', 4000)
       </script>
       <div class="body">
        <p class="introduction">
         Oh, hello! This is a
         <span style="font-size:115%">
          wonderful
         </span>
         page meant to let you practice web scraping. This page was originally created to help people work with the
         <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank">
          <strong>
           Beautiful Soup 4
          </strong>
         </a>
         library.
        </p>
        <p>
         The following table gives some general information for the following
         <code>
          programming languages
         </code>
         :
        </p>
        <ul>
         <li>
          Python
         </li>
         <li>
          Pascal
         </li>
         <li>
          Lisp
         </li>
         <li>
          D#
         </li>
         <li>
          Cobol
         </li>
         <li>
          Fortran
         </li>
         <li>
          Haskell
         </li>
        </ul>
        <table style="width:100%">
         <tr>
          <th>
           Program Name
          </th>
          <th>
           Internet Points
          </th>
          <th>
           Kittens?
          </th>
         </tr>
         <tr>
          <td>
           Python
          </td>
          <td>
           932914021
          </td>
          <td>
           Definitely
          </td>
         </tr>
         <tr>
          <td>
           Pascal
          </td>
          <td>
           532
          </td>
          <td>
           Unlikely
          </td>
         </tr>
         <tr>
          <td>
           Lisp
          </td>
          <td>
           1522
          </td>
          <td>
           Uncertain
          </td>
         </tr>
         <tr>
          <td>
           D#
          </td>
          <td>
           12
          </td>
          <td>
           Possibly
          </td>
         </tr>
         <tr>
          <td>
           Cobol
          </td>
          <td>
           3
          </td>
          <td>
           No.
          </td>
         </tr>
         <tr>
          <td>
           Fortran
          </td>
          <td>
           52124
          </td>
          <td>
           Yes.
          </td>
         </tr>
         <tr>
          <td>
           Haskell
          </td>
          <td>
           24
          </td>
          <td>
           lol.
          </td>
         </tr>
        </table>
        <p>
         I think it's clear that, on a scale of 1-10, python is:
        </p>
        <div class="card hoverable">
         <div class="card-content">
          <div class="card-title">
          </div>
          <img alt="omg batman" class="responsive-img" src="https://s-media-cache-ak0.pinimg.com/originals/e8/2a/ff/e82aff2876b080675449d0cef7685321.jpg">
          </img>
         </div>
        </div>
        <p>
         Javascript (dynamic data) test:
        </p>
        <p class="jstest" id="yesnojs">
         y u bad tho?
        </p>
        <script>
         document.getElementById('yesnojs').innerHTML = 'Look at you shinin!';
        </script>
        <br/>
        <br/>
        <pre>Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!</pre>
        <p>
         Whᶐt hαppéns now¿
        </p>
        <p>
         <a href="/sitemap.xml" target="blank">
          <strong>
           sitemap
          </strong>
         </a>
        </p>
       </div>
      </div>
     </body>
    </html>
    <!--login modal-->
    <!--Register modal-->
    <script>
     $(document).ready(function(){
    				$(".button-collapse").sideNav();
    				$('.modal-trigger').leanModal();
    				$('.collapsible').collapsible({
    				  accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    				});
    				$('#aside').pushpin({ top:110, bottom:500 });
    		  });
    </script>
    <script>
     $(document).ready(function(){
    			$('.collapsible').collapsible({
    			  accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    			});
    			$('select').material_select();
    		  });
    </script>
    <script>
     function goBack() {
    			window.history.back()
    		}
    </script>
    <script src="/static/js/run_prettify.js" type="text/javascript">
    </script>
    <footer class="page-footer">
     <div class="container">
      <div class="row">
       <div class="col l6 s12">
        <h5 class="white-text">
         You've reached the end!
        </h5>
        <p class="grey-text text-lighten-4">
         Contact: Harrison@pythonprogramming.net.
        </p>
        <ul>
         <li>
          <a class="grey-text text-lighten-3" href="/support-donate/">
           Support this Website!
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="/consulting/">
           Consulting and Contracting
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://www.facebook.com/pythonprogramming.net/">
           Facebook
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://twitter.com/sentdex">
           Twitter
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://instagram.com/sentdex">
           Instagram
          </a>
         </li>
        </ul>
       </div>
       <div class="col l4 offset-l2 s12">
        <h6 class="white-text">
         Legal stuff:
        </h6>
        <ul>
         <li>
          <a class="grey-text text-lighten-3" href="/about/tos/">
           Terms and Conditions
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="/about/privacy-policy/">
           Privacy Policy
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
     <a href="https://xkcd.com/353/" target="blank">
      <p class="grey-text right" style="padding-right:10px">
       Programming is a superpower.
      </p>
     </a>
     <div class="footer-copyright">
      <div class="container">
       © OVER 9000! PythonProgramming.net
      </div>
     </div>
    </footer>
    


We can use multiple attributes/methods depending on what we wanna scrape/get!


```python
print(soup.title)
```

    <title>Python Programming Tutorials</title>


We can deal with soup.title (which is a Tag object), getting name, content, parent, etc...


```python
print(soup.title.name)
```

    title



```python
print(soup.title.string)
```

    Python Programming Tutorials



```python
print(soup.title.parent.name)
```

    head



```python
print(soup.p)
```

    <p class="introduction">Oh, hello! This is a <span style="font-size:115%">wonderful</span> page meant to let you practice web scraping. This page was originally created to help people work with the <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="blank"><strong>Beautiful Soup 4</strong></a> library.</p>



```python
soup.p['class']
```




    ['introduction']



We can find all the items with the same Tag, and get them as an iterable object


```python
all_para = soup.find_all('p')
print(type(all_para[1]))
```

    <class 'bs4.element.Tag'>


We can even iterate :-) (+ text vs. string)


```python
for para in all_para:
    print(para.string)
    print(str(para.text))
    print("----")
```

    None
    Oh, hello! This is a wonderful page meant to let you practice web scraping. This page was originally created to help people work with the Beautiful Soup 4 library.
    ----
    None
    The following table gives some general information for the following programming languages:
    ----
    I think it's clear that, on a scale of 1-10, python is:
    I think it's clear that, on a scale of 1-10, python is:
    ----
    Javascript (dynamic data) test:
    Javascript (dynamic data) test:
    ----
    y u bad tho?
    y u bad tho?
    ----
    Whᶐt hαppéns now¿
    Whᶐt hαppéns now¿
    ----
    sitemap
    sitemap
    ----
    Contact: Harrison@pythonprogramming.net.
    Contact: Harrison@pythonprogramming.net.
    ----
    Programming is a superpower.
    Programming is a superpower.
    ----



```python
links = soup.find_all('a')
print(links[2])
for url in links:
    print(url.text)
    print(url.get('href'))
    print(url.get('class'))
    print("---")

```

    <a href="/">Home</a>
    
    /
    ['brand-logo']
    ---
    
    #
    ['button-collapse']
    ---
    Home
    /
    None
    ---
    +=1
    /+=1/
    ['tooltipped']
    ---
    Support the Content
    /support/
    None
    ---
    Community
    https://goo.gl/7zgAVQ
    None
    ---
    Log in
    /login/
    None
    ---
    Sign up
    /register/
    None
    ---
    Home
    /
    None
    ---
    +=1
    /+=1/
    ['tooltipped']
    ---
    Support the Content
    /support/
    None
    ---
    Community
    https://goo.gl/7zgAVQ
    None
    ---
    Log in
    /login/
    None
    ---
    Sign up
    /register/
    None
    ---
    Beautiful Soup 4
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    None
    ---
    sitemap
    /sitemap.xml
    None
    ---
    Support this Website!
    /support-donate/
    ['grey-text', 'text-lighten-3']
    ---
    Consulting and Contracting
    /consulting/
    ['grey-text', 'text-lighten-3']
    ---
    Facebook
    https://www.facebook.com/pythonprogramming.net/
    ['grey-text', 'text-lighten-3']
    ---
    Twitter
    https://twitter.com/sentdex
    ['grey-text', 'text-lighten-3']
    ---
    Instagram
    https://instagram.com/sentdex
    ['grey-text', 'text-lighten-3']
    ---
    Terms and Conditions
    /about/tos/
    ['grey-text', 'text-lighten-3']
    ---
    Privacy Policy
    /about/privacy-policy/
    ['grey-text', 'text-lighten-3']
    ---
    Programming is a superpower.
    https://xkcd.com/353/
    None
    ---



```python
divs = soup.find_all('div', attrs={"class": "container", "style":"max-width:1500px; min-height:100%"})
len(divs)
```




    1




```python
body = soup.find('div',attrs={"class":"body", })
print(body.prettify())

```


      File "<ipython-input-66-ff5aca60cfbd>", line 1
        body = soup.find('div',attrs={"class":"body", "style":"max-width:1500px; min-height:100%})
                                                                                                  ^
    SyntaxError: EOL while scanning string literal




```python
footer = soup.find('footer')
print(footer.prettify())
```

    <footer class="page-footer">
     <div class="container">
      <div class="row">
       <div class="col l6 s12">
        <h5 class="white-text">
         You've reached the end!
        </h5>
        <p class="grey-text text-lighten-4">
         Contact: Harrison@pythonprogramming.net.
        </p>
        <ul>
         <li>
          <a class="grey-text text-lighten-3" href="/support-donate/">
           Support this Website!
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="/consulting/">
           Consulting and Contracting
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://www.facebook.com/pythonprogramming.net/">
           Facebook
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://twitter.com/sentdex">
           Twitter
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="https://instagram.com/sentdex">
           Instagram
          </a>
         </li>
        </ul>
       </div>
       <div class="col l4 offset-l2 s12">
        <h6 class="white-text">
         Legal stuff:
        </h6>
        <ul>
         <li>
          <a class="grey-text text-lighten-3" href="/about/tos/">
           Terms and Conditions
          </a>
         </li>
         <li>
          <a class="grey-text text-lighten-3" href="/about/privacy-policy/">
           Privacy Policy
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
     <a href="https://xkcd.com/353/" target="blank">
      <p class="grey-text right" style="padding-right:10px">
       Programming is a superpower.
      </p>
     </a>
     <div class="footer-copyright">
      <div class="container">
       © OVER 9000! PythonProgramming.net
      </div>
     </div>
    </footer>
    



```python
for child in footer.children:
    print(child)
    print("---")
```

    
    
    ---
    <div class="container">
    <div class="row">
    <div class="col l6 s12">
    <h5 class="white-text">You've reached the end!</h5>
    <p class="grey-text text-lighten-4">Contact: Harrison@pythonprogramming.net.</p>
    <ul>
    <li><a class="grey-text text-lighten-3" href="/support-donate/">Support this Website!</a></li>
    <li><a class="grey-text text-lighten-3" href="/consulting/">Consulting and Contracting</a></li>
    <li><a class="grey-text text-lighten-3" href="https://www.facebook.com/pythonprogramming.net/">Facebook</a></li>
    <li><a class="grey-text text-lighten-3" href="https://twitter.com/sentdex">Twitter</a></li>
    <li><a class="grey-text text-lighten-3" href="https://instagram.com/sentdex">Instagram</a></li>
    </ul>
    </div>
    <div class="col l4 offset-l2 s12">
    <h6 class="white-text">Legal stuff:</h6>
    <ul>
    <li><a class="grey-text text-lighten-3" href="/about/tos/">Terms and Conditions</a></li>
    <li><a class="grey-text text-lighten-3" href="/about/privacy-policy/">Privacy Policy</a></li>
    </ul>
    </div>
    </div>
    </div>
    ---
    
    
    ---
    <a href="https://xkcd.com/353/" target="blank"><p class="grey-text right" style="padding-right:10px">Programming is a superpower.</p></a>
    ---
    
    
    ---
    <div class="footer-copyright">
    <div class="container">
                © OVER 9000! PythonProgramming.net
    
                </div>
    </div>
    ---
    
    
    ---



```python
len(list(body.children))
```




    28




```python
body.find('a')

```


```python
for item in body.findAll('a') :
    print(item.string + " is a link to " + item.get('href'))
    if (item.has_attr('target')):
        print("target is: " + item.get("target"))
```


```python
body.findAll('div')
```


```python
body.findAll('img')
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
response = requests.get('https://github.com/igorsteinmacher/')
content = response.content
soup=BeautifulSoup(content, "html.parser")
soup
```




    
    <!DOCTYPE html>
    
    <html lang="en">
    <head>
    <meta charset="utf-8"/>
    <link href="https://github.githubassets.com" rel="dns-prefetch"/>
    <link href="https://avatars0.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars1.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars2.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://avatars3.githubusercontent.com" rel="dns-prefetch"/>
    <link href="https://github-cloud.s3.amazonaws.com" rel="dns-prefetch"/>
    <link href="https://user-images.githubusercontent.com/" rel="dns-prefetch"/>
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/frameworks-2b0800d93d72358b528dc71d5a482020.css" integrity="sha512-KwgA2T1yNYtSjccdWkggIHevOjkIgZqdsUtA0GyLMFalickiFVC+1RUh0JVQ5/gWaj/HQ/p5JIbABYtB68iwcQ==" media="all" rel="stylesheet">
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/site-81b8499d5fa110569cb6fa2fe68c5b52.css" integrity="sha512-gbhJnV+hEFactvov5oxbUhQzmfVk0Hq4beAJ8JMPi0mlKB6T+7scqcQA9vQQ4hD/LCKAiTprFfkL2MejRkywkA==" media="all" rel="stylesheet">
    <link crossorigin="anonymous" href="https://github.githubassets.com/assets/github-cb3321b77abe760fce00b7db3d9fc94c.css" integrity="sha512-yzMht3q+dg/OALfbPZ/JTIDob9Ut0TQ4cFkxNYUs7A9nIXUaeSw1f5CGL5hAXuZ4hqkSjE8ll9ZwNR43/RR1ew==" media="all" rel="stylesheet">
    <script crossorigin="anonymous" defer="defer" integrity="sha512-8K2vvwbW+6H27Nad5ydg8PA2/aMD/LKq+EiK9s0U0hhVZxCI2tWBsYk9beAtisRw2j+Or5k2/F+6dk02nmj/PA==" src="https://github.githubassets.com/assets/environment-f0adafbf.js" type="application/javascript"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-YftqjDO3D+bLwgkQdcNXayWNyGE2X+VQ04LXwM3FcfbTXrEGy6Gpo7QNfnZ/ewGrGC5zbGiA286vIf37MKm0NA==" src="https://github.githubassets.com/assets/chunk-frameworks-61fb6a8c.js" type="application/javascript"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Shix6Hkv5DNREArBi1dz6K2Dezl6x88FzVNzPUHKbjuk6iZAuHacGedCwe/1YQtFhf8DzLIIDhr1Sb41uwiIXg==" src="https://github.githubassets.com/assets/chunk-vendor-4a18b1e8.js" type="application/javascript"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-McL56abCjFGYqTr8S72dU21rns1EOJmDDFcaRrHQmIugbXAz4LRTxXQPyiJHDCHI7qGofFJiBAqx2U+e8xF+og==" src="https://github.githubassets.com/assets/behaviors-31c2f9e9.js" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/chunk-contributions-spider-graph-3f660c92.js" defer="defer" integrity="sha512-P2YMkqfXJOOfxTTkNHbblY5ks3U+e9w9tiVyK9syrE5+JmlaCg1kUiuT1DfbyJXwaOLaRLT3zam2r+QrxTZ3iw==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-drag-drop.js" data-src="https://github.githubassets.com/assets/chunk-drag-drop-2430c5f1.js" defer="defer" integrity="sha512-JDDF8W8Wl5vopo9t4K4NtIEUMCYov3ZjVpv9lC1SDUxhejU+ILu8V3l6BhkaIRMYJioQWj9am9tJSTvND+8wJg==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-jump-to.js" data-src="https://github.githubassets.com/assets/chunk-jump-to-9e8fa354.js" defer="defer" integrity="sha512-no+jVC1jE6jD3Zau5xnnQ1qovueGndLuXLWyqtlyO7SDS1bXrNEjrebU4mb+tY2vvYYru+krGpI3hL9tkbM5kg==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-profile-pins-element.js" data-src="https://github.githubassets.com/assets/chunk-profile-pins-element-b5c1f8c4.js" defer="defer" integrity="sha512-tcH4xCRuMBAh1PruDaiwGnRIbHlF6bGLhxyCQ16uqok1cV5QFMguVPWJtN9KI0jGQOgN+Pha3+uOUXhXdfK/qw==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-randomColor.js" data-src="https://github.githubassets.com/assets/chunk-randomColor-80fc776d.js" defer="defer" integrity="sha512-gPx3bYhTjyC83X5u5KlEDJpwGAHt3AC2p5s9iMuAfPTeSj7kHlKMW231C3K3c7+jvlpWpELk8DJsefrYdRzqjA==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-runner-groups.js" data-src="https://github.githubassets.com/assets/chunk-runner-groups-13e1fec0.js" defer="defer" integrity="sha512-E+H+wAtjiqutBvn2cnXzDIvmasIhYiS7i7JzOfFUwo+Ej8zT54OrJtP//RhwixnypgOpCF4JvqzYy6zOtORDmg==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-sortable-behavior.js" data-src="https://github.githubassets.com/assets/chunk-sortable-behavior-a9d88290.js" defer="defer" integrity="sha512-qdiCkJPPR4LxwUKftEmJe2v79E8xnTceYqylsWkMsGuARkiKkX9iFNwkvZJ3bDfS5YHSPD3+k+N2/I73tvlL1Q==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-tweetsodium.js" data-src="https://github.githubassets.com/assets/chunk-tweetsodium-3695118c.js" defer="defer" integrity="sha512-NpURjBPyJ0JT8hWOMbLErYNeb0bTkKfmFX1hl1F8C/q6jckqWObeOzEAcs6TRlj+cqAR6GDohEBxDgkYBlx+QQ==" type="application/javascript"></script>
    <script crossorigin="anonymous" data-module-id="./chunk-user-status-submit.js" data-src="https://github.githubassets.com/assets/chunk-user-status-submit-8bfa15b9.js" defer="defer" integrity="sha512-i/oVuQCFzcV49ZAwOjQ0Q6hnafj5zU2pTOqeNPwA7YylWWWtSld/uttlua/+MbeQmwRD1+2qoFkWl5gSstHsew==" type="application/javascript"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-c3tb1KFn4+bFvyDfLbcSPfl55X7g48vBuqgSDaXOhArQvWPW4AxmkHajZOKz3Qzx/ZxT+0VRGd3Zh2bYoSxJ2w==" src="https://github.githubassets.com/assets/profile-737b5bd4.js" type="application/javascript"></script>
    <meta content="width=device-width" name="viewport"/>
    <title>igorsteinmacher (Igor Steinmacher) · GitHub</title>
    <meta content="Assistant Professor @ NAU.
    Researcher: Mining Software Repositories and behavior in Open Source are my main topics - igorsteinmacher" name="description"/>
    <link href="/opensearch.xml" rel="search" title="GitHub" type="application/opensearchdescription+xml"/>
    <link href="https://github.com/fluidicon.png" rel="fluid-icon" title="GitHub"/>
    <meta content="1401488693436528" property="fb:app_id"/>
    <meta content="app-id=1477376905" name="apple-itunes-app">
    <meta content="https://avatars1.githubusercontent.com/u/2953768?s=400&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" name="twitter:image:src"><meta content="@github" name="twitter:site"><meta content="summary" name="twitter:card"><meta content="igorsteinmacher - Overview" name="twitter:title"/><meta content="Assistant Professor @ NAU.
    Researcher: Mining Software Repositories and behavior in Open Source are my main topics - igorsteinmacher" name="twitter:description"/>
    <meta content="https://avatars1.githubusercontent.com/u/2953768?s=400&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" property="og:image"/><meta content="GitHub" property="og:site_name"/><meta content="profile" property="og:type"/><meta content="igorsteinmacher - Overview" property="og:title"/><meta content="https://github.com/igorsteinmacher" property="og:url"/><meta content="Assistant Professor @ NAU.
    Researcher: Mining Software Repositories and behavior in Open Source are my main topics - igorsteinmacher" property="og:description"/><meta content="igorsteinmacher" property="profile:username"/>
    <link href="https://github.githubassets.com/" rel="assets"/>
    <meta content="FB3C:7162:10D52F:1C5B48:5F9B41FE" data-pjax-transient="true" name="request-id"/><meta content="f1958bc7d1d7ce084bdb44c7d128aa482d08942c" data-pjax-transient="true" name="html-safe-nonce"/><meta content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJGQjNDOjcxNjI6MTBENTJGOjFDNUI0ODo1RjlCNDFGRSIsInZpc2l0b3JfaWQiOiI2NDEyNTk4NjcyMzMzOTQ3MzkxIiwicmVnaW9uX2VkZ2UiOiJpYWQiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-pjax-transient="true" name="visitor-payload"/><meta content="96fd3d8b585664c1e6da5291e8699676aca96e41f338cb82bbd906de42869014" data-pjax-transient="true" name="visitor-hmac"/><meta content="false" data-pjax-transient="true" name="cookie-consent-required"/>
    <meta content="" data-pjax-transient="true" name="github-keyboard-shortcuts"/>
    <meta data-pjax-transient="" name="selected-link" value="/igorsteinmacher"/>
    <meta content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY" name="google-site-verification"/>
    <meta content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU" name="google-site-verification"/>
    <meta content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA" name="google-site-verification"/>
    <meta content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc" name="google-site-verification"/>
    <meta content="collector.githubapp.com" name="octolytics-host"><meta content="github" name="octolytics-app-id"><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url"><meta class="js-octo-ga-id" content="" name="octolytics-dimension-ga_id">
    <meta content="/&lt;user-name&gt;" data-pjax-transient="true" name="analytics-location">
    <meta content="UA-3769691-2" name="google-analytics"/>
    <meta class="js-ga-set" content="Responsive" data-pjax-transient="" name="dimension10"/>
    <meta class="js-ga-set" content="Logged Out" name="dimension1"/>
    <meta content="github.com" name="hostname"/>
    <meta content="" name="user-login"/>
    <meta content="github.com" name="expected-hostname"/>
    <meta content="MARKETPLACE_PENDING_INSTALLATIONS" name="enabled-features"/>
    <meta content="b9b9a6cd9020fd294e749174360057b62dc991426611a59772a02f58839eb8da" http-equiv="x-pjax-version"/>
    <meta content="https://api.github.com/_private/browser/stats" name="browser-stats-url"/>
    <meta content="https://api.github.com/_private/browser/errors" name="browser-errors-url"/>
    <meta content="https://api.github.com/_private/browser/optimizely_client/errors" name="browser-optimizely-client-errors-url"/>
    <link color="#000000" href="https://github.githubassets.com/pinned-octocat.svg" rel="mask-icon"/>
    <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.png" rel="alternate icon" type="image/png"/>
    <link class="js-site-favicon" href="https://github.githubassets.com/favicons/favicon.svg" rel="icon" type="image/svg+xml"/>
    <meta content="#1e2327" name="theme-color"/>
    <link crossorigin="use-credentials" href="/manifest.json" rel="manifest"/>
    </meta></meta></meta></meta></meta></meta></meta></meta></meta></link></link></link></head>
    <body class="logged-out env-production page-responsive page-profile">
    <div class="position-relative js-header-wrapper">
    <a class="px-2 py-4 bg-blue text-white show-on-focus js-skip-to-content" href="#start-of-content">Skip to content</a>
    <span class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed">
    <span class="Progress-item progress-pjax-loader-bar" style="background-color: #79b8ff;width: 0%;"></span>
    </span>
    <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
    <div class="container-xl d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
    <a aria-label="Homepage" class="mr-4" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/">
    <svg aria-hidden="true" class="octicon octicon-mark-github text-white" height="32" version="1.1" viewbox="0 0 16 16" width="32"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
    </a>
    <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
    </div>
    <div class="d-flex flex-items-center">
    <a class="d-inline-block d-lg-none f5 text-white no-underline border border-gray-dark rounded-2 px-2 py-1 mr-3 mr-sm-5" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"site header","repository_id":null,"auth_type":"SIGN_UP","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="a2aaebac3ea071571c2667a6d347e840c19f139e38e403c7fb54513a56d87807" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E&amp;source=header">
                    Sign up
                  </a>
    <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link d-lg-none mt-1 js-details-target" type="button">
    <svg aria-hidden="true" class="octicon octicon-three-bars text-white" height="24" version="1.1" viewbox="0 0 16 16" width="24"><path d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z" fill-rule="evenodd"></path></svg>
    </button>
    </div>
    </div>
    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
    <div class="d-flex d-lg-none flex-justify-end border-bottom bg-gray-light p-3">
    <button aria-expanded="false" aria-label="Toggle navigation" class="btn-link js-details-target" type="button">
    <svg aria-hidden="true" class="octicon octicon-x text-gray" height="24" version="1.1" viewbox="0 0 24 24" width="24"><path d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg>
    </button>
    </div>
    <nav aria-label="Global" class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0">
    <ul class="d-lg-flex list-style-none">
    <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                        Why GitHub?
                        <svg class="icon-chevon-down-mktg position-absolute position-lg-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
    <a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features" href="/features">Features <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a>
    <ul class="list-style-none f5 pb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code review" href="/features/code-review/">Code review</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Project management" href="/features/project-management/">Project management</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Integrations" href="/features/integrations">Integrations</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Actions" href="/features/actions">Actions</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Packages" href="/features/packages">Packages</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Security" href="/features/security">Security</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Team management" href="/features#team-management">Team management</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Code hosting" href="/features#hosting">Hosting</a></li>
    <li class="edge-item-fix hide-xl"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Mobile" href="/mobile">Mobile</a></li>
    </ul>
    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories" href="/customer-stories">Customer stories <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Security" href="/security">Security <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    </div>
    </details>
    </li>
    <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Team" href="/team">Team</a>
    </li>
    <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise" href="/enterprise">Enterprise</a>
    </li>
    <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                        Explore
                        <svg class="icon-chevon-down-mktg position-absolute position-lg-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore" href="/explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn &amp; contribute</h4>
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Topics" href="/topics">Topics</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Collections" href="/collections">Collections</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Trending" href="/trending">Trending</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Learning lab" href="https://lab.github.com/">Learning Lab</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Open source guides" href="https://opensource.guide">Open source guides</a></li>
    </ul>
    <h4 class="text-gray-light text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
    <ul class="list-style-none mb-0">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Events" href="https://github.com/events">Events</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Community forum" href="https://github.community">Community forum</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Education" href="https://education.github.com">GitHub Education</a></li>
    <li class="edge-item-fix"><a class="py-2 pb-0 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to GitHub Stars Program" href="https://stars.github.com">GitHub Stars program</a></li>
    </ul>
    </div>
    </details>
    </li>
    <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
    <a class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace" href="/marketplace">Marketplace</a>
    </li>
    <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center">
    <details class="HeaderMenu-details details-overlay details-reset width-full">
    <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                        Pricing
                        <svg class="icon-chevon-down-mktg position-absolute position-lg-relative" fill="none" viewbox="0 0 14 8" x="0px" xml:space="preserve" y="0px">
    <path d="M1,1l6.2,6L13,1"></path>
    </svg>
    </summary>
    <div class="dropdown-menu flex-auto rounded-1 bg-white px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
    <a class="pb-2 lh-condensed-ultra d-block link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing" href="/pricing">Plans <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a>
    <ul class="list-style-none mb-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Compare plans" href="/pricing#feature-comparison">Compare plans</a></li>
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block link-gray no-underline f5" data-ga-click="(Logged out) Header, go to Contact Sales" href="https://enterprise.github.com/contact">Contact Sales</a></li>
    </ul>
    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
    <li class="edge-item-fix"><a class="py-2 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Nonprofits" href="/nonprofit">Nonprofit <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    <li class="edge-item-fix"><a class="py-2 pb-0 lh-condensed-ultra d-block no-underline link-gray-dark no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education" href="https://education.github.com">Education <span class="Bump-link-symbol float-right text-normal text-gray-light">→</span></a></li>
    </ul>
    </div>
    </details>
    </li>
    </ul>
    </nav>
    <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
    <div class="d-lg-flex mb-3 mb-lg-0">
    <div aria-expanded="false" aria-haspopup="listbox" aria-label="Search or jump to" aria-owns="jump-to-results" class="header-search flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to" role="combobox">
    <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></div></div></div></div></div></div></header></div></body></html><form accept-charset="UTF-8" action="/users/igorsteinmacher/search" aria-label="Site" class="js-site-search-form" data-scope-id="2953768" data-scope-type="User" data-scoped-search-url="/users/igorsteinmacher/search" data-unscoped-search-url="/search" method="get" role="search">
    <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
    <input aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" autocapitalize="off" autocomplete="off" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-scoped-placeholder="Search" data-unscoped-placeholder="Search GitHub" name="q" placeholder="Search" spellcheck="false" type="text" value=""/>
    <input class="js-data-jump-to-suggestions-path-csrf" data-csrf="true" type="hidden" value="i39DC4v8fremSXKL9ZF/EjGIex0AC18EBtFax60EotZnNFzR9zXTNW41Ye2vaC7OKR2VQ2WT+pZyyvoKImPC7Q==">
    <input class="js-site-search-type-field" name="type" type="hidden"/>
    <img alt="" class="mr-2 header-search-key-slash" src="https://github.githubassets.com/images/search-key-slash.svg"/>
    <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
    <ul class="d-none js-jump-to-suggestions-template-container">
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this user" class="js-jump-to-badge-search-text-default d-none">
            In this user
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    </ul>
    <ul class="d-none js-jump-to-no-results-template-container">
    <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
    </li>
    </ul>
    <ul class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container" id="jump-to-results" role="listbox">
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this user" class="js-jump-to-badge-search-text-default d-none">
            In this user
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
    <a class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="" tabindex="-1">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
    <svg aria-label="Repository" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" height="16" role="img" title="Repository" version="1.1" viewbox="0 0 16 16" width="16"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Project" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" height="16" role="img" title="Project" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg>
    <svg aria-label="Search" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" height="16" role="img" title="Search" version="1.1" viewbox="0 0 16 16" width="16"><path d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z" fill-rule="evenodd"></path></svg>
    </div>
    <img alt="" aria-label="Team" class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" height="28" src="" width="28"/>
    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>
    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
    <span aria-label="in this user" class="js-jump-to-badge-search-text-default d-none">
            In this user
          </span>
    <span aria-label="in all of GitHub" class="js-jump-to-badge-search-text-global d-none">
            All GitHub
          </span>
    <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
          Jump to
          <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
    </a>
    </li>
    </ul>
    </div>
    </input></label>
    </form> 
    
    
    <a class="HeaderMenu-link no-underline mr-3" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"site header menu","repository_id":null,"auth_type":"SIGN_UP","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="280a7a05028c69a5da781dd06f27ee361045bc587b439de88b93cfbb9b0cc61f" href="/login?return_to=%2Figorsteinmacher">
              Sign in
            </a>
    <a class="HeaderMenu-link d-inline-block no-underline border border-gray-dark rounded-1 px-2 py-1" data-ga-click="Sign up, click to sign up for account, ref_page:/&lt;user-name&gt;;ref_cta:Sign up;ref_loc:header logged out" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"site header menu","repository_id":null,"auth_type":"SIGN_UP","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="280a7a05028c69a5da781dd06f27ee361045bc587b439de88b93cfbb9b0cc61f" href="/join?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E&amp;source=header">
                  Sign up
                </a>
    
    
    
    
    
    <div class="show-on-focus" id="start-of-content"></div>
    <div data-pjax-replace="" id="js-flash-container">
    <template class="js-flash-template">
    <div class="flash flash-full {{ className }}">
    <div class="px-2">
    <button aria-label="Dismiss this message" class="flash-close js-flash-close" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg>
    </button>
    <div>{{ message }}</div>
    </div>
    </div>
    </template>
    </div>
    <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>
    <div class="application-main" data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
    <main data-pjax-container="" id="js-pjax-container">
    <div class="mt-4 position-sticky top-0 d-none d-md-block bg-white width-full border-bottom" style="z-index:3;">
    <div class="container-xl px-3 px-md-4 px-lg-5">
    <div class="gutter-condensed gutter-lg flex-column flex-md-row d-flex">
    <div class="flex-shrink-0 col-12 col-md-3 mb-4 mb-md-0">
    <div class="user-profile-sticky-bar">
    <div class="user-profile-mini-vcard d-table">
    <span class="user-profile-mini-avatar d-table-cell v-align-middle lh-condensed-ultra pr-2">
    <img alt="@igorsteinmacher" class="rounded-1 avatar-user" height="32" src="https://avatars0.githubusercontent.com/u/2953768?s=88&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" width="32">
    </img></span>
    <span class="d-table-cell v-align-middle lh-condensed">
    <strong>igorsteinmacher</strong>
    <span class="user-following-container">
    <span class="follow d-block">
    <a class="btn btn-sm mini-follow-button" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"follow button","repository_id":null,"auth_type":"LOG_IN","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="a87ebd7f7a81c893624731730f9849172551fecb6fbb1d15b526e35bb1db032e" href="/login?return_to=%2Figorsteinmacher">Follow</a>
    </span>
    </span>
    </span>
    </div>
    </div>
    </div>
    <div class="flex-shrink-0 col-12 col-md-9 mb-4 mb-md-0">
    <div class="UnderlineNav width-full box-shadow-none">
    <nav aria-label="User profile" class="UnderlineNav-body" data-pjax="">
    <a aria-current="page" class="UnderlineNav-item selected" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_OVERVIEW","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="873837d54268b9fd34da2b289cc759035ab7bda4b27f1ad9ead5765504ee7a14" href="/igorsteinmacher">
    <svg aria-hidden="true" class="octicon octicon-book UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z" fill-rule="evenodd"></path></svg>
          Overview
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_REPOSITORIES","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="9bd88af737513787f19ecf4db267ab3ca21548a27581c4625ea57ee1f1f8d3f0" href="/igorsteinmacher?tab=repositories">
    <svg aria-hidden="true" class="octicon octicon-repo UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg>
          Repositories
          <span class="Counter" title="55">55</span>
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_PROJECTS","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="7b63bc1cc282c310c1f0207d2c5b6d88dcf03224ac79efaedecf46947fcc774c" href="/igorsteinmacher?tab=projects">
    <svg aria-hidden="true" class="octicon octicon-project UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg>
          Projects
          <span class="Counter" hidden="hidden" title="0">0</span>
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_PACKAGES","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="9d037a65741a966adda872bc01a79356e7439ff605dfeb655d93583a20afe981" href="/igorsteinmacher?tab=packages">
    <svg aria-hidden="true" class="octicon octicon-package UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.878.392a1.75 1.75 0 00-1.756 0l-5.25 3.045A1.75 1.75 0 001 4.951v6.098c0 .624.332 1.2.872 1.514l5.25 3.045a1.75 1.75 0 001.756 0l5.25-3.045c.54-.313.872-.89.872-1.514V4.951c0-.624-.332-1.2-.872-1.514L8.878.392zM7.875 1.69a.25.25 0 01.25 0l4.63 2.685L8 7.133 3.245 4.375l4.63-2.685zM2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432L2.5 5.677zm6.25 8.271l4.625-2.683a.25.25 0 00.125-.216V5.677L8.75 8.432v5.516z" fill-rule="evenodd"></path></svg>
            Packages
    </a> </nav>
    </div>
    </div>
    </div> </div>
    </div>
    <div class="container-xl px-3 px-md-4 px-lg-5">
    <div class="gutter-condensed gutter-lg flex-column flex-md-row d-flex">
    <div class="flex-shrink-0 col-12 col-md-3 mb-4 mb-md-0">
    <div class="h-card mt-md-n5" data-acv-badge-hovercards-enabled="" itemscope="" itemtype="http://schema.org/Person">
    <div class="user-profile-sticky-bar js-user-profile-sticky-bar d-none d-md-block">
    <div class="user-profile-mini-vcard d-table">
    <span class="user-profile-mini-avatar d-table-cell v-align-middle lh-condensed-ultra pr-2">
    <img alt="@igorsteinmacher" class="rounded-1 avatar-user" height="32" src="https://avatars0.githubusercontent.com/u/2953768?s=88&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" width="32">
    </img></span>
    <span class="d-table-cell v-align-middle lh-condensed">
    <strong>igorsteinmacher</strong>
    <span class="user-following-container">
    <span class="follow d-block">
    <a class="btn btn-sm mini-follow-button" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"follow button","repository_id":null,"auth_type":"LOG_IN","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="a87ebd7f7a81c893624731730f9849172551fecb6fbb1d15b526e35bb1db032e" href="/login?return_to=%2Figorsteinmacher">Follow</a>
    </span>
    </span>
    </span>
    </div>
    </div>
    <div class="clearfix d-flex d-md-block flex-items-center mb-4 mb-md-0">
    <div class="position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0" style="z-index:4;">
    <a href="https://avatars1.githubusercontent.com/u/2953768?s=400&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" itemprop="image"><img alt="Avatar" class="avatar avatar-user width-full border bg-white" height="260" src="https://avatars1.githubusercontent.com/u/2953768?s=460&amp;u=0821bf34565e19803f4065e4220ce38093177e75&amp;v=4" style="height:auto;" width="260"/></a>
    <div class="user-status-container position-relative hide-sm hide-md">
    <div class="d-flex user-status-circle-badge-container">
    <div class="p-2 d-block d-md-inline-block user-status-circle-badge lh-condensed-ultra" data-team-hovercards-enabled="">
    <div class="d-flex flex-items-center flex-items-stretch">
    <div class="user-status-emoji-container mr-2">
    <g-emoji alias="thought_balloon" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ad.png">💭</g-emoji>
    </div>
    <div class="user-status-message-wrapper f6 text-gray-dark no-wrap">
    <div>Teaching and bringing students to Open Source</div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="vcard-names-container float-left col-10 col-md-12 pt-1 pt-md-3 pb-1 pb-md-3 js-sticky js-user-profile-sticky-fields">
    <h1 class="vcard-names pl-2 pl-md-0">
    <span class="p-name vcard-fullname d-block overflow-hidden" itemprop="name">Igor Steinmacher</span>
    <span class="p-nickname vcard-username d-block" itemprop="additionalName">igorsteinmacher</span>
    </h1>
    </div>
    </div>
    <div class="mt-2 user-status-container d-md-none">
    <div class="p-2 d-block d-md-inline-block" data-team-hovercards-enabled="">
    <div class="d-flex flex-items-center flex-items-stretch">
    <div class="user-status-emoji-container mr-2">
    <g-emoji alias="thought_balloon" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4ad.png">💭</g-emoji>
    </div>
    <div class="user-status-message-wrapper f6 text-gray-dark ws-normal lh-condensed">
    <div>Teaching and bringing students to Open Source</div>
    </div>
    </div>
    </div>
    </div>
    <div class="p-note user-profile-bio mb-3 js-user-profile-bio f4"><div>Assistant Professor @ NAU.
    Researcher: Mining Software Repositories and behavior in Open Source are my main topics</div></div>
    <div class="d-flex flex-column">
    <div class="flex-order-1 flex-md-order-none">
    <div class="d-flex">
    <div class="flex-1 mb-0 mb-md-3">
    <div class="js-sticky js-user-profile-follow-button pb-1 mb-n1"></div>
    <span class="user-following-container">
    <span class="follow d-block">
    <a class="btn btn-block" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"follow button","repository_id":null,"auth_type":"LOG_IN","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="a87ebd7f7a81c893624731730f9849172551fecb6fbb1d15b526e35bb1db032e" href="/login?return_to=%2Figorsteinmacher">Follow</a>
    </span>
    </span>
    </div>
    <div class="flex-shrink-0 ml-2 d-flex flex-items-center mb-0 mb-md-3">
    <details class="details-overlay details-reset position-relative" id="blob-more-options-details">
    <summary class="btn" role="button" type="button">
    <span class="px-2 link-gray">
    <svg aria-label="More options" class="octicon octicon-kebab-horizontal" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
    </span>
    </summary> <div>
    <ul class="dropdown-menu dropdown-menu-sw">
    <li>
    <div>
    <details class="details-reset details-overlay details-overlay-dark">
    <summary class="dropdown-item text-small">
            Block or report user
          </summary>
    <details-dialog aria-label="Block or report igorsteinmacher" class="Box d-flex flex-column anim-fade-in fast Box-overlay--narrow">
    <div class="Box-header">
    <button aria-label="Close dialog" class="Box-btn-octicon btn-octicon float-right" data-close-dialog="" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg>
    </button>
    <h1 class="Box-title">Block or report igorsteinmacher</h1>
    </div>
    <div class="Box-body overflow-auto">
    <div class="border-bottom">
    <!-- '"` --><!-- </textarea></xmp> --></div></div></details-dialog></details></div></li></ul></div></details></div></div></div></div></div></div></div></div></main></div><form accept-charset="UTF-8" action="/account/ignore_user/igorsteinmacher" class="mb-3" method="post"><input data-csrf="true" name="authenticity_token" type="hidden" value="G2TyPhFaZNzR/Fq9gHeEKYW9BGOZ8JaNZL8kQ2lPFjWxvuZEkbdCywemzuxG0C5fCzW2pRVjxrC920SXCRqzUA==">
    <strong>Block user</strong>
    <p>
                  Prevent this user from interacting with your repositories and sending you notifications.
                Learn more about <a href="https://docs.github.com/en/articles/blocking-a-user-from-your-personal-account">blocking users</a>.
              </p>
    <button class="btn btn-danger" type="submit">
                Block user
              </button>
    </input></form> 
    <div class="mt-3">
    <strong>Report abuse</strong>
    <p>
              Contact GitHub support about this user’s behavior.
              Learn more about <a href="https://docs.github.com/en/articles/reporting-abuse-or-spam">reporting abuse</a>.
            </p>
    <a class="btn btn-danger" href="/contact/report-abuse?report=igorsteinmacher+%28user%29">Report abuse</a>
    </div>
    
    
    
    
    
    
     
    
    
    <div class="js-profile-editable-area d-flex flex-column d-md-block">
    <div class="flex-order-1 flex-md-order-none mt-2 mt-md-0">
    <div class="mb-3">
    <a class="link-gray no-underline no-wrap" href="/igorsteinmacher?tab=followers">
    <svg aria-hidden="true" class="octicon octicon-people text-gray-light" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z" fill-rule="evenodd"></path></svg>
    <span class="text-bold text-gray-dark">61</span>
              followers
    </a>        · <a class="link-gray no-underline no-wrap" href="/igorsteinmacher?tab=following">
    <span class="text-bold text-gray-dark">5</span>
              following
    </a>        · <a class="link-gray no-underline no-wrap" href="/igorsteinmacher?tab=stars">
    <svg aria-hidden="true" class="octicon octicon-star text-gray-light" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>
    <span class="text-bold text-gray-dark">9</span>
    </a> </div>
    </div>
    <ul class="vcard-details">
    <li aria-label="Organization: NAU" class="vcard-detail pt-1 css-truncate css-truncate-target hide-sm hide-md" itemprop="worksFor" show_title="false"><svg aria-hidden="true" class="octicon octicon-organization" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.5 14.25c0 .138.112.25.25.25H4v-1.25a.75.75 0 01.75-.75h2.5a.75.75 0 01.75.75v1.25h2.25a.25.25 0 00.25-.25V1.75a.25.25 0 00-.25-.25h-8.5a.25.25 0 00-.25.25v12.5zM1.75 16A1.75 1.75 0 010 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 00.25-.25V8.285a.25.25 0 00-.111-.208l-1.055-.703a.75.75 0 11.832-1.248l1.055.703c.487.325.779.871.779 1.456v5.965A1.75 1.75 0 0114.25 16h-3.5a.75.75 0 01-.197-.026c-.099.017-.2.026-.303.026h-3a.75.75 0 01-.75-.75V14h-1v1.25a.75.75 0 01-.75.75h-3zM3 3.75A.75.75 0 013.75 3h.5a.75.75 0 010 1.5h-.5A.75.75 0 013 3.75zM3.75 6a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM3 9.75A.75.75 0 013.75 9h.5a.75.75 0 010 1.5h-.5A.75.75 0 013 9.75zM7.75 9a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5zM7 6.75A.75.75 0 017.75 6h.5a.75.75 0 010 1.5h-.5A.75.75 0 017 6.75zM7.75 3a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5z" fill-rule="evenodd"></path></svg>
    <span class="p-org"><div>NAU</div></span>
    </li>
    <li aria-label="Home location: Flagstaff, AZ, USA" class="vcard-detail pt-1 css-truncate css-truncate-target hide-sm hide-md" itemprop="homeLocation" show_title="false"><svg aria-hidden="true" class="octicon octicon-location" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M11.536 3.464a5 5 0 010 7.072L8 14.07l-3.536-3.535a5 5 0 117.072-7.072v.001zm1.06 8.132a6.5 6.5 0 10-9.192 0l3.535 3.536a1.5 1.5 0 002.122 0l3.535-3.536zM8 9a2 2 0 100-4 2 2 0 000 4z" fill-rule="evenodd"></path></svg>
    <span class="p-label">Flagstaff, AZ, USA</span>
    </li>
    <li aria-label="Email: " class="vcard-detail pt-1 css-truncate css-truncate-target" itemprop="email"><svg aria-hidden="true" class="octicon octicon-mail" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 2A1.75 1.75 0 000 3.75v.736a.75.75 0 000 .027v7.737C0 13.216.784 14 1.75 14h12.5A1.75 1.75 0 0016 12.25v-8.5A1.75 1.75 0 0014.25 2H1.75zM14.5 4.07v-.32a.25.25 0 00-.25-.25H1.75a.25.25 0 00-.25.25v.32L8 7.88l6.5-3.81zm-13 1.74v6.441c0 .138.112.25.25.25h12.5a.25.25 0 00.25-.25V5.809L8.38 9.397a.75.75 0 01-.76 0L1.5 5.809z" fill-rule="evenodd"></path></svg>
    <a class="link-gray-dark" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"view user email","repository_id":null,"auth_type":"LOG_IN","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="c84347d1be48cfcf4bc2a5244df8053b2b20690c19d51a12a5716673cf76f8b6" href="/login?return_to=https%3A%2F%2Fgithub.com%2Figorsteinmacher%2F" rel="nofollow">Sign in to view email</a>
    </li>
    <li class="vcard-detail pt-1 css-truncate css-truncate-target" data-test-selector="profile-website-url" itemprop="url"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z" fill-rule="evenodd"></path></svg>
    <a class="link-gray-dark" href="http://www.igor.pro.br" rel="nofollow me">www.igor.pro.br</a>
    </li>
    </ul>
    </div>
    
    <div class="border-top pt-3 mt-3 d-none d-md-block">
    <h2 class="h4 mb-2">Highlights</h2>
    <ul class="list-style-none">
    <li class="mt-2 position-relative">
    <span class="cursor-pointer" data-hovercard-type="acv_badge" data-hovercard-url="/users/igorsteinmacher/acv/hovercard">
    <svg aria-hidden="true" class="octicon octicon-north-star text-gray-light mr-1" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.5.75a.75.75 0 00-1.5 0v5.19L4.391 3.33a.75.75 0 10-1.06 1.061L5.939 7H.75a.75.75 0 000 1.5h5.19l-2.61 2.609a.75.75 0 101.061 1.06L7 9.561v5.189a.75.75 0 001.5 0V9.56l2.609 2.61a.75.75 0 101.06-1.061L9.561 8.5h5.189a.75.75 0 000-1.5H9.56l2.61-2.609a.75.75 0 00-1.061-1.06L8.5 5.939V.75z"></path></svg>Arctic Code Vault Contributor
              </span>
    </li>
    <li class="mt-2">
    <svg aria-hidden="true" class="octicon octicon-star text-gray-light" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>
    <span class="label bg-purple text-uppercase">Pro</span>
    </li>
    </ul>
    </div>
    <div class="border-top pt-3 mt-3 clearfix hide-sm hide-md">
    <h2 class="mb-2 h4">Organizations</h2>
    <a aria-label="JabRef" class="avatar-group-item" data-hovercard-type="organization" data-hovercard-url="/orgs/JabRef/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"MEMBER_ORGANIZATION_AVATAR","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="950bdaa6c95568b545e270db90fc4cc8499487896a2194671e515e2c0fe1c543" href="/JabRef" itemprop="follows">
    <img alt="@JabRef" class="avatar" height="32" src="https://avatars2.githubusercontent.com/u/3914421?s=60&amp;v=4" width="32">
    </img></a> <a aria-label="NAU-OSS" class="avatar-group-item" data-hovercard-type="organization" data-hovercard-url="/orgs/NAU-OSS/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"MEMBER_ORGANIZATION_AVATAR","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="950bdaa6c95568b545e270db90fc4cc8499487896a2194671e515e2c0fe1c543" href="/NAU-OSS" itemprop="follows">
    <img alt="@NAU-OSS" class="avatar" height="32" src="https://avatars0.githubusercontent.com/u/42679979?s=60&amp;v=4" width="32"/>
    </a> </div>
    
    
    <div class="flex-shrink-0 col-12 col-md-9 mb-4 mb-md-0">
    <div class="UnderlineNav user-profile-nav d-block d-md-none position-sticky top-0 pl-3 ml-n3 mr-n3 pr-3 bg-white" style="z-index:3;">
    <nav aria-label="User profile" class="UnderlineNav-body" data-pjax="">
    <a aria-current="page" class="UnderlineNav-item selected" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_OVERVIEW","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="873837d54268b9fd34da2b289cc759035ab7bda4b27f1ad9ead5765504ee7a14" href="/igorsteinmacher">
    <svg aria-hidden="true" class="octicon octicon-book UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z" fill-rule="evenodd"></path></svg>
          Overview
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_REPOSITORIES","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="9bd88af737513787f19ecf4db267ab3ca21548a27581c4625ea57ee1f1f8d3f0" href="/igorsteinmacher?tab=repositories">
    <svg aria-hidden="true" class="octicon octicon-repo UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z" fill-rule="evenodd"></path></svg>
          Repositories
          <span class="Counter" title="55">55</span>
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_PROJECTS","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="7b63bc1cc282c310c1f0207d2c5b6d88dcf03224ac79efaedecf46947fcc774c" href="/igorsteinmacher?tab=projects">
    <svg aria-hidden="true" class="octicon octicon-project UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z" fill-rule="evenodd"></path></svg>
          Projects
          <span class="Counter" hidden="hidden" title="0">0</span>
    </a>
    <a class="UnderlineNav-item" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TAB_PACKAGES","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="9d037a65741a966adda872bc01a79356e7439ff605dfeb655d93583a20afe981" href="/igorsteinmacher?tab=packages">
    <svg aria-hidden="true" class="octicon octicon-package UnderlineNav-octicon hide-sm" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.878.392a1.75 1.75 0 00-1.756 0l-5.25 3.045A1.75 1.75 0 001 4.951v6.098c0 .624.332 1.2.872 1.514l5.25 3.045a1.75 1.75 0 001.756 0l5.25-3.045c.54-.313.872-.89.872-1.514V4.951c0-.624-.332-1.2-.872-1.514L8.878.392zM7.875 1.69a.25.25 0 01.25 0l4.63 2.685L8 7.133 3.245 4.375l4.63-2.685zM2.5 5.677v5.372c0 .09.047.171.125.216l4.625 2.683V8.432L2.5 5.677zm6.25 8.271l4.625-2.683a.25.25 0 00.125-.216V5.677L8.75 8.432v5.516z" fill-rule="evenodd"></path></svg>
            Packages
    </a> </nav>
    </div>
    <div>
    <signup-prompt class="signup-prompt-bg rounded-1 mt-4" data-prompt="signup" hidden="">
    <div class="signup-prompt p-4 text-center mb-4 rounded-1">
    <div class="position-relative">
    <button class="position-absolute top-0 right-0 btn-link link-gray" data-action="click:signup-prompt#dismiss" data-ga-click="(Logged out) Sign up prompt, clicked Dismiss, text:dismiss" type="button">
              Dismiss
            </button>
    <h3 class="pt-4 pt-lg-2">Create your own GitHub profile</h3>
    <p class="col-8 mx-auto">Sign up for your own profile on GitHub, the best place to host code, manage projects, and build software alongside 50 million developers.</p>
    <a class="btn btn-primary" data-ga-click="Sign up, click to sign up for account, text:Sign up" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"sign up prompt","repository_id":null,"auth_type":"SIGN_UP","originating_url":"https://github.com/igorsteinmacher","user_id":null}}' data-hydro-click-hmac="f3cdaf8b55aa18b7f73ac7b7dea3bd76223f08aa0d974e53d4a17fd492bd4b86" href="/join?source=prompt-users-profile">Sign up</a>
    </div>
    </div>
    </signup-prompt>
    <div class="position-relative">
    <div class="mt-4">
    <div class="js-pinned-items-reorder-container">
    <h2 class="f4 mb-2 text-normal">
          Popular repositories
        <img alt="" class="spinner pinned-items-spinner js-pinned-items-spinner" src="https://github.githubassets.com/images/spinners/octocat-spinner-32.gif" width="13"/>
    <span aria-live="polite" class="ml-2 text-gray f6 js-pinned-items-reorder-message" data-error-text="Something went wrong." data-success-text="Order updated." role="status"></span>
    </h2>
    <ol class="d-flex flex-wrap list-style-none gutter-condensed mb-4">
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public source">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/CS499-OSS">
    <span class="repo" title="CS499-OSS">CS499-OSS</span>
    </a>
    </div>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
                Open Source Software Development Course at NAU
              </p>
    <p class="mb-0 f6 text-gray">
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/CS499-OSS/stargazers">
    <svg aria-label="stars" class="octicon octicon-star" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>
                    12
                  </a>
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/CS499-OSS/network/members">
    <svg aria-label="forks" class="octicon octicon-repo-forked" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z" fill-rule="evenodd"></path></svg>
                    55
                  </a>
    </p>
    </div>
    </div>
    </li>
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public source">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/INF502-Fall2020">
    <span class="repo" title="INF502-Fall2020">INF502-Fall2020</span>
    </a>
    </div>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
    </p>
    <p class="mb-0 f6 text-gray">
    <span class="d-inline-block mr-3">
    <span class="repo-language-color" style="background-color: #e34c26"></span>
    <span itemprop="programmingLanguage">HTML</span>
    </span>
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/INF502-Fall2020/stargazers">
    <svg aria-label="stars" class="octicon octicon-star" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>
                    2
                  </a>
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/INF502-Fall2020/network/members">
    <svg aria-label="forks" class="octicon octicon-repo-forked" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z" fill-rule="evenodd"></path></svg>
                    31
                  </a>
    </p>
    </div>
    </div>
    </li>
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public source">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/ProjetoIntegrador">
    <span class="repo" title="ProjetoIntegrador">ProjetoIntegrador</span>
    </a>
    </div>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
    </p>
    <p class="mb-0 f6 text-gray">
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/ProjetoIntegrador/stargazers">
    <svg aria-label="star" class="octicon octicon-star" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z" fill-rule="evenodd"></path></svg>
                    1
                  </a>
    <a class="pinned-item-meta muted-link" href="/igorsteinmacher/ProjetoIntegrador/network/members">
    <svg aria-label="fork" class="octicon octicon-repo-forked" height="16" role="img" version="1.1" viewbox="0 0 16 16" width="16"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z" fill-rule="evenodd"></path></svg>
                    1
                  </a>
    </p>
    </div>
    </div>
    </li>
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public fork">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/rails-1">
    <span class="repo" title="rails-1">rails-1</span>
    </a>
    </div>
    <p class="text-gray text-small mb-2">Forked from <a class="muted-link" href="/capistrano/rails">capistrano/rails</a></p>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
                Official Ruby on Rails specific tasks for Capistrano
              </p>
    <p class="mb-0 f6 text-gray">
    <span class="d-inline-block mr-3">
    <span class="repo-language-color" style="background-color: #701516"></span>
    <span itemprop="programmingLanguage">Ruby</span>
    </span>
    </p>
    </div>
    </div>
    </li>
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public fork">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/gitProjeto">
    <span class="repo" title="gitProjeto">gitProjeto</span>
    </a>
    </div>
    <p class="text-gray text-small mb-2">Forked from <a class="muted-link" href="/SamuellP/gitProjeto">SamuellP/gitProjeto</a></p>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
    </p>
    <p class="mb-0 f6 text-gray">
    </p>
    </div>
    </div>
    </li>
    <li class="col-12 col-md-6 col-lg-6 mb-3 d-flex flex-content-stretch">
    <div class="Box pinned-item-list-item d-flex p-3 width-full public source">
    <div class="pinned-item-list-item-content">
    <div class="d-flex width-full flex-items-center position-relative">
    <a class="text-bold flex-auto min-width-0" href="/igorsteinmacher/repoTeste">
    <span class="repo" title="repoTeste">repoTeste</span>
    </a>
    </div>
    <p class="pinned-item-desc text-gray text-small d-block mt-2 mb-3">
    </p>
    <p class="mb-0 f6 text-gray">
    </p>
    </div>
    </div>
    </li>
    </ol>
    </div>
    </div>
    <div class="mt-4 position-relative">
    <div class="js-yearly-contributions">
    <div class="position-relative">
    <h2 class="f4 text-normal mb-2">
          401 contributions
            in the last year
        </h2>
    <div class="border py-2 graph-before-activity-overview">
    <div class="js-calendar-graph mx-md-2 mx-3 d-flex flex-column flex-items-end flex-xl-items-center overflow-hidden pt-1 is-graph-loading graph-canvas calendar-graph height-full text-center" data-from="2019-10-27 00:00:00 UTC" data-graph-url="/users/igorsteinmacher/contributions?to=2020-10-29" data-org="" data-to="2020-10-29 23:59:59 UTC" data-url="/igorsteinmacher">
    <svg class="js-calendar-graph-svg" height="128" width="828">
    <g data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_CALENDAR_SQUARE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="68900ef35a32cab4189baf3e29dc0088cc55e05f6fb5ffaf440c8bb439567685" transform="translate(10, 20)">
    <g transform="translate(0, 0)">
    <rect class="day" data-count="1" data-date="2019-10-27" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="16" y="0"></rect>
    <rect class="day" data-count="1" data-date="2019-10-28" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="16" y="15"></rect>
    <rect class="day" data-count="2" data-date="2019-10-29" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="16" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-10-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="16" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-10-31" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="16" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-11-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="16" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-11-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="16" y="90"></rect>
    </g>
    <g transform="translate(16, 0)">
    <rect class="day" data-count="0" data-date="2019-11-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="15" y="0"></rect>
    <rect class="day" data-count="1" data-date="2019-11-04" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="15" y="15"></rect>
    <rect class="day" data-count="2" data-date="2019-11-05" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="15" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-11-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="15" y="45"></rect>
    <rect class="day" data-count="2" data-date="2019-11-07" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="15" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-11-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="15" y="75"></rect>
    <rect class="day" data-count="3" data-date="2019-11-09" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="15" y="90"></rect>
    </g>
    <g transform="translate(32, 0)">
    <rect class="day" data-count="0" data-date="2019-11-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="14" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-11-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="14" y="15"></rect>
    <rect class="day" data-count="6" data-date="2019-11-12" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="14" y="30"></rect>
    <rect class="day" data-count="1" data-date="2019-11-13" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="14" y="45"></rect>
    <rect class="day" data-count="1" data-date="2019-11-14" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="14" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-11-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="14" y="75"></rect>
    <rect class="day" data-count="3" data-date="2019-11-16" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="14" y="90"></rect>
    </g>
    <g transform="translate(48, 0)">
    <rect class="day" data-count="0" data-date="2019-11-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-11-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-11-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-11-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-11-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-11-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="13" y="75"></rect>
    <rect class="day" data-count="1" data-date="2019-11-23" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="13" y="90"></rect>
    </g>
    <g transform="translate(64, 0)">
    <rect class="day" data-count="0" data-date="2019-11-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-11-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="15"></rect>
    <rect class="day" data-count="2" data-date="2019-11-26" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="12" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-11-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-11-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-11-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-11-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="12" y="90"></rect>
    </g>
    <g transform="translate(80, 0)">
    <rect class="day" data-count="0" data-date="2019-12-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-12-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-12-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-12-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-12-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-12-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-12-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="11" y="90"></rect>
    </g>
    <g transform="translate(96, 0)">
    <rect class="day" data-count="0" data-date="2019-12-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-12-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-12-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-12-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-12-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-12-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-12-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="10" y="90"></rect>
    </g>
    <g transform="translate(112, 0)">
    <rect class="day" data-count="0" data-date="2019-12-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-12-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-12-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-12-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-12-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-12-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-12-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="9" y="90"></rect>
    </g>
    <g transform="translate(128, 0)">
    <rect class="day" data-count="0" data-date="2019-12-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-12-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-12-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="30"></rect>
    <rect class="day" data-count="0" data-date="2019-12-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="45"></rect>
    <rect class="day" data-count="0" data-date="2019-12-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="60"></rect>
    <rect class="day" data-count="0" data-date="2019-12-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="75"></rect>
    <rect class="day" data-count="0" data-date="2019-12-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="8" y="90"></rect>
    </g>
    <g transform="translate(144, 0)">
    <rect class="day" data-count="0" data-date="2019-12-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="0"></rect>
    <rect class="day" data-count="0" data-date="2019-12-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="15"></rect>
    <rect class="day" data-count="0" data-date="2019-12-31" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-01-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-01-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-01-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="7" y="75"></rect>
    <rect class="day" data-count="1" data-date="2020-01-04" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="7" y="90"></rect>
    </g>
    <g transform="translate(160, 0)">
    <rect class="day" data-count="0" data-date="2020-01-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-01-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-01-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-01-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-01-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-01-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-01-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="6" y="90"></rect>
    </g>
    <g transform="translate(176, 0)">
    <rect class="day" data-count="0" data-date="2020-01-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-01-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-01-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-01-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-01-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="60"></rect>
    <rect class="day" data-count="2" data-date="2020-01-17" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="5" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-01-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="5" y="90"></rect>
    </g>
    <g transform="translate(192, 0)">
    <rect class="day" data-count="0" data-date="2020-01-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-01-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-01-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-01-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-01-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-01-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-01-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="4" y="90"></rect>
    </g>
    <g transform="translate(208, 0)">
    <rect class="day" data-count="0" data-date="2020-01-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-01-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-01-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-01-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-01-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-01-31" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-02-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="3" y="90"></rect>
    </g>
    <g transform="translate(224, 0)">
    <rect class="day" data-count="0" data-date="2020-02-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="2" y="0"></rect>
    <rect class="day" data-count="1" data-date="2020-02-03" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="2" y="15"></rect>
    <rect class="day" data-count="26" data-date="2020-02-04" fill="var(--color-calendar-graph-day-L4-bg)" height="11" width="11" x="2" y="30"></rect>
    <rect class="day" data-count="4" data-date="2020-02-05" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="2" y="45"></rect>
    <rect class="day" data-count="1" data-date="2020-02-06" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="2" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-02-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="2" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-02-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="2" y="90"></rect>
    </g>
    <g transform="translate(240, 0)">
    <rect class="day" data-count="0" data-date="2020-02-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="0"></rect>
    <rect class="day" data-count="2" data-date="2020-02-10" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="1" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-02-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-02-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-02-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-02-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-02-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="1" y="90"></rect>
    </g>
    <g transform="translate(256, 0)">
    <rect class="day" data-count="0" data-date="2020-02-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-02-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-02-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-02-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-02-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-02-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-02-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="0" y="90"></rect>
    </g>
    <g transform="translate(272, 0)">
    <rect class="day" data-count="0" data-date="2020-02-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-02-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-02-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-02-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-02-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-02-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-02-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-1" y="90"></rect>
    </g>
    <g transform="translate(288, 0)">
    <rect class="day" data-count="0" data-date="2020-03-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-03-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-03-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-03-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-03-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-03-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-03-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-2" y="90"></rect>
    </g>
    <g transform="translate(304, 0)">
    <rect class="day" data-count="0" data-date="2020-03-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-03-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-03-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-03-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-03-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-03-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-03-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-3" y="90"></rect>
    </g>
    <g transform="translate(320, 0)">
    <rect class="day" data-count="0" data-date="2020-03-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-03-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-03-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-03-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-03-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-03-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-03-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-4" y="90"></rect>
    </g>
    <g transform="translate(336, 0)">
    <rect class="day" data-count="0" data-date="2020-03-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-5" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-03-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-5" y="15"></rect>
    <rect class="day" data-count="1" data-date="2020-03-24" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-5" y="30"></rect>
    <rect class="day" data-count="2" data-date="2020-03-25" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-5" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-03-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-5" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-03-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-5" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-03-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-5" y="90"></rect>
    </g>
    <g transform="translate(352, 0)">
    <rect class="day" data-count="0" data-date="2020-03-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-6" y="0"></rect>
    <rect class="day" data-count="1" data-date="2020-03-30" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-6" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-03-31" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-6" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-04-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-6" y="45"></rect>
    <rect class="day" data-count="2" data-date="2020-04-02" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-6" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-04-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-6" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-04-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-6" y="90"></rect>
    </g>
    <g transform="translate(368, 0)">
    <rect class="day" data-count="0" data-date="2020-04-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-04-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="15"></rect>
    <rect class="day" data-count="1" data-date="2020-04-07" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-7" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-04-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-04-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-04-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-04-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-7" y="90"></rect>
    </g>
    <g transform="translate(384, 0)">
    <rect class="day" data-count="0" data-date="2020-04-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-8" y="0"></rect>
    <rect class="day" data-count="1" data-date="2020-04-13" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-8" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-04-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-8" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-04-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-8" y="45"></rect>
    <rect class="day" data-count="2" data-date="2020-04-16" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-8" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-04-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-8" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-04-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-8" y="90"></rect>
    </g>
    <g transform="translate(400, 0)">
    <rect class="day" data-count="0" data-date="2020-04-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-04-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-04-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-04-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-04-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-04-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-04-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-9" y="90"></rect>
    </g>
    <g transform="translate(416, 0)">
    <rect class="day" data-count="0" data-date="2020-04-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-04-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-04-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-04-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-04-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-05-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-05-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-10" y="90"></rect>
    </g>
    <g transform="translate(432, 0)">
    <rect class="day" data-count="0" data-date="2020-05-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-11" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-05-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-11" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-05-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-11" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-05-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-11" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-05-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-11" y="60"></rect>
    <rect class="day" data-count="5" data-date="2020-05-08" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-11" y="75"></rect>
    <rect class="day" data-count="1" data-date="2020-05-09" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-11" y="90"></rect>
    </g>
    <g transform="translate(448, 0)">
    <rect class="day" data-count="0" data-date="2020-05-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-05-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-05-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-05-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-05-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-05-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-05-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-12" y="90"></rect>
    </g>
    <g transform="translate(464, 0)">
    <rect class="day" data-count="0" data-date="2020-05-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-05-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="15"></rect>
    <rect class="day" data-count="1" data-date="2020-05-19" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-13" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-05-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-05-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-05-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-05-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-13" y="90"></rect>
    </g>
    <g transform="translate(480, 0)">
    <rect class="day" data-count="0" data-date="2020-05-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-05-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-05-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-05-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-05-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-05-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-05-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-14" y="90"></rect>
    </g>
    <g transform="translate(496, 0)">
    <rect class="day" data-count="0" data-date="2020-05-31" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-06-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-06-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-06-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-06-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-06-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-06-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-15" y="90"></rect>
    </g>
    <g transform="translate(512, 0)">
    <rect class="day" data-count="0" data-date="2020-06-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-06-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-06-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-06-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-06-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-06-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-06-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-16" y="90"></rect>
    </g>
    <g transform="translate(528, 0)">
    <rect class="day" data-count="0" data-date="2020-06-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-06-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-06-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-06-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-06-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-06-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-06-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-17" y="90"></rect>
    </g>
    <g transform="translate(544, 0)">
    <rect class="day" data-count="0" data-date="2020-06-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-06-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-06-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-06-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-06-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-06-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-06-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-18" y="90"></rect>
    </g>
    <g transform="translate(560, 0)">
    <rect class="day" data-count="0" data-date="2020-06-28" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-06-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-06-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-07-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-07-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-07-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-07-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-19" y="90"></rect>
    </g>
    <g transform="translate(576, 0)">
    <rect class="day" data-count="0" data-date="2020-07-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-07-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-07-07" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-07-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-07-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-07-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-07-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-20" y="90"></rect>
    </g>
    <g transform="translate(592, 0)">
    <rect class="day" data-count="0" data-date="2020-07-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-07-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-07-14" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-07-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-07-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-07-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-07-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-21" y="90"></rect>
    </g>
    <g transform="translate(608, 0)">
    <rect class="day" data-count="0" data-date="2020-07-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-07-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-07-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-07-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-07-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-07-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-07-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-22" y="90"></rect>
    </g>
    <g transform="translate(624, 0)">
    <rect class="day" data-count="0" data-date="2020-07-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-23" y="0"></rect>
    <rect class="day" data-count="2" data-date="2020-07-27" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-23" y="15"></rect>
    <rect class="day" data-count="12" data-date="2020-07-28" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-23" y="30"></rect>
    <rect class="day" data-count="3" data-date="2020-07-29" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-23" y="45"></rect>
    <rect class="day" data-count="4" data-date="2020-07-30" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-23" y="60"></rect>
    <rect class="day" data-count="1" data-date="2020-07-31" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-23" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-08-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-23" y="90"></rect>
    </g>
    <g transform="translate(640, 0)">
    <rect class="day" data-count="0" data-date="2020-08-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-24" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-08-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-24" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-08-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-24" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-08-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-24" y="45"></rect>
    <rect class="day" data-count="31" data-date="2020-08-06" fill="var(--color-calendar-graph-day-L4-bg)" height="11" width="11" x="-24" y="60"></rect>
    <rect class="day" data-count="10" data-date="2020-08-07" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-24" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-08-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-24" y="90"></rect>
    </g>
    <g transform="translate(656, 0)">
    <rect class="day" data-count="0" data-date="2020-08-09" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-25" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-08-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-25" y="15"></rect>
    <rect class="day" data-count="1" data-date="2020-08-11" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-25" y="30"></rect>
    <rect class="day" data-count="5" data-date="2020-08-12" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-25" y="45"></rect>
    <rect class="day" data-count="3" data-date="2020-08-13" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-25" y="60"></rect>
    <rect class="day" data-count="1" data-date="2020-08-14" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-25" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-08-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-25" y="90"></rect>
    </g>
    <g transform="translate(672, 0)">
    <rect class="day" data-count="0" data-date="2020-08-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-26" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-08-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-26" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-08-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-26" y="30"></rect>
    <rect class="day" data-count="9" data-date="2020-08-19" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-26" y="45"></rect>
    <rect class="day" data-count="7" data-date="2020-08-20" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-26" y="60"></rect>
    <rect class="day" data-count="6" data-date="2020-08-21" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-26" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-08-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-26" y="90"></rect>
    </g>
    <g transform="translate(688, 0)">
    <rect class="day" data-count="6" data-date="2020-08-23" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-27" y="0"></rect>
    <rect class="day" data-count="1" data-date="2020-08-24" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-27" y="15"></rect>
    <rect class="day" data-count="3" data-date="2020-08-25" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-27" y="30"></rect>
    <rect class="day" data-count="1" data-date="2020-08-26" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-27" y="45"></rect>
    <rect class="day" data-count="2" data-date="2020-08-27" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-27" y="60"></rect>
    <rect class="day" data-count="10" data-date="2020-08-28" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-27" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-08-29" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-27" y="90"></rect>
    </g>
    <g transform="translate(704, 0)">
    <rect class="day" data-count="0" data-date="2020-08-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-28" y="0"></rect>
    <rect class="day" data-count="2" data-date="2020-08-31" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-28" y="15"></rect>
    <rect class="day" data-count="6" data-date="2020-09-01" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-28" y="30"></rect>
    <rect class="day" data-count="4" data-date="2020-09-02" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-28" y="45"></rect>
    <rect class="day" data-count="13" data-date="2020-09-03" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-28" y="60"></rect>
    <rect class="day" data-count="2" data-date="2020-09-04" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-28" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-09-05" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-28" y="90"></rect>
    </g>
    <g transform="translate(720, 0)">
    <rect class="day" data-count="0" data-date="2020-09-06" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-29" y="0"></rect>
    <rect class="day" data-count="13" data-date="2020-09-07" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-29" y="15"></rect>
    <rect class="day" data-count="37" data-date="2020-09-08" fill="var(--color-calendar-graph-day-L4-bg)" height="11" width="11" x="-29" y="30"></rect>
    <rect class="day" data-count="7" data-date="2020-09-09" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-29" y="45"></rect>
    <rect class="day" data-count="1" data-date="2020-09-10" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-29" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-09-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-29" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-09-12" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-29" y="90"></rect>
    </g>
    <g transform="translate(736, 0)">
    <rect class="day" data-count="0" data-date="2020-09-13" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-30" y="0"></rect>
    <rect class="day" data-count="18" data-date="2020-09-14" fill="var(--color-calendar-graph-day-L3-bg)" height="11" width="11" x="-30" y="15"></rect>
    <rect class="day" data-count="27" data-date="2020-09-15" fill="var(--color-calendar-graph-day-L4-bg)" height="11" width="11" x="-30" y="30"></rect>
    <rect class="day" data-count="1" data-date="2020-09-16" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-30" y="45"></rect>
    <rect class="day" data-count="3" data-date="2020-09-17" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-30" y="60"></rect>
    <rect class="day" data-count="2" data-date="2020-09-18" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-30" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-09-19" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-30" y="90"></rect>
    </g>
    <g transform="translate(752, 0)">
    <rect class="day" data-count="0" data-date="2020-09-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="0"></rect>
    <rect class="day" data-count="0" data-date="2020-09-21" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-09-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-09-23" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="45"></rect>
    <rect class="day" data-count="1" data-date="2020-09-24" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-31" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-09-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-09-26" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-31" y="90"></rect>
    </g>
    <g transform="translate(768, 0)">
    <rect class="day" data-count="0" data-date="2020-09-27" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-32" y="0"></rect>
    <rect class="day" data-count="5" data-date="2020-09-28" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-32" y="15"></rect>
    <rect class="day" data-count="5" data-date="2020-09-29" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-32" y="30"></rect>
    <rect class="day" data-count="0" data-date="2020-09-30" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-32" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-10-01" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-32" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-10-02" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-32" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-10-03" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-32" y="90"></rect>
    </g>
    <g transform="translate(784, 0)">
    <rect class="day" data-count="0" data-date="2020-10-04" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-33" y="0"></rect>
    <rect class="day" data-count="2" data-date="2020-10-05" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-33" y="15"></rect>
    <rect class="day" data-count="7" data-date="2020-10-06" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-33" y="30"></rect>
    <rect class="day" data-count="1" data-date="2020-10-07" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-33" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-10-08" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-33" y="60"></rect>
    <rect class="day" data-count="3" data-date="2020-10-09" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-33" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-10-10" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-33" y="90"></rect>
    </g>
    <g transform="translate(800, 0)">
    <rect class="day" data-count="0" data-date="2020-10-11" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-34" y="0"></rect>
    <rect class="day" data-count="8" data-date="2020-10-12" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-34" y="15"></rect>
    <rect class="day" data-count="8" data-date="2020-10-13" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-34" y="30"></rect>
    <rect class="day" data-count="3" data-date="2020-10-14" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-34" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-10-15" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-34" y="60"></rect>
    <rect class="day" data-count="0" data-date="2020-10-16" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-34" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-10-17" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-34" y="90"></rect>
    </g>
    <g transform="translate(816, 0)">
    <rect class="day" data-count="0" data-date="2020-10-18" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-35" y="0"></rect>
    <rect class="day" data-count="4" data-date="2020-10-19" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-35" y="15"></rect>
    <rect class="day" data-count="0" data-date="2020-10-20" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-35" y="30"></rect>
    <rect class="day" data-count="2" data-date="2020-10-21" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-35" y="45"></rect>
    <rect class="day" data-count="0" data-date="2020-10-22" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-35" y="60"></rect>
    <rect class="day" data-count="1" data-date="2020-10-23" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-35" y="75"></rect>
    <rect class="day" data-count="0" data-date="2020-10-24" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-35" y="90"></rect>
    </g>
    <g transform="translate(832, 0)">
    <rect class="day" data-count="0" data-date="2020-10-25" fill="var(--color-calendar-graph-day-bg)" height="11" width="11" x="-36" y="0"></rect>
    <rect class="day" data-count="8" data-date="2020-10-26" fill="var(--color-calendar-graph-day-L2-bg)" height="11" width="11" x="-36" y="15"></rect>
    <rect class="day" data-count="2" data-date="2020-10-27" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-36" y="30"></rect>
    <rect class="day" data-count="6" data-date="2020-10-28" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-36" y="45"></rect>
    <rect class="day" data-count="1" data-date="2020-10-29" fill="var(--color-calendar-graph-day-L1-bg)" height="11" width="11" x="-36" y="60"></rect>
    </g>
    <text class="month" x="31" y="-8">Nov</text>
    <text class="month" x="91" y="-8">Dec</text>
    <text class="month" x="166" y="-8">Jan</text>
    <text class="month" x="226" y="-8">Feb</text>
    <text class="month" x="286" y="-8">Mar</text>
    <text class="month" x="361" y="-8">Apr</text>
    <text class="month" x="421" y="-8">May</text>
    <text class="month" x="496" y="-8">Jun</text>
    <text class="month" x="556" y="-8">Jul</text>
    <text class="month" x="616" y="-8">Aug</text>
    <text class="month" x="691" y="-8">Sep</text>
    <text class="month" x="751" y="-8">Oct</text>
    <text class="wday" dx="-10" dy="8" style="display: none;" text-anchor="start">Sun</text>
    <text class="wday" dx="-10" dy="25" text-anchor="start">Mon</text>
    <text class="wday" dx="-10" dy="32" style="display: none;" text-anchor="start">Tue</text>
    <text class="wday" dx="-10" dy="56" text-anchor="start">Wed</text>
    <text class="wday" dx="-10" dy="57" style="display: none;" text-anchor="start">Thu</text>
    <text class="wday" dx="-10" dy="85" text-anchor="start">Fri</text>
    <text class="wday" dx="-10" dy="81" style="display: none;" text-anchor="start">Sat</text>
    </g></svg>
    </div>
    <div class="contrib-footer clearfix mt-1 mx-3 px-3 pb-1">
    <div class="float-left text-gray">
    <a class="" href="https://docs.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile">
                Learn how we count contributions</a>.
            </div>
    <div class="contrib-legend text-gray" title="A summary of pull requests, issues opened, and commits to the default and gh-pages branches.">
              Less
              <ul class="legend">
    <li style="background-color: var(--color-calendar-graph-day-bg)"></li>
    <li style="background-color: var(--color-calendar-graph-day-L1-bg)"></li>
    <li style="background-color: var(--color-calendar-graph-day-L2-bg)"></li>
    <li style="background-color: var(--color-calendar-graph-day-L3-bg)"></li>
    <li style="background-color: var(--color-calendar-graph-day-L4-bg)"></li>
    </ul>
              More
            </div>
    </div>
    </div>
    </div>
    </div>
    <div class="activity-listing contribution-activity" data-pjax-container="" id="js-contribution-activity">
    <div class="d-none d-lg-block">
    <div class="profile-timeline-year-list js-profile-timeline-year-list bg-white js-sticky float-right col-2 pl-5">
    <ul class="filter-list small">
    <li>
    <a aria-label="Contribution activity in 2020" class="js-year-link filter-item px-3 mb-2 py-2 selected" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2020-10-01&amp;to=2020-10-29" id="year-link-2020">2020</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2019" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2019-12-01&amp;to=2019-12-31" id="year-link-2019">2019</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2018" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2018-12-01&amp;to=2018-12-31" id="year-link-2018">2018</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2017" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2017-12-01&amp;to=2017-12-31" id="year-link-2017">2017</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2016" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2016-12-01&amp;to=2016-12-31" id="year-link-2016">2016</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2015" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2015-12-01&amp;to=2015-12-31" id="year-link-2015">2015</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2014" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2014-12-01&amp;to=2014-12-31" id="year-link-2014">2014</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2013" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2013-12-01&amp;to=2013-12-31" id="year-link-2013">2013</a>
    </li>
    <li>
    <a aria-label="Contribution activity in 2012" class="js-year-link filter-item px-3 mb-2 py-2" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"CONTRIBUTION_YEAR_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="d4bf374d0b41a26890fb9c6afef012fde6487ad6da1ec62e8572e2105f3d2817" href="/igorsteinmacher?tab=overview&amp;from=2012-12-01&amp;to=2012-12-31" id="year-link-2012">2012</a>
    </li>
    </ul>
    </div>
    </div>
    <h2 class="f4 text-normal mb-2">
        Contribution activity
      </h2>
    <div class="contribution-activity-listing float-left col-12 col-lg-10">
    <div class="profile-timeline discussion-timeline width-full pb-4">
    <h3 class="profile-timeline-month-heading bg-white d-inline-block h6 pr-2 py-1">
          October <span class="text-gray">2020</span>
    </h3>
    <div class="profile-rollup-wrapper py-4 pl-4 position-relative ml-3 js-details-container Details">
    <span class="discussion-item-icon"><svg aria-hidden="true" class="octicon octicon-repo-push" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1 2.5A2.5 2.5 0 013.5 0h8.75a.75.75 0 01.75.75v3.5a.75.75 0 01-1.5 0V1.5h-8a1 1 0 00-1 1v6.708A2.492 2.492 0 013.5 9h3.25a.75.75 0 010 1.5H3.5a1 1 0 100 2h5.75a.75.75 0 010 1.5H3.5A2.5 2.5 0 011 11.5v-9zm13.23 7.79a.75.75 0 001.06-1.06l-2.505-2.505a.75.75 0 00-1.06 0L9.22 9.229a.75.75 0 001.06 1.061l1.225-1.224v6.184a.75.75 0 001.5 0V9.066l1.224 1.224z" fill-rule="evenodd"></path></svg></span>
    <button aria-expanded="false" class="btn-link f4 muted-link no-underline lh-condensed width-full js-details-target" type="button">
    <span class="float-left ws-normal text-left">
            Created 51
            commits in
            8
            repositories
          </span>
    <span class="d-inline-block float-right">
    <span aria_label="Collapse" class="profile-rollup-toggle-closed float-right" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_CATEGORY_ROLLUP_COLLAPSE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="cfd9a2f97d3a53e11390526e5625c91063f0a2df2c7c99d49a795873599a16bc"><svg aria-hidden="true" class="octicon octicon-fold" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M10.896 2H8.75V.75a.75.75 0 00-1.5 0V2H5.104a.25.25 0 00-.177.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 2zM8.75 15.25a.75.75 0 01-1.5 0V14H5.104a.25.25 0 01-.177-.427l2.896-2.896a.25.25 0 01.354 0l2.896 2.896a.25.25 0 01-.177.427H8.75v1.25zm-6.5-6.5a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM6 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 016 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM12 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 0112 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5z" fill-rule="evenodd"></path></svg></span>
    <span aria_label="Expand" class="profile-rollup-toggle-open float-right" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_CATEGORY_ROLLUP_EXPAND","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="1a2cae486d73dbc25ee0aab926efbe377ef05405f922073d21f5fabab80a1ab7"><svg aria-hidden="true" class="octicon octicon-unfold" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.177.677l2.896 2.896a.25.25 0 01-.177.427H8.75v1.25a.75.75 0 01-1.5 0V4H5.104a.25.25 0 01-.177-.427L7.823.677a.25.25 0 01.354 0zM7.25 10.75a.75.75 0 011.5 0V12h2.146a.25.25 0 01.177.427l-2.896 2.896a.25.25 0 01-.354 0l-2.896-2.896A.25.25 0 015.104 12H7.25v-1.25zm-5-2a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM6 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 016 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM12 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 0112 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5z" fill-rule="evenodd"></path></svg></span>
    </span>
    </button>
    <ul class="profile-rollup-content list-style-none" data-repository-hovercards-enabled="">
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/igorsteinmacher/INF502-Fall2020">igorsteinmacher/INF502-Fall2020</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/igorsteinmacher/INF502-Fall2020/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            34 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="67% of commits in October were made to igorsteinmacher/INF502-Fall2020 " class="tooltipped tooltipped-n" style="width: 67%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L3-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/XiwenChen-NAU/INF502/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/XiwenChen-NAU/INF502">XiwenChen-NAU/INF502</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/XiwenChen-NAU/INF502/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            4 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="8% of commits in October were made to XiwenChen-NAU/INF502 " class="tooltipped tooltipped-n" style="width: 8%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/igorsteinmacher/CS499-OSS/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/igorsteinmacher/CS499-OSS">igorsteinmacher/CS499-OSS</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/igorsteinmacher/CS499-OSS/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            4 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="8% of commits in October were made to igorsteinmacher/CS499-OSS " class="tooltipped tooltipped-n" style="width: 8%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/igorsteinmacher/pythonCI_class/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/igorsteinmacher/pythonCI_class">igorsteinmacher/pythonCI_class</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/igorsteinmacher/pythonCI_class/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            3 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="6% of commits in October were made to igorsteinmacher/pythonCI_class " class="tooltipped tooltipped-n" style="width: 6%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/Manoj-Mallidi/INF502/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/Manoj-Mallidi/INF502">Manoj-Mallidi/INF502</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/Manoj-Mallidi/INF502/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            2 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="4% of commits in October were made to Manoj-Mallidi/INF502 " class="tooltipped tooltipped-n" style="width: 4%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/Dahlmannnnn/INF502/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/Dahlmannnnn/INF502">Dahlmannnnn/INF502</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/Dahlmannnnn/INF502/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            2 commits
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="4% of commits in October were made to Dahlmannnnn/INF502 " class="tooltipped tooltipped-n" style="width: 4%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/EfayZ/INF502/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/EfayZ/INF502">EfayZ/INF502</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/EfayZ/INF502/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            1 commit
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="2% of commits in October were made to EfayZ/INF502 " class="tooltipped tooltipped-n" style="width: 2%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    <li class="ml-0 py-1">
    <div class="d-inline-block col-8 css-truncate css-truncate-target lh-condensed">
    <a data-hovercard-type="repository" data-hovercard-url="/JW2372/INF502/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/JW2372/INF502">JW2372/INF502</a>
    <a class="f6 muted-link ml-lg-1 mt-1 mt-lg-0 d-block d-lg-inline" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_COMMIT_RANGE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="102dc4fda4cc774efde1ff499a0194905e86f4e42c6118bf03831a85d4793bb1" href="/JW2372/INF502/commits?author=igorsteinmacher&amp;since=2020-10-01&amp;until=2020-10-30">
            1 commit
    </a> </div>
    <div class="col-3 d-inline-block float-right">
    <div aria-label="2% of commits in October were made to JW2372/INF502 " class="tooltipped tooltipped-n" style="width: 2%">
    <span class="d-flex anim-grow-x progress-bar mt-1" style="background-color: var(--color-calendar-graph-day-L1-bg)"></span>
    </div>
    </div>
    </li>
    </ul>
    </div>
    <div class="profile-rollup-wrapper py-4 pl-4 position-relative ml-3" data-issue-and-pr-hovercards-enabled="" data-repository-hovercards-enabled="">
    <span class="discussion-item-icon"><svg aria-hidden="true" class="octicon octicon-flame" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M7.998 14.5c2.832 0 5-1.98 5-4.5 0-1.463-.68-2.19-1.879-3.383l-.036-.037c-1.013-1.008-2.3-2.29-2.834-4.434-.322.256-.63.579-.864.953-.432.696-.621 1.58-.046 2.73.473.947.67 2.284-.278 3.232-.61.61-1.545.84-2.403.633a2.788 2.788 0 01-1.436-.874A3.21 3.21 0 003 10c0 2.53 2.164 4.5 4.998 4.5zM9.533.753C9.496.34 9.16.009 8.77.146 7.035.75 4.34 3.187 5.997 6.5c.344.689.285 1.218.003 1.5-.419.419-1.54.487-2.04-.832-.173-.454-.659-.762-1.035-.454C2.036 7.44 1.5 8.702 1.5 10c0 3.512 2.998 6 6.498 6s6.5-2.5 6.5-6c0-2.137-1.128-3.26-2.312-4.438-1.19-1.184-2.436-2.425-2.653-4.81z" fill-rule="evenodd"></path></svg></span>
    <div class="d-flex flex-justify-between flex-items-baseline mb-3">
    <h4 class="text-normal text-gray lh-condensed my-0 pr-3">
          Created an issue in
          <a class="link-gray-dark" data-hovercard-type="repository" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_REPO_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="0ba6646054ee14c36f0469f7244d290f4bf987bf19f3b38e6b288aa3be6c0001" href="/igorsteinmacher/INF502-Fall2020">igorsteinmacher/INF502-Fall2020</a>
          that received 1
          comment
        </h4>
    <a class="f6 text-gray-light muted-link no-wrap" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_DATE_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="b03d63284944b251c3ac06cf76b541d92c563aafe09eef7f50d1f3c50b1475b5" href="/igorsteinmacher?tab=overview&amp;from=2020-10-01&amp;to=2020-10-31">
    <time class="no-wrap">Oct 13</time>
    </a> </div>
    <div class="profile-timeline-card bg-white border rounded-1 p-3">
    <svg aria-hidden="true" class="octicon octicon-issue-opened open d-inline-block mt-1 float-left" height="16" title="Open" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg>
    <div class="ml-4">
    <h3 class="lh-condensed my-0">
    <a class="text-gray-dark" data-hovercard-type="issue" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/issues/36/hovercard" href="/igorsteinmacher/INF502-Fall2020/issues/36">Create the first version of the database</a>
    </h3>
    <div class="text-gray mb-0 mt-2">
    <p></p>
    </div>
    <div class="f6 text-gray mt-2">
            1
            comment
          </div>
    </div>
    </div>
    </div>
    <div class="profile-rollup-wrapper py-4 pl-4 position-relative ml-3 js-details-container Details open">
    <span class="discussion-item-icon">
    <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg>
    </span>
    <button aria-expanded="false" class="btn-link f4 muted-link no-underline lh-condensed width-full js-details-target" type="button">
    <span class="float-left ws-normal text-left">
            Opened 4
            other
            issues
            in 1
            repository
          </span>
    <span class="d-inline-block float-right">
    <span aria_label="Collapse" class="profile-rollup-toggle-closed float-right" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_CATEGORY_ROLLUP_COLLAPSE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="cfd9a2f97d3a53e11390526e5625c91063f0a2df2c7c99d49a795873599a16bc"><svg aria-hidden="true" class="octicon octicon-fold" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M10.896 2H8.75V.75a.75.75 0 00-1.5 0V2H5.104a.25.25 0 00-.177.427l2.896 2.896a.25.25 0 00.354 0l2.896-2.896A.25.25 0 0010.896 2zM8.75 15.25a.75.75 0 01-1.5 0V14H5.104a.25.25 0 01-.177-.427l2.896-2.896a.25.25 0 01.354 0l2.896 2.896a.25.25 0 01-.177.427H8.75v1.25zm-6.5-6.5a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM6 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 016 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM12 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 0112 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5z" fill-rule="evenodd"></path></svg></span>
    <span aria_label="Expand" class="profile-rollup-toggle-open float-right" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_CATEGORY_ROLLUP_EXPAND","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="1a2cae486d73dbc25ee0aab926efbe377ef05405f922073d21f5fabab80a1ab7"><svg aria-hidden="true" class="octicon octicon-unfold" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.177.677l2.896 2.896a.25.25 0 01-.177.427H8.75v1.25a.75.75 0 01-1.5 0V4H5.104a.25.25 0 01-.177-.427L7.823.677a.25.25 0 01.354 0zM7.25 10.75a.75.75 0 011.5 0V12h2.146a.25.25 0 01.177.427l-2.896 2.896a.25.25 0 01-.354 0l-2.896-2.896A.25.25 0 015.104 12H7.25v-1.25zm-5-2a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM6 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 016 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5zM12 8a.75.75 0 01-.75.75h-.5a.75.75 0 010-1.5h.5A.75.75 0 0112 8zm2.25.75a.75.75 0 000-1.5h-.5a.75.75 0 000 1.5h.5z" fill-rule="evenodd"></path></svg></span>
    </span>
    </button>
    <div class="profile-rollup-content">
    <div class="profile-rollup-summarized js-details-container Details py-2 open" data-issue-and-pr-hovercards-enabled="" data-repository-hovercards-enabled="">
    <button aria-expanded="false" class="js-details-target d-flex flex-items-baseline btn-link no-underline lh-condensed text-left width-full" data-octo-click="profile_timeline_toggle_rollup_created_issues" type="button">
    <div class="d-inline-block col-6">
    <span class="css-truncate css-truncate-target" data-hovercard-type="repository" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/hovercard">igorsteinmacher/INF502-Fall2020</span>
    </div>
    <span class="col-6 d-inline-block f6 text-gray link-hover-blue float-right text-right">
    <span class="text-white State--red rounded-1 ml-2 px-1">1</span>
              closed
              <span class="text-white State--green rounded-1 ml-2 px-1">3</span>
              open
          </span>
    </button>
    <ul class="mt-1 profile-rollup-content list-style-none">
    <li class="py-1 ml-0">
    <span class="css-truncate css-truncate-target">
    <span class="profile-rollup-icon">
    <svg aria-hidden="true" class="octicon octicon-issue-closed closed" height="16" title="Closed" version="1.1" viewbox="0 0 16 16" width="16"><path d="M1.5 8a6.5 6.5 0 0110.65-5.003.75.75 0 00.959-1.153 8 8 0 102.592 8.33.75.75 0 10-1.444-.407A6.5 6.5 0 011.5 8zM8 12a1 1 0 100-2 1 1 0 000 2zm0-8a.75.75 0 01.75.75v3.5a.75.75 0 11-1.5 0v-3.5A.75.75 0 018 4zm4.78 4.28l3-3a.75.75 0 00-1.06-1.06l-2.47 2.47-.97-.97a.749.749 0 10-1.06 1.06l1.5 1.5a.75.75 0 001.06 0z" fill-rule="evenodd"></path></svg>
    </span>
    <a class="content-title no-underline" data-hovercard-type="issue" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/issues/39/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_ISSUE_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="840ddaaa43632a291d0a558929883d29d8ed50b0a0b067c26ac4b1ae7b2c3ec1" href="/igorsteinmacher/INF502-Fall2020/issues/39">
    <span class="link-gray-dark-underline link-gray-dark">Number 1</span>
    </a> </span>
    <time class="float-right f6 text-gray-light pt-1" title="This contribution was made on Oct 13">
                Oct 13
              </time>
    </li>
    <li class="py-1 ml-0">
    <span class="css-truncate css-truncate-target">
    <span class="profile-rollup-icon">
    <svg aria-hidden="true" class="octicon octicon-issue-opened open" height="16" title="Open" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg>
    </span>
    <a class="content-title no-underline" data-hovercard-type="issue" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/issues/38/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_ISSUE_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="840ddaaa43632a291d0a558929883d29d8ed50b0a0b067c26ac4b1ae7b2c3ec1" href="/igorsteinmacher/INF502-Fall2020/issues/38">
    <span class="link-gray-dark-underline link-gray-dark">Any issue</span>
    </a> </span>
    <time class="float-right f6 text-gray-light pt-1" title="This contribution was made on Oct 13">
                Oct 13
              </time>
    </li>
    <li class="py-1 ml-0">
    <span class="css-truncate css-truncate-target">
    <span class="profile-rollup-icon">
    <svg aria-hidden="true" class="octicon octicon-issue-opened open" height="16" title="Open" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg>
    </span>
    <a class="content-title no-underline" data-hovercard-type="issue" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/issues/37/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_ISSUE_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="840ddaaa43632a291d0a558929883d29d8ed50b0a0b067c26ac4b1ae7b2c3ec1" href="/igorsteinmacher/INF502-Fall2020/issues/37">
    <span class="link-gray-dark-underline link-gray-dark">Create the Business model classes</span>
    </a> </span>
    <time class="float-right f6 text-gray-light pt-1" title="This contribution was made on Oct 13">
                Oct 13
              </time>
    </li>
    <li class="py-1 ml-0">
    <span class="css-truncate css-truncate-target">
    <span class="profile-rollup-icon">
    <svg aria-hidden="true" class="octicon octicon-issue-opened open" height="16" title="Open" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z" fill-rule="evenodd"></path></svg>
    </span>
    <a class="content-title no-underline" data-hovercard-type="issue" data-hovercard-url="/igorsteinmacher/INF502-Fall2020/issues/35/hovercard" data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_ISSUE_LINK","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="840ddaaa43632a291d0a558929883d29d8ed50b0a0b067c26ac4b1ae7b2c3ec1" href="/igorsteinmacher/INF502-Fall2020/issues/35">
    <span class="link-gray-dark-underline link-gray-dark">Grade PA01</span>
    </a> </span>
    <time class="float-right f6 text-gray-light pt-1" title="This contribution was made on Oct 13">
                Oct 13
              </time>
    </li>
    </ul>
    </div>
    </div>
    </div>
    </div>
    </div>
    <!-- '"` --><!-- </textarea></xmp> --></div></div></div></div></div><form accept-charset="UTF-8" action="/igorsteinmacher?tab=overview&amp;from=2020-09-01&amp;to=2020-09-30&amp;include_header=no" class="ajax-pagination-form js-ajax-pagination js-show-more-timeline-form col-lg-10 col-12" data-from="2020-10-01" data-title="igorsteinmacher (Igor Steinmacher) / September 2020" data-to="2020-10-29" data-url="/igorsteinmacher?tab=overview&amp;from=2020-09-01&amp;to=2020-09-30" data-year="2020" method="get">
    <img alt="" class="contribution-activity-spinner col-10 next" src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif">
    <button class="ajax-pagination-btn btn btn-outline width-full f6 mt-0 py-2 contribution-activity-show-more" data-disable-with="Loading..." data-hydro-click='{"event_type":"user_profile.click","payload":{"profile_user_id":2953768,"target":"TIMELINE_SHOW_MORE","user_id":null,"originating_url":"https://github.com/igorsteinmacher"}}' data-hydro-click-hmac="8f8a406e56156a65ecd628edcc6f879c462a9aab790f830acdd7f4f0cac568e9" name="button" type="submit">Show more activity</button>
    <p class="text-gray f6 mt-4">
        Seeing something unexpected? Take a look at the
        <a href="https://docs.github.com/categories/setting-up-and-managing-your-github-profile">GitHub profile guide</a>.
      </p>
    </img></form>
    
    
    
    
    
    
    
    
    <div class="footer container-xl width-full p-responsive" role="contentinfo">
    <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between flex-sm-items-center pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light">
    <a aria-label="Homepage" class="footer-octicon d-none d-lg-block mr-lg-4" href="https://github.com" title="GitHub">
    <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewbox="0 0 16 16" width="24"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
    </a>
    <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
    <li class="mr-3 mr-lg-0">© 2020 GitHub, Inc.</li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
    <li class="js-cookie-consent-preferences-link-container mr-3 mr-lg-0" hidden="hidden">
    <button class="btn-link js-cookie-consent-preferences-link" data-ga-click="Footer, go to cookie preferences, text:cookie preferences" type="button">Cookie Preferences</button>
    </li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to status, text:status" href="https://githubstatus.com/">Status</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to help, text:help" href="https://docs.github.com">Help</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to Pricing, text:Pricing" href="https://github.com/pricing">Pricing</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to api, text:api" href="https://docs.github.com">API</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to training, text:training" href="https://services.github.com">Training</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to blog, text:blog" href="https://github.blog">Blog</a></li>
    <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
    </div>
    <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
    </div>
    </div>
    <div class="ajax-error-message flash flash-error" id="ajax-error-message">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg>
    <button aria-label="Dismiss error" class="flash-close js-ajax-error-dismiss" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg>
    </button>
        You can’t perform that action at this time.
      </div>
    <div class="js-stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z" fill-rule="evenodd"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
    <template id="site-details-dialog">
    <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open="">
    <summary aria-label="Close dialog" role="button"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
    <button aria-label="Close dialog" class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" data-close-dialog="" type="button">
    <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z" fill-rule="evenodd"></path></svg>
    </button>
    <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
    </details>
    </template>
    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
    <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
    </div>
    </div>
    <div class="js-cookie-consent-banner" hidden="">
    <div class="hx_cookie-banner p-2 p-sm-3 p-md-4">
    <div class="Box hx_cookie-banner-box box-shadow-medium mx-auto" style="max-width: 1194px;">
    <div class="Box-body border-0 py-0 px-3 px-md-4">
    <div class="js-main-cookie-banner hx_cookie-banner-main">
    <div class="d-md-flex flex-items-center py-3">
    <p class="f5 flex-1 mb-3 mb-md-0">
                  
      We use <span class="text-bold">optional</span> third-party analytics cookies to understand how you use GitHub.com so we can build better products.
    
                  <span class="btn-link js-cookie-consent-learn-more">Learn more</span>.
                </p>
    <div class="d-flex d-md-block flex-wrap flex-sm-nowrap">
    <button class="btn btn-outline flex-1 mr-1 mx-sm-1 m-md-0 ml-md-2 js-cookie-consent-accept">Accept</button>
    <button class="btn btn-outline flex-1 ml-1 m-md-0 ml-md-2 js-cookie-consent-reject">Reject</button>
    </div>
    </div>
    </div>
    <div class="js-cookie-details hx_cookie-banner-details" hidden="">
    <div class="d-md-flex flex-items-center py-3">
    <p class="f5 flex-1 mb-2 mb-md-0">
                  
      We use <span class="text-bold">optional</span> third-party analytics cookies to understand how you use GitHub.com so we can build better products.
    
                  <br/>
                  You can always update your selection by clicking <span class="text-bold">Cookie Preferences</span> at the bottom of the page.
                  For more information, see our <a href="https://docs.github.com/en/free-pro-team@latest/github/site-policy/github-privacy-statement">Privacy Statement</a>.
                </p>
    </div>
    <div class="d-md-flex flex-items-center py-3 border-top">
    <div class="f5 flex-1 mb-2 mb-md-0">
    <h5 class="mb-1">Essential cookies</h5>
    <p class="f6 mb-md-0">We use essential cookies to perform essential website functions, e.g. they're used to log you in. 
                    <a href="https://docs.github.com/en/github/site-policy/github-subprocessors-and-cookies">Learn more</a>
    </p>
    </div>
    <div class="text-right">
    <h5 class="text-blue">Always active</h5>
    </div>
    </div>
    <div class="d-md-flex flex-items-center py-3 border-top">
    <div class="f5 flex-1 mb-2 mb-md-0">
    <h5 class="mb-1">Analytics cookies</h5>
    <p class="f6 mb-md-0">We use analytics cookies to understand how you use our websites so we can make them better, e.g. they're used to gather information about the pages you visit and how many clicks you need to accomplish a task. 
                    <a href="https://docs.github.com/en/github/site-policy/github-subprocessors-and-cookies">Learn more</a>
    </p>
    </div>
    <div class="text-right">
    <div class="BtnGroup mt-1 mt-md-0 ml-2">
    <button class="btn btn-outline BtnGroup-item js-accept-analytics-cookies" type="button">Accept</button>
    <button class="btn btn-outline BtnGroup-item js-reject-analytics-cookies" type="button">Reject</button>
    </div>
    </div>
    </div>
    <div class="text-right py-3 border-top">
    <button class="btn btn-primary js-save-cookie-preferences" disabled="" type="button">Save preferences</button>
    </div>
    </div>
    </div></div> </div>
    </div>
    





```python
bio = soup.find('div', attrs={'class':'p-note'})
list(bio.children)[0].text

```




    'Assistant Professor @ NAU.\nResearcher: Mining Software Repositories and behavior in Open Source are my main topics'




```python

```
