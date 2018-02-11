from sys import argv
from time import sleep

# Set time to first argument
time = argv[1]

# Set seconds to integer representation of time
seconds = int(time)

# Make sure time provided is greater than or equal to zero
if(seconds < 0):
    print("Time must be greater than or equal to zero")
    quit()

# Start countdown
while(seconds > 0):
    print(str(seconds) + " second(s) remaining...")
    seconds -= 1
    sleep (1)
print("Beep! Beep! Beep! " + time + " second(s) have passed!")
