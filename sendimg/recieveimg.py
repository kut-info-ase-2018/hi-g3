# -*- coding:utf-8 -*-
#!/usr/bin/python
import socket  
import numpy  
import cv2  

  
def getimage():
    #IPアドレスとポート番号は環境に応じて変更
    HOST = "192.168.11.21"
    PORT = 80
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    sock.connect((HOST,PORT))   
    sock.send('HELLO\n')  
    buf=''   
    recvlen=100  
    while recvlen>0:  
        receivedstr=sock.recv(1024*8)  
        recvlen=len(receivedstr)  
        buf +=receivedstr  
    sock.close()  
    narray=numpy.fromstring(buf,dtype='uint8')  
    return cv2.imdecode(narray,1)  
  
while True:  
    img = getimage()
    cv2.imshow('Capture',img)  
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break