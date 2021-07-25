import cv2 
import numpy as np

class Draw_shape:
    def __init__(self,width,height):
        self.width = width
        self.height =height 
        # here 3 is for rgb colorfull img or canvas
        self.canvas = np.zeros((self.width,self.height,3),np.uint8) 
    def fill_color(self):
        # which is blue color (bgr)
        self.canvas[:] = 255,0,0
        cv2.imshow("Canvas",self.canvas)
        cv2.waitKey(0)
    def draw_shape(self):
        # (img startingpoing endingpoint color thickness)
        cv2.line(self.canvas,(0,0),(self.canvas.shape[0],self.canvas.shape[1]),(255,255,0),2)
        cv2.line(self.canvas,(0,self.canvas.shape[1]),(self.canvas.shape[0],0),(255,255,0),2)
        cv2.circle(self.canvas,(256,256),50,(255,255,0),2)
        for i in  range(1,512):
            cv2.circle(self.canvas,(256,256),(i*10)+50,(255,255,0),2) 
        cv2.rectangle(self.canvas,(0,0),(256,256),(0,0,0),4)
        cv2.rectangle(self.canvas,(256,0),(512,256),(0,0,0),4)
        cv2.rectangle(self.canvas,(0,256),(256,512),(0,0,0),4)
        cv2.rectangle(self.canvas,(256,256),(512,512),(0,0,0),4)
        cv2.putText(self.canvas,"My Shapes",(70,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
        cv2.imshow("Canvas with line",self.canvas)
        cv2.waitKey(0)






if __name__ == '__main__':
    obj = Draw_shape(512,512)
    obj.fill_color()
    obj.draw_shape()
    