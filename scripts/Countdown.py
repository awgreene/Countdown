#!/usr/bin/python
from time import sleep
seconds = 10
while(seconds > 0):
    print(str(seconds) + " second(s) remaining...")
    seconds -= 1
    sleep (1)
print("Beep! Beep! Beep! 10  second(s) have passed!")
