#!/usr/bin/python3
import Adafruit_DHT
import os
import logging
import time

### Gdzie dodawać fragment logging.basicConfig, na początku czy końcu programu?
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

from datetime import datetime

period = 900
DHT11_pin = 23


def get_mesure():
  time = datetime.now()
  sensor = Adafruit_DHT.DHT11
  humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
  logging.info(f"Wilgotność {humidity} % Temp {temperature} *C")



 # dane = ('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

get_mesure()
logic = True
while logic == True:
  get_mesure()
  time.sleep(period)
