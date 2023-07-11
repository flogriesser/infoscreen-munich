import sys
from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

sleep(30)

while True:
    if GPIO.input(21):
        print("Motion Detected")
        subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "on"])
        sleep(300)
    else:
        subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "off"])
        print("No Motion")
