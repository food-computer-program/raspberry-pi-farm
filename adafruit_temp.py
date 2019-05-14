#get the temperature from the blue temperature sensor
import sys
import Adafruit_DHT

#read the temperature and humidity from the blue (DHT11) sensor
#hold the sensor to get a different reading!
humidity, temperature = Adafruit_DHT.read_retry(11,4)

#print out the temperature and humidity readings   
print('Temp: {0:01f} C Humidity: {1:0.1f} %'.format(temperature, humidity))


