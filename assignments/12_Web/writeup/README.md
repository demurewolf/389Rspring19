# Web Writeup

Name: Josiah Wedgwood
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (40 Pts)

* First clicked around the Vuln shop webpage and observed how the webpage url changes
* Each individual exploit's webpage was from the /item resource on the shop, just with changing values for the id parameter in the url
* The title led to SQL, so use SQL injection on the /item page of the Vuln shop
* Tried using values such as ```0' or '1'='1' -- ``` for the id parameter but the webpage would load the error page for sql injection
* I then went searching for alternate ways to express this sql injection and then I changed the ```or``` to ```||```
* The above alteration showed a webpage with the shop information from each exploit sold and then the info for a secret flag exploit that can be bought for $1337

Flag: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

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

* Opening target code shows a variable next that get changed to direct the user's sign up process
* On the signup page, the next button at the bottom is set with an a href tag as ```<a href="{{ next }}">Next >></a>```
* From Flask's security page (http://flask.pocoo.org/docs/1.0/security/), there's a section explaining how Jinja does not protect agains a href tags from executing javascript, so changing the next variable in the URL can embed xss

URL to embed xss (needs user to trigger by clicking next button)
```raw
https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('unsafe');
```

Level 6:

* Opening target code showed how the includeGadget program sanitizes the url given in the anchor
* ```if (url.match(/^https?:\/\//))``` only matches agains either http:// or https:// in the url, but it's not case sensitive. Variations like hTTps:// or HTTPS:// will not match
* Pastebin can host a js script that calls the alert function
* Making the anchor hTTps://pastebin.com/Bg2Y5jAY does not seem to make the program execute. The gadget only needs the file, not the pastebin webpage, so changing it to the download link would fix that.

URL anchor to execute xss:
```raw
hTTps://pastebin.com/dl/Bg2Y5jAY
```

