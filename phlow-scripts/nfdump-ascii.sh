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
