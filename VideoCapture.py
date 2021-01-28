# -*- coding: utf-8 -*-
"""
Created on Thu Dez 01 08:14:40 2021

@author: dngom
Abrir webcam
"""

import cv2

video = cv2.VideoCapture(0)

while True:
    conectado, frame = video.read()
    
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()