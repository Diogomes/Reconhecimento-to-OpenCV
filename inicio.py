import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('elon1.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('elon2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#faceLoc = face_recognition.face_locations(imgElon)[0]
#encodeElon = face_recognition.face_encodings(imgElon)[0]
#cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[2]),(255,0,255),2)
''
cv2.imshow('elon1',imgElon)
cv2.imshow('elon2',imgTest)
cv2.waitKey(0)
