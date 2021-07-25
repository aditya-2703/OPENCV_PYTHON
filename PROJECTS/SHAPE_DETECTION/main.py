import cv2
import numpy as np



class Detect_shape:
    def __init__(self,image,img_flag):

        
        self.normal_vdo = cv2.VideoCapture(0)

        # Set Value Windows 
        cv2.namedWindow("threshold")
        # cv2.createTrackbar('threshold1','threshold',26,255,self.empty)
        # cv2.createTrackbar('threshold2','threshold',23,255,self.empty)
        cv2.createTrackbar('Area',"threshold",5000,30000,self.empty)
        # normal_img = cv2.imread('./static/circle.png')

        self.image = image
        self.is_img_or_vdo_flag=img_flag

    def empty(self,a):
        pass

    def get_contorous(self,img,imgcontorous):
        contorous,hirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        # for remove noice 
        for cont in contorous:
            area = cv2.contourArea(cont)
            min_area = cv2.getTrackbarPos('Area','threshold')
            if area>min_area:
                # cv2.drawContours(imgcontorous,cont,-1,(0,0  ,255),7)
                peri = cv2.arcLength(cont,True)
                approx = cv2.approxPolyDP(cont ,0.02* peri,True)
                x,y,w,h = cv2.boundingRect(approx)
                cv2.rectangle(imgcontorous,(x,y),(x+w,y+h),(0,255,0),5)
                cv2.putText(imgcontorous, " points :  " + str(len(approx)),(x+w+20,y+20),cv2.FONT_HERSHEY_COMPLEX,.7,(255,0,0),2)
                cv2.putText(imgcontorous, " Area :  " + str(int(area)),(x+w+20,y+45),cv2.FONT_HERSHEY_COMPLEX,.7,(255,0,0),2)

    def main(self):        
        while True:

            if self.is_img_or_vdo_flag:
                img = self.image
            else:
                flag,img = self.normal_vdo.read()
                img = cv2.resize(img,(400,500))
            imgcont = img.copy()

            Blur_img = cv2.GaussianBlur(img,(7,7),1)
            gray_img = cv2.cvtColor(Blur_img,cv2.COLOR_BGR2GRAY)
            
            # if you use trackbar
            # threshold1 = cv2.getTrackbarPos('threshold1','threshold')
            # threshold2 = cv2.getTrackbarPos('threshold2','threshold')
            
            # or 
            threshold1 = 26
            threshold2 = 23

            Canny_img = cv2.Canny(gray_img,threshold1,threshold2)
            kernel = np.ones((5,5))
            dialate_img = cv2.dilate(Canny_img,kernel,iterations=1)
            

            # Blur_img = Blur_img.reshape((Blur_img.shape[0],Blur_img.shape[1],3))
            # gray_img  =gray_img.reshape((gray_img.shape[0],gray_img.shape[1],3))
            # Canny_img=Canny_img.reshape((Canny_img.shape[0],Canny_img.shape[1],3))
            # dialate_img =dialate_img.reshape((dialate_img.shape[0],dialate_img.shape[1],3))

            
            self.get_contorous(dialate_img,imgcont)
            
            # stack_img = np.hstack([gray_img,Canny_img,dialate_img])

            # cv2.imshow("img stack",stack_img)
            cv2.imshow("img stack",imgcont)



            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


image_path = cv2.imread('./static/img.png')
# if you want to detect image then make is_image  flag true else false
is_image = False
detect_obj = Detect_shape(image_path,is_image)
detect_obj.main()