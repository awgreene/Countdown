#!/usr/bin/python
from os import environ
from time import sleep

time = environ['TIMEOUT']
seconds = int(time)
if(seconds < 0):
    print("TIMEOUT must be greater than or equal to zero")
    quit()

while(seconds > 0):
    print(str(seconds) + " second(s) remaining...")
    seconds -= 1
    sleep (1)
print("Beep! Beep! Beep! " + time + " second(s) have passed!")
