import cv2

class Resize_img:
    def __init__(self,width,height):
        self.width = width
        self.height= height
        self.path =  './static/img.png'
        self.img = cv2.imread(self.path)
    def resize_img(self):
        resized_img = cv2.resize(self.img,(self.width,self.height))
        shape = resized_img.shape
        print(shape)
        cv2.imshow("Resized Image",resized_img)
        cv2.waitKey(0)


class Crop_img:
    def __init__(self,width,height):
        self.width = width
        self.height= height
        self.path =  './static/img.png'
        self.img = cv2.imread(self.path)
    def croped_img(self):
        # height,width
        cropped_img = self.img[800:,0:]
        cv2.imshow("Cropped img",cropped_img)
        cv2.waitKey(0)


if __name__ == '__main__':
    # R_size_obj = Resize_img(100,100)
    # R_size_obj.resize_img()

    C_img_obj = Crop_img(500,500)
    C_img_obj.croped_img()
    