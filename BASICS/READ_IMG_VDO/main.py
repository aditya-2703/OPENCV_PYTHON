import cv2


class Image_show:

    def __init__(self):

        # load images
        self.image = cv2.imread('./static/image.png')
    
    def show_image(self):
        # show images
        cv2.imshow('Name of window',self.image)

        # for engaged the screen with user 
        # 1000 -> 1s
        # 0 -> infinite
        cv2.waitKey(0)

class Video_show:
    def __init__(self):
        self.frame_width = 660
        self.frame_height = 500
        # for use of webcam just put 0 in path
        # self.video =  cv2.VideoCapture(0)
        self.video = cv2.VideoCapture('./static/video.mp4')
 
    # video is nothing but just collections of images 
    def show_vdo(self):
        
        while True:
            success_flag,images_frame  = self.video.read()
            
            # for resizing vdo or img
            images_frame = cv2.resize(images_frame , (self.frame_width,self.frame_height))

            cv2.imshow("Name of window",images_frame)

            # for breaking loop 
            # if press q then break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    
    vdo = Video_show()
    vdo.show_vdo()
    