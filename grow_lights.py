#control grow lights for the food computer from a Raspberry Pi
import RPi.GPIO as GPIO
from time import sleep

#identify where the lights are connected to the Raspberry Pi
# in this case, we’re attaching it to the GPIO Pin 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

#set the schedule for the lights to go on and off

#for brevity, we’re going to test a short light schedule 3 times
for i in range(3):
    #the next three lines of code turn the lights on for 2 seconds
    # change the number after “sleep” to keep the lights on or off for different amounts of time! 
    GPIO.output(7, GPIO.HIGH)
    print('light is on') #print out a statement to let us know the lights should be on
    sleep(2)
    #the next three lines of code turn the lights off for 2 seconds
    GPIO.output(7, GPIO.LOW)
    print('light is off') #print out a statement to let us know the lights should be off
    sleep(2)

