#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# shoot.py
import threading
import os
import time
import datetime

capture_lock = threading.RLock() # lock object

class Camera(object):

  def __init__(self):
   self.todaydetail = datetime.datetime.today()
   global capture_lock

  def shutter(self, sender, earg):
    with capture_lock:
      print time.clock()
      starttime = time.time()
      print("-----撮影中-----")
      os.system('raspistill -o ' + earg + '.jpg -vf -hf -w 1024 -h 768 -t 1000 -ex antishake')
      os.system('mv ' + earg + '.jpg img')
      interval = starttime - time.time()
      print(str(interval) + "秒")
      time.sleep(1)
