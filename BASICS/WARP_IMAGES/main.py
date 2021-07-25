import cv2 
import numpy as np


# our goal is to cut blackjack from list of cards 

# for warp image or cut image we should have our dimensions - for ease we also do in with mouse interaction will see in another repo
# here this points are get with the use of ms paint

top_left = [224,91]
top_right =  [432,137]
bottom_left = [162,378]
bottom_right = [368,427]
width,height = 400,500

# for cutting image the dim
points1 = np.float32([top_left,top_right,bottom_left,bottom_right])
# for final product dim
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

image  = cv2.imread('./static/img.jpg')
# cv2.circle(image,(points1[0][0],points1[0][1]),5,(0,0,255),cv2.FILLED)
# cv2.circle(image,(points1[1][0],points1[1][1]),5,(0,0,255),cv2.FILLED)
# cv2.circle(image,(points1[2][0],points1[2][1]),5,(0,0,255),cv2.FILLED)
# cv2.circle(image,(points1[3][0],points1[3][1]),5,(0,0,255),cv2.FILLED)

matrix =cv2.getPerspectiveTransform(points1,points2)
output = cv2.warpPerspective(image,matrix,(width,height))

cv2.imshow('image',image)
cv2.imshow('final result',output)

cv2.waitKey(0)

