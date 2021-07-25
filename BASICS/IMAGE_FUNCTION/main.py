import cv2
import numpy as np

class Image_function:
    def __init__(self):
        self.path = './static/img.png'
        self.img = cv2.imread(self.path)
    def normal_img(self):
        self.show_img(self.img)
    def show_img(self,image):
        image=cv2.resize(image,(400,500))
        cv2.imshow("Normal img",image)  
        cv2.waitKey(0) 
    def gray_img(self):
        image_gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        self.show_img(image_gray)
    def edge_img(self):
        # canny - para(image,threshold 1,threshold 2) thrshold increseas then edges decreases
        image_edge  = cv2.Canny(self.img,100,100)
        self.show_img(image_edge)
    def blur_img(self):
        # blur - para(image,(k-size,k-size),sigma) k-size(always odd) increases  then blur increase
        image_blur = cv2.GaussianBlur(self.img,(9,9),0)
        self.show_img(image_blur)

    def dialate_img(self):
        #for increases this edge size will use dialation
        # dialate - para(image,matarix,iterations) as iteration increases then thickness  increases
        image_edge  = cv2.Canny(self.img,100,100)
        kernel = np.ones((5,5),np.int)
        image_dialate =  cv2.dilate(image_edge,kernel,iterations=1) 
        self.show_img(image_dialate)

    def erode_img(self):
        # this is reverse of dialation 
        # this decreases the size of thickness
        image_edge  = cv2.Canny(self.img,100,100)
        kernel = np.ones((5,5),np.int)
        image_dialate =  cv2.dilate(image_edge,kernel,iterations=1) 
        image_erode = cv2.erode(image_dialate,kernel,iterations=1)
        # you can see that we get almost same image after this erode after performing dialation to prove dialation  is reverse of erode
        self.show_img(image_erode)


if __name__ == '__main__':
    obj = Image_function()
    # obj.normal_img()
    # obj.gray_img()
    # obj.edge_img()
    # obj.blur_img()
    # obj.dialate_img()
    obj.erode_img()