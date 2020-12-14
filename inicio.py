import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic/elon1.jpg')
imgElon = cv2.cvtColor(imgElon.cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_img_file('ImagesBasic/elon2.jpg')

faceLoc = face_recognition.face_locations()

cv2.imshow('elon1'.imgElon)
cv2.imshow('elon2'.imgTest)
cv2.waitKey(0)