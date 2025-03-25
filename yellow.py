import numpy as np
import cv2
import requests

import time

cap=cv2.VideoCapture(0)

time.sleep(2)

background=0

#capturing background image
for i in range(30):
  ret, background = cap.read()


while(cap.isOpened()):

    ret,img = cap.read()

    if not ret:
        break

    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSB

    #HSV values

    lower_yellow=np.array([25,120,95])
    upper_yellow=np.array([35,255,255])
    mask1=cv2.inRange(hsv,lower_yellow,upper_yellow)   #Separating the cloak part

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,
                              np.ones((3,3),np.uint8), iterations=2)   #noise removal
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,
                              np.ones((3,3),np.uint8), iterations=1)

    mask2=cv2.bitwise_not(mask1)     #except the cloak

    res1=cv2.bitwise_and(background,background,mask=mask1)  #used for segmentation of the color
    res2=cv2.bitwise_and(img,img,mask=mask2)   #Used to substitute the cloak part
    final_output=cv2.addWeighted(res1,1,res2,1,0)


    cv2.imshow('Eureka!!', final_output)
    k = cv2.waitKey(10)
    if (k==27):
        break
cap.release()
cv2.destroyAllWindows()
