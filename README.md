## Got flowy flowy?   |;>|

<img src="https://raw.github.com/sometheycallme/splunk-flowy-flowy/master/assets/flowy.png" width="250" height="250" />


splunk-flowy-flowy
==================

This is a Splunk configuration for consuming netflow v5,7,9 data.


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



### License

The MIT License (MIT)
Copyright (c) 2013 - @sometheycallme @jcwx @rupak98

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

