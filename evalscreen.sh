#!/bin/sh

export DISPLAY=:0.0
export XAUTHORITY=/home/pi/.Xauthority

timestamp=$(date +"%Y%m%d%H%M%S")
filename="/home/pi/evalscreen/screen_$timestamp.png"

scrot -q 20 "$filename"

$(dirname "$0")/evalimage.py "$filename"

if [ $? -eq 0 ]
then
    echo $(date -u) "OK"
else
    echo $(date -u) "Aborted->Refresh"
    xdotool key --window $(xdotool getactivewindow) ctrl+R
fi