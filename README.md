splunk-flowy-flowy
==================

This is a Splunk configuration for consuming flow data using nfcapd, inotify, ascii-conversion, universal forwarder, and splunk views


## Design Review

"splunk flowy flowy" is an amalgamation of 
- NFCAPD 
- iNotify 
- nfcapd-ascii bash script,  

### Contributors

@jcwx - John Weir - INOC
@rupack89 - RupaFunction1
@sometheycallme (Tim) - International Securities Exchange

### references

This cisco whitepaper on the relevant fields for extracting data from flows was helpful when we built the app.

http://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html

We also used the field acronyms in this 


### splunk configuration for splunk-flowy-flowy

[INDEX = netflow_si_traffic] to be created.

[SOURCETYPE = netflow]

Data resides on [IC-SPK03 == /var/log/nfdump-ascii]

The files are written every minute.

Requirements:

- Take the ASCII converted files.  Get them into splunk, with index and source type above.  This can be accomplished with the serverclass.conf  and new deployment-app called ''ise-netfow''.  the app would be responsible for telling the universal forwarder to splunk data located in the ASCII folder listed in  3) below.    

- Then - we can use the field extractions to make a version of this netflow-integrator app from splunk base that works for ISE.

Sounds simple - but really is a bit of work for us.  LETS GO!

### how the data gets massaged for indexing

Summary:
1) nfcap is running as a service - in order to get the data off of the stack and into the /var/log/nfcap directory
-opens port
-listens to flows
-stores them as binary nfcap files in log directory


2) nfdump-ascii.sh script is responsible for the data conversion & inotify

```
#!/bin/sh

# CONFIGURATION
DIR="/var/log/nfcapd/"
EVENTS="moved_to"
FIFO="/tmp/inotify2.fifo"

# FUNCTIONS
on_exit() {
kill $INOTIFY_PID
rm $FIFO
exit
}

on_event() {
local date=$1
local time=$2
local file=$3

sleep 5

#echo "$date $time moved to: $file"
/usr/bin/nfdump -qr "$DIR""$file" -o csv > /var/log/nfdump-ascii/nfdump-ascii."$date"."$time".log
}

# MAIN
if [ ! -e "$FIFO" ]
then
mkfifo "$FIFO"
fi

inotifywait -m -e "$EVENTS" --timefmt '%Y-%m-%d %H:%M:%S' --format '%T %f' "$DIR" > "$FIFO" &
INOTIFY_PID=$!

trap "on_exit" 2 3 15

while read date time file
do
on_event $date $time $file &
done < "$FIFO"


on_exit
```

###  ascii nfdump script would need to be modified to run as a service (init script needed)
<i> WE can probably run this as part of the pre-processing init script (which we don't quite have yet) </i>

```
[root@ic-spk03 nfdump-ascii]# ps -ef | grep ascii
root     16453     1  0 Feb08 ?        00:00:00 su -m nfcapd /usr/local/bin/nfdump-ascii.sh
uc4      16454 16453  0 Feb08 ?        00:00:08 bash /usr/local/bin/nfdump-ascii.sh
root     30398 28794  0 11:11 pts/1    00:00:00 grep --color ascii
```


3) upon successful running of the scripts above in 1 and 2, we basically get ASCII conversion of the nfcapd binaries on a minute to minute basis.    The file is a consolidation of all netflow data into a single file from any host reporting.    

example:

PWD 
/var/log/nfdump-ascii

[root@ic-spk03 nfdump-ascii]#

.....
  nfdump-ascii.2013-02-22.11:17:00.log



3) inotify triggers the 
