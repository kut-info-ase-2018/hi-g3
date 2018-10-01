#!/usr/local/bin/python
# -*- coding: utf-8 -*-
###/usr/bin/python
# upload.py

import pysftp
import threading
import time

up_lock = threading.RLock()

class Uploader(object):

  def __init__(self):
    self.HOST = '172.21.42.152'
    self.PORT = 22
    self.USER = 'iwatalab'
    self.PRIVATE_KEY_FILE = '/home/pi/.ssh/id_rsa'
    self.uploadPath = '/home/iwatalab/upload_image'
    global uploader_lock

  def upload(self, sender, earg):
    with up_lock:
      starttime = time.time()
      self.uploadPath = '/home/iwatalab/upload_image'
      self.fPath = '/home/pi/Rewrite/monitoring/img/' + earg + '.jpg'
      sftp = pysftp.Connection(self.HOST, username=self.USER, port=self.PORT, private_key=self.PRIVATE_KEY_FILE)
      sftp.listdir()
      sftp.chdir(self.uploadPath)
      sftp.getcwd()
      sftp.put(self.fPath)
      sftp.close()

      interval = starttime - time.time()
      print(str(interval) + "秒")