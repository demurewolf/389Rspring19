# Writeup 3 - Operational Security and Social Engineering

Name: Josiah Wedgwood
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (40 pts)

Call Elizabeth Moffet as a concerned IT technician from Ziggo, one of the Netherlands largest ISP, and claim there's unusual/missing activity from her business IP address. 

To prove she's the CEO of 1337Bank and one of our essential customers, I would have her vocally answer the security question: What is your mother's maiden name? At this point, her identity would be 'validated' and I have her mother's maiden name.

I would run her through some internet connectivity test, like trying to access facebook or www.ziggo.nl, through the browser of her choice. Without giving any suggestions, Elizabeth should naturually use her preferred browser to check the internet, and then upon successfully connecting to the test websites I can then ask what browser is she using.

### Part 2 (60 pts)

Vulnerabilities:
1) Open port w/ weak login password

This vulnerability lets an adversary have direct access to and control of 1337Bank's server. Weak passwords compromise the security of a given account because adversaries can guess or brute-force weak passwords more easily than stronger passwords.

I first recommend changing the password on v0idcache's account to a stronger alternative. Stronger passwords are longer and more complex than weaker passwords, but they should not be easy to guess. As an example, the current password 'linkinpark' is weak because it only has lowercase letters and it is a name of a popular music group, which makes it easier to guess. A stronger alternative would be something similar to '!Park_L1nk1n', which is stronger because it includes lowercase letters, uppercase letters, symbols, and numbers.

2) Unnecessarily opened port

This vulnerability is mainly a problem due to the service listening on it requiring a weak password, but adversaries now have an additional attack vector on 1337Bank's server because port 1337 is opened. The service behind the port is a remote terminal, but port 22 also has a secure SSH service for a remote terminal too.

I recommend simply closing port 1337, and then establishing SSH keys on 1337Bank's server with admins who regularly log into the server. SSH is a secure network protocol that allows remote login and command execution (the service on port 1337 also provided these features), but establishes private and public SSH keys for remote users connecting to the server. Using SSH keys is stronger than only using a login password because the keys are tied to the employee's devices and 1337Bank's server can validate the users who should have remote access. 

3) Website login form can reveal admin account info

This vulnerability shows that making a HTTP request 1337Bank's server is not prepared to handle causes the server to crash, at which point an adversary can look at the crash log returned to see the admin login credentials the server uses.

I recommend patching 1337Bank's server so that all non-'POST' http requests are ignored. This would suppress any crash or exception logs that would otherwise occur if an adversary used this login form as an attack vector, and then the adversary would not be able to read source code from those logs.
