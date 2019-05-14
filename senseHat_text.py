#display a message on the LED screen
from sense_hat import SenseHat
from time import sleep

sense=SenseHat()

#this code will display a message on the LED screen
#change the green text inside the “” to display your own message
#change the scroll speed to be faster (lower number) or faster (higher number)
#change the text color to make your message a different color; (0,0,225) is blue, (0,225,0) is #green, (225,0,0) is red; type different numbers to make your own color!
sense.show_message("Let's make a Food Computer!", scroll_speed = 0.1, text_colour = (255,225,225)) 

