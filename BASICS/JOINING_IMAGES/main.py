import cv2 
import numpy as np


class Join_img:
    def __init__(self):
        self.path = './static/img.jpg'
        self.normal_img = cv2.imread(self.path)
        self.grey_img = cv2.cvtColor(self.normal_img,cv2.COLOR_BGR2GRAY)
        self.edge_img = cv2.Canny(self.normal_img,100,100)
        self.blur_img = cv2.GaussianBlur(self.normal_img,(5,5),0)

    def set_dim(self):
        # all dimensions should be same 
        self.normal_img = cv2.resize(self.normal_img,(0,0),None,1,1)
        self.grey_img = cv2.resize(self.grey_img,(0,0),None,1,1)
        self.edge_img = cv2.resize(self.edge_img,(0,0),None,1,1)
        self.blur_img = cv2.resize(self.grey_img,(0,0),None,1,1)
    def join_imges_horizontal(self):
        self.set_dim()
        # for verticaly stack  images 
        v_images = np.vstack((self.grey_img,self.edge_img,self.blur_img))

        # for horizontal stack images
        h_images = np.hstack((self.grey_img,self.edge_img,self.blur_img))
        cv2.imshow("H Stack images ",h_images)
        cv2.imshow("H Stack images ",v_images)
        cv2.waitKey(0)

if __name__ == '__main__':
    obj = Join_img()
    obj.join_imges_horizontal()
    