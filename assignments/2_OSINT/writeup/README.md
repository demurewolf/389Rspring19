# Writeup 2 - OSINT

Name: Josiah Wedgwood 
Section: 0101 

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (45 pts)

v0idcache's real name: Elizabeth Moffet

She is a banking CEO for 1337bank.money in the Netherlands

Personal info + social media accounts:
Twitter handle: @v0idcache
Reddit account: u/v0idcache
Business email: v0idcache@protonmail.com 

I used checkusername.com to see which websites already had a user with the username v0idcache, and it came up with the Reddit and Twitter accounts.

The business email came directly from v0idcache's website 1337bank.money

IPs found: 
142.93.136.81 - from using dig on 1337bank.money. I used censys.io to confirm that the server is in Amsterdam, NL and that the IP is registered under a DigitalOcean license

Hidden files + directories:
Git repository found on port 80 from nmap scan. The flag is CMSC389R-{h1d3_s3cret_g1ts}
Hidden directory on 1337bank.money/secret_directory. The flag is CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

Open ports:
TCP 22 - ssh
TCP 25 - smtp (This port is filtered, and doesn't appear when running a port scan with t1shopper.com)
TCP 80 - http
TCP 1337 - This service was unrecognized by nmap (waste?) but revealed some packets prompting for a username and password.
TCP 11211 - memcache

Ports 22, 25, and 80 were found using nmap as `nmap -A 1337bank.money`. The -A flag was an attempt for OS discovery, but there wasn't an exact match from nmap. Ports 1337 and 11211 were only found after using `nmap -sV -p1-65535` and causing a lot of network disruption to 1337bank.money.

v0idcache is running Ubuntu on their website. This was found by using censys.io to search for 1337bank.money. 

Additional flags:
Reddit - CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}

### Part 2 (75 pts)

Flag from v0idcache's server: CMSC389R-{brut3_f0rce_m4ster}
Login credentials:
- username: v0idcache
- password: linkinpark

For this part of the assignment, I first used 'nc 142.93.136.81 1337' to first test the login
prompt. I then entered a dummy username and password to see what would happen on an incorrect
login attempt. I then framed my stub.py script to also make a connection to v0idcache's server,
and send, at first, one username and password combination to the server. After getting this
step to work, I then refactored the program to submit login requests for each password in
the rockyou.txt password list file, with v0idcache as the attempted username (this was just
an initial guess, because this same username is used on other social media accounts). My
brute-force script would keep making login requests as log as the script received the 'Fail'
message from v0idcache's server. It stops making requests on the first login attempt that
receives something different than a fail message, and then it prints the data sent by
v0idcache's server and the password used in the login attempt. This case occurred when the
script used 'linkinpark' as the password, at which point v0idcache's server sent 'Success!'
and now we have a valid username/password combination for the server.

I found the flag in 'flag.txt' under the home directory of v0idcache's server, as well as a 
large directory of flag files simply called 'files/'.
