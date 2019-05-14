from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

#get the temperature from the temperature sensor on the LED screen
temp = sense.get_temperature()

#we get a number with a lot of numbers after the decimal, so we use this code to round that value
round_temp = round(temp,2)

#display the temperature from the LED screen
sense.show_message("The temperature is "+ str(round_temp)+ " degrees Celsius")

