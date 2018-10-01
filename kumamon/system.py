#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python

import pysftp
from time import time, sleep, clock
import RPi.GPIO as GPIO
import os
from datetime import datetime

INTAVAL = 2
SLEEPTIME = 1
SENSOR_PIN = 17
HOST = '172.21.42.152'
PORT = 22
USER = 'iwatalab'
PRIVATE_KEY_FILE = '/home/pi/.ssh/id_rsa'
uploadPath = '/home/iwatalab/upload_image'

exe_time = datetime.now().minute
upload_time = 2
exe_time = exe_time + upload_time

f = open('system_pid.txt', 'w')
f.write(str(os.getpid()))
f.close()

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def my_callback_upload():
  starttime = time()
  fName = datetime.today().strftime("%Y%m%d_%H%M%S")
  os.system('tar -cf ' + fName + '.tar img')
  fPath = '/home/pi/Rewrite/monitoring/' + fName + '.tar'
  sftp = pysftp.Connection(HOST, username=USER, port=PORT, private_key=PRIVATE_KEY_FILE)
  sftp.listdir()
  sftp.chdir(uploadPath)
  sftp.getcwd()
  sftp.put(fPath)
  sftp.close()
  os.system('rm /home/pi/Rewrite/monitoring/img/*')
  interval = starttime - time()
  print(str(interval) + "秒")

def my_callback_time(channel):
    print clock()

def my_callback_shoot(channel):
  print clock()
  starttime = time()
  print("-----撮影中-----")
  todaydetail = datetime.today().strftime("%Y%m%d_%H%M%S")
  os.system('raspistill -o ' + todaydetail + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
  os.system('mv ' + todaydetail + '.jpg img')
  interval = starttime - time()
  print(str(interval) + "秒")
  sleep(SLEEPTIME)

GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING)
GPIO.add_event_callback(SENSOR_PIN, my_callback_time)
GPIO.add_event_callback(SENSOR_PIN, my_callback_shoot)

while True:
  if(exe_time >= 60):
    exe_time = exe_time - 60

  if(exe_time == datetime.now().minute):
    #my_callback_upload()
    exe_time = exe_time + upload_time

  sleep(SLEEPTIME)

GPIO.cleanup()
