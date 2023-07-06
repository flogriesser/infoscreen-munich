#!/bin/bash

# Set the GPIO mode
gpio mode 1 up

# Set the pin as an input
gpio mode 26 in

echo "Waiting for sensor to settle"
sleep 2

echo "Detecting motion"

while true; do
    if [ $(gpio read 26) -eq 1 ]; then
        echo "Motion Detected!"
        vcgencmd display_power 1
        sleep 300 #Sleep 5 Minutes
    fi
    sleep 5
    vcgencmd display_power 0
done

