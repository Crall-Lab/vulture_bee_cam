#!/bin/bash

#source ~/Desktop/bombusbox-setup.sh #this command pulls all the environmental variables that we set in setup.sh into this script
DATE=$(date +"%Y-%m-%d") #This record the current date with format YYYY-MM-DD
DATETIME=$(date +"%Y-%m-%d_%H-%M-%S") #Records current date and time with format YYYY-MM-DD_HH-mm-SS
OUTPUT=/mnt/data/"$HOSTNAME"_"$DATE"/"$HOSTNAME"_"$DATETIME".mjpeg
#OUTPUT="$VIDEO_DIRECTORY"/"$HOSTNAME"_"$DATE"/"$HOSTNAME"_"$DATETIME"."$CODEC"

sudo mkdir -p /mnt/data/"$HOSTNAME"_"$DATE"

#Set to record for 9 minutes and 50 seconds each video
libcamera-vid --width 4608 --height 2592 --codec mjpeg -o "$OUTPUT" --nopreview -t 20000 --framerate 20
echo video recorded!
