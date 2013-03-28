## Got phlow? 

<img src="https://raw.github.com/phlowy/splunk-phlow/master/phlow-assets/flow.png" width="250" height="250" />


splunk-phlow
==================

This is an application for consuming netflow v5,7,9 data using NFDUMP, iNotify, Binary-ASCII coverter, and Splunk!

<img src="https://raw.github.com/phlowy/splunk-phlow/master/phlow-assets/phlowdash.png" width="750" height="400" />


### Overview

Splunk Phlow is an amalgamation of 
- NFDUMP
- iNotify 
- nfcapd-ascii bash script
- logrotate
- tito (for the RPM)
- cron (to handle scheduling)
- init scripts (to handle service starting)
- puppet (out of scope - but to get this built/rebuilt/rebuilt/......rebuilt and stable)
- custom Splunk app: Splunk Phlow

### Contributors

[@jcwx John Weir](https://github.com/jcwx) 

[@rupak98 - Rupak Pandya](https://github.com/Rupak98) 

[@sometheycallme - Tim Kropp](https://github.com/sometheycallme) 

[@sorandom - Sandeep Khaneja](https://github.com/sorandom) 

[@jumanjiman - Paul Morgan](https://github.com/jumanjiman) 

[@vpalacio - Victor Palacio](https://github.com/vpalacio) 


### references / mashup

This cisco whitepaper on the relevant fields for extracting data from flows was helpful when we built the app.

http://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html

We also used the field references here

http://www.ietf.org/rfc/rfc3954.txt
http://en.wikipedia.org/wiki/NetFlow

We rely on NFDUMP to get data into binary and off the stack.

http://nfdump.sourceforge.net

We rely on inotify to get data out of binary nfcapd into ascii format

http://linuxaria.com/article/introduction-inotify?lang=en

### Our Wiki

https://github.com/sometheycallme/splunk-flowy-flowy/wiki
