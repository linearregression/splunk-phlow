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

### references

This cisco whitepaper on the relevant fields for extracting data from flows was helpful when we built the app.

http://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html

We also used the field references 

http://www.ietf.org/rfc/rfc3954.txt
http://en.wikipedia.org/wiki/NetFlow


### splunk configuration details for splunk-flowy-flowy

The index we created:

[INDEX = netflow_si_traffic] 

The source type

[SOURCETYPE = netflow]

Data resides on [Splunk Forwarder Host == /var/log/nfdump-ascii]

The files are written every minute.

Requirements:

- Take the ASCII converted files.  
- Get them into splunk, with index and source type above.  
- This can be accomplished with the serverclass.conf  and new deployment-app called ''<your-company-name>-netfow''. 
- The app would be responsible for telling the universal forwarder to splunk data located in the ASCII folder listed in item 3) below.    
- Then - we can use the field extractions and field aliases to populate dashboards for splunk-flowy-flowy

Sounds simple - but is a bit of legwork.

Props.conf

```
[netflow]
# For the new nfdump output format that includes router_ip
EXTRACT-flow = \d{4}-\d{2}-\d{2}\s\d{1,2}:\d{1,2}:\d{1,2}\.\d{1,3}\s+(?<duration>\d+\.\d+)\s+(?<protocol>\w+)\s+(?<src_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<src_port>\d{1,5})\s+->\s+(?<dest_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<dest_port>\d{1,5})\s+(?<tcp_flag>[\w\.]+)\s+(?<tos>\d+)\s+(?<packets>\d+)\s+(?<bytes>\d+)\s+(?<pps>\d+)\s+(?<bps>\d+)\s+(?<bpp>\d+)\s+(?<flow_count>\d+)\s+(?<exp_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
 
SHOULD_LINEMERGE = false
FIELDALIAS-proto = protocol AS proto
FIELDALIAS-srcip = src_ip AS srcip
FIELDALIAS-srcport = src_port AS srcport
FIELDALIAS-dstip = dest_ip AS dstip
FIELDALIAS-dst_ip = dest_ip AS dst_ip
FIELDALIAS-dstport = dest_port AS dstport
FIELDALIAS-dst_port = dest_port AS dst_port
FIELDALIAS-flags = tcp_flag AS flags
FIELDALIAS-num_packets = packets AS num_packets
FIELDALIAS-num_bytes = bytes AS num_bytes
FIELDALIAS-num_flows = flow_count AS num_flows
FIELDALIAS-router_ip = exp_ip AS router_ip
```
 
# For the nfdump output format: extended
#EXTRACT-flow = \d{4}-\d{2}-\d{2}\s\d{1,2}:\d{1,2}:\d{1,2}\.\d{1,3}\s+(?<duration>\d+\.\d+)\s+(?<proto>\w+)\s+(?<srcip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<srcport>\d{1,5})\s+->\s+(?<dstip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<dstport>\d{1,5})\s+(?<flags>[\w\.]+)\s+(?<tos>\d+)\s+(?<num_packets>\d+)\s+(?<num_bytes>\d+)\s+(?<pps>\d+)\s+(?<bps>\d+)\s+(?<bpp>\d+)\s+(?<num_flows>\d+)
# For the (default) output format: line
# EXTRACT-flow = \d{4}-\d{2}-\d{2}\s\d{1,2}:\d{1,2}:\d{1,2}\.\d{1,3}\s+(?<duration>\d+\.\d+)\s+(?<proto>\w+)\s+(?<srcip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<srcport>\d{1,5})\s+->\s+(?<dstip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?<dstport>\d{1,5})\s+(?<num_packets>\d+)\s+(?<num_bytes>\d+)\s+(?<num_flows>\d+)
 
lookup_proto = protocol_lookup protocol
lookup_srcport = port_lookup port AS src_port OUTPUT service AS src_service
lookup_dstport = port_lookup port AS dest_port OUTPUT service AS dest_service

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

[root@yourhost nfdump-ascii]#

.....
  nfdump-ascii.2013-02-22.11:17:00.log




