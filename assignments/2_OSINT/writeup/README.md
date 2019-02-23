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

All ports were found using nmap as `nmap -A 1337bank.money`. The -A flag was an attempt for OS discovery, but there wasn't an exact match from nmap.

v0idcache is running Ubuntu on their website. This was found by using censys.io to search for 1337bank.money. 

Additional flags:
Reddit - CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}

### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*
