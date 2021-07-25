import cv2
import numpy as np


points = np.zeros((4,2),np.int)
index = 0

# this function will print the co-ordinates of point which we click
def mouse_point_event(event,x,y,flag,parameters):
    global index
    # here we click each time the co-ordinate updated
    if event == cv2.EVENT_LBUTTONDOWN:
        points[index] = x,y 
        index+=1
        # index = (index)%(4)
        # print(points)
img = cv2.imread('./static/book.jpg')



# pattern is top_left top_right ,bottom_left ,bottom_right ,
while True:

    if index == 4:
        width=300
        height=400
        points1 = np.float32([points[0],points[1],points[2],points[3]])
        # for final product dim
        points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


        matrix =cv2.getPerspectiveTransform(points1,points2)
        output = cv2.warpPerspective(img,matrix,(width,height))

        cv2.imshow('final result',output)

    for x in range(4):
        cv2.circle(img,(points[x][0],points[x][1]),15,(0,255,0),cv2.FILLED)

    cv2.imshow('image',img)
    cv2.setMouseCallback('image',mouse_point_event)
    
    # press q for break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break