# Writeup 6 - Forensics

Name: Josiah Wedgwood
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Josiah Wedgwood

## Assignment Writeup

### Part 1 (45 Pts)

1) 142.93.136.81 was attacked.

2) The attackers were using some port scanner on the victim's machine to open tcp connections on somewhat randomly chosen ports. The tool used is probably nmap.

3) 159.203.113.181 is the machine initiating the port scan and then the following FTP conversation with the victim. A censys search shows the attackers are connecting from Clifton, NJ, USA.

4) The attackers are using the FTP port 21 to transfer files.

5)
	a) A jpeg file called find_me.jpeg
	b) GPS Latitude: South 34 degrees 57' 29.14" Longitude: West 54 degrees 56' 16.28". This puts the photo taken right at a beach in Maldonado, Uruguay, South America.
	c) 2018/12/23 17:16:24 (yyyy/mm/dd hh:mm:ss)
	d) Apple Iphone 8
	e) The GPSAltitude tag shows 4.5726 m above sea level. This makes sense because the picture clearly shows a beach.

6) The attackers left a file called greetz.fpff on the victim's machine.

7) A simple countermeasure to prevent this intrusion would be to change the login information on the victim's FTP server. The current password is pwned, since the attacker only logged into the FTP server once with the correct credentials instead of making multiple attempts to get the correct password. The replacement password should be unique to the victim and strong enough to prevent brute force attacks.

### Part 2 (55 Pts)

stub.py is my implementation of the fpff parser.

Information about greetz.fpff:

1) greetz.fpff was generated on 2019-03-27 04:15:05.

2) The author is a user named fl1nch

3) There are 5 sections in total (listed in order of appearance in greetz.fpff):
Ascii section: 
Hey you, keep looking :)

Coord section:
This section contains the coordinates Latitude 52.336035, Longitude 4.880673

Png section:
This section contains a png image of testudo cheering, along with the flag CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak} printed sideways

Ascii section:
This contains the reversed flag }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC, which is just CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}

Ascii section:
This section contains the base64 encoded string Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=, which when decoded shows the flag CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}

4) Flags found: 
CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}
CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}

