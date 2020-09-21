#!/usr/bin/python3
import Adafruit_DHT
import os

from datetime import datetime



def get_mesure():
  time = datetime.now()
  sensor1 = Adafruit_DHT.DHT11



time = datetime.now()
sensor = Adafruit_DHT.DHT11
DHT11_pin = 23
path = '/home/pi/AdminStuff'


humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
if humidity is not None and temperature is not None:
  dane = ('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  file = open("dht11_data.log", "a")
  file.write(str(time) + " " + dane + "\n")
  file.close()
  
else:
  print('Failed to get reading from the sensor.')


def get_mesure():
  time = datetime.now()
  sensor1 = Adafruit_DHT.DHT11
  