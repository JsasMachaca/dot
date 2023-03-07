#!/bin/bash

status=$(bluetoothctl show | grep "Powered" | awk '{print $2}')

if [ $status = "yes" ];then

	echo "%{F#F9107A}"

elif [ $status = "no" ];then 

	echo "%{F#6D6D6D}"

fi
