import os
import RPi.GPIO as GPIO

INTAVAL = 2
SLEEPTIME = 1
SENSOR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

if(GPIO.input(SENSOR_PIN)==GPIO.HIGH):
  os.system('raspistill -o test1.jpg')
else:
  print('pin is low')


