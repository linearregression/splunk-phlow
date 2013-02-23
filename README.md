## Got flowy flowy?   
<img src="https://raw.github.com/flowy-flowy/splunk-flowy-flowy/master/assets/flowy.png" width="250" height="250" />


splunk-flowy-flowy
==================

This is an application for consuming netflow v5,7,9 data using NFDUMP, iNotify, Binary-ASCII coverter, and Splunk!

<img src="https://raw.github.com/flowy-flowy/splunk-flowy-flowy/master/assets/nfdash2.png" width="750" height="250" />


### Overview

"splunk flowy flowy" is an amalgamation of 
- NFCAPD 
- iNotify 
- nfcapd-ascii bash script
- logrotate
- tito (for the RPM)
- cron (to handle scheduling)
- init scripts (to handle service starting)
- puppet (out of scope - but to get this built/rebuilt/rebuilt/......rebuilt and stable)
- custom Splunk app: splunk-flowy-flowy :)

### Contributors

[@jcwx John Weir](https://github.com/jcwx) 

[@rupak98 - Rupak Pandya](https://github.com/Rupak98) 

[@sometheycallme - Tim Kropp](https://github.com/sometheycallme) 


### references / mashup

This cisco whitepaper on the relevant fields for extracting data from flows was helpful when we built the app.

http://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html

We also used the field references here

http://www.ietf.org/rfc/rfc3954.txt
http://en.wikipedia.org/wiki/NetFlow

We rely on nfcapd to get data into binary and off the stack.

http://nfdump.sourceforge.net

We rely on inotify to get data out of binary nfcapd into ascii format

http://linuxaria.com/article/introduction-inotify?lang=en

### Our Wiki

https://github.com/sometheycallme/splunk-flowy-flowy/wiki
