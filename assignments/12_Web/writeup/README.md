# Web Writeup

Name: Josiah Wedgwood
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (40 Pts)
TODO

### Part 2 (60 Pts)

Level 1:
* First tried inputing the string "test" to see how page changes normally.
* Query text is displayed in bold in the DOM
* Toggling the target code shows that the query text is directly embedded into the DOM between the tags <b> and </b>
* Using the query "<script>alert("test")</script>" shows an alert on the results page and the expected bold text is no longer present.

Query to execute xss:
```html
<script>alert("test")</script>
```

Level 2:
* First I just tried "<script>alert("test")</script>" in the message field to see that the message is turns blank on the webpage, but there's no script execution
* I was honestly stuck on this level. Even though I could embed other html elements in the webpage, I couldn't get the <script> element to work directly
* Using the final hint "This level is sponsored by the letters i, m and g and the attribute onerror.", I quickly looked up what the onerror attribute is for html elements.
* Now knowing about onerror, I used ```"<img src="/doesnotexist" onerror="alert('test')">"``` to save an xss vector on the webpage
  
Message to execute xss:
```html
<img src="/doesnotexist" onerror="alert('test')">
```

Level 3:

* Opened the target code and examined how the chooseTab(num) function showed images on the webpage
* chooseTab directly puts the num parameter in the img src with ```html += "<img src='/static/level3/cloud" + num + ".jpg' />";```
* Clicked on an image to see how URL changes -- #number is appended to URL depending on the image clicked
* I then tried getting the javascript parser to close the image src name and then insert the onerror attribute to execute my xss

URL to execute xss:
```raw
https://xss-game.appspot.com/level3/frame#' onerror='alert("test")'/>
```

Level 4:

* Opened target code and saw that user input is inserted as ```onload="startTimer('{{ timer }}');" ```
* Using ```5');// ``` as the input starts the timer function with 5 seconds and escapes the '); from the onload attribute
* Added an alert between the comments and the semicolon to get ```5');alert("test");// ``` and this executes the alert

Input to execute xss:
```raw
5');alert("test");//
```

Level 5:
TODO

Level 6:
TODO

