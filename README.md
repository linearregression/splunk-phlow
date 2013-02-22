splunk-flowy-flowy
==================

This is a Splunk configuration for consuming flow data.

### Design Review

"splunk flowy flowy" is an amalgamation of 
- NFCAPD 
- iNotify 
- nfcapd-ascii bash script,  

### Contributors

@jcwx - John Weir - INOC

@rupack89 - Rupak Pandya Function1

@sometheycallme (Tim) - International Securities Exchange


### references / mashup

This cisco whitepaper on the relevant fields for extracting data from flows was helpful when we built the app.

http://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html

We also used the field references here

http://www.ietf.org/rfc/rfc3954.txt
http://en.wikipedia.org/wiki/NetFlow

We rely on inotify to get data out of binary nfcapd into ascii format

http://linuxaria.com/article/introduction-inotify?lang=en



### Our Wiki

https://github.com/sometheycallme/splunk-flowy-flowy/wiki




