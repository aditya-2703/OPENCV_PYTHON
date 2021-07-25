import cv2 
import numpy as np
from numpy.core.shape_base import hstack


# 0 111 0 139 136 255

def empty(a):
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV',640,240)
cv2.createTrackbar('Hue min','HSV',0,179,empty)
cv2.createTrackbar('Hue max','HSV',179,179,empty)
cv2.createTrackbar('Sat min','HSV',0,255,empty)
cv2.createTrackbar('Sat max','HSV',255,255,empty)
cv2.createTrackbar('Value min','HSV',0,255,empty)
cv2.createTrackbar('Value max','HSV',255,255,empty)

# image = cv2.imread('./static/img.jpg')
vdo = cv2.VideoCapture(0)

while True:
    
    flag , img = vdo.read()
    img=cv2.resize(img,(400,300))
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos('Hue min','HSV')
    h_max=cv2.getTrackbarPos('Hue max','HSV')
    s_min=cv2.getTrackbarPos('Sat min','HSV')
    s_max=cv2.getTrackbarPos('Sat max','HSV')
    v_min=cv2.getTrackbarPos('Value min','HSV')
    v_max=cv2.getTrackbarPos('Value max','HSV')
    
    # h_min = 0
    # h_max = 111
    # s_min = 0
    # s_max = 139
    # v_min = 136
    # v_max = 255



    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    result2 = cv2.bitwise_and(imgHsv,imgHsv,mask=mask)

    # mask  = mask.reshape((225,225,3)) 

    # print(result.shape,result2.shape,image.shape,imgHsv.shape)

    main = np.hstack([img,imgHsv,result,result2])

    cv2.imshow('Main',main)

    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break

