#!/bin/bash

cd /var/infoscreen-munich

git pull

flask run &

firefox -url "127.0.0.1:5000" -new-window --kiosk

exit 0
