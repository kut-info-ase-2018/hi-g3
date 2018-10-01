#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# motion.py
import threading
import RPi.GPIO as GPIO
import time
import event
import datetime

class MotionSensor(object):

    def __init__(self):
      self.INTAVAL = 2
      self.SLEEPTIME = 1
      self.SENSOR_PIN = 17
      self.event_handlers = event.Event()

    def detect(self, sender, earg):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.SENSOR_PIN, GPIO.IN)
      self.term = time.time() - self.INTAVAL
      while True:
        try:
          if(GPIO.input(self.SENSOR_PIN)==GPIO.HIGH) and (self.term + self.INTAVAL < time.time()):
            print time.clock()
            self.term = time.time()
            self.image_detail = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
            self.event_handlers(self, self.image_detail)
          time.sleep(self.SLEEPTIME)

        except KeyboardInterrupt:
            print("break motion")
            break