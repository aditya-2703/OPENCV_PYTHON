import mediapipe as mp 
import cv2
import time

from mediapipe.python.solutions.hands import HandLandmark




   

class Handtrack:
    def __init__(self) :
        

        # here will use google mediapipe module for hand tracking
        self.mphand = mp.solutions.hands
        self.hands = self.mphand.Hands() 
        # first will initialize model or module

        # we also want to draw the line and marks on hand easy to understand so we have to manage this by
        self.mpdraw = mp.solutions.drawing_utils

    # this function will take image as parameter and draw all lines and dots and return new image
    def track(self,img_frame):
        # then will read each frame 
        # first will convert to rgb bcz module requires rgb manner
    
        imgrgb = cv2.cvtColor(img_frame,cv2.COLOR_BGR2RGB)     
        # after converting bgr to rgb will give this frame to process function in hands object
        # this function will give dimension of tracking by processing 
    
    
        self.results = self.hands.process(imgrgb)
        # if will got this dimensions then will do this
        
        if self.results.multi_hand_landmarks:
            # this there is not single dimensions there are many more so will have to iterate through it 
            for handlandmark  in self.results.multi_hand_landmarks:
                # will use this dimensions and draw landmarks
                # for puting lines among this dots will add HAND_CONNECTIONS
                self.mpdraw.draw_landmarks(img_frame,handlandmark,self.mphand.HAND_CONNECTIONS)

        return img_frame 
    
    # this function returns the positions of hands as list
    def findposition(self,img,handNo=0,custom_draw=True):

        landmark_list= []

        # if we detect any dimensions or hand then will 
        if self.results.multi_hand_landmarks:
            # for particular hand location 
            myhand = self.results.multi_hand_landmarks[handNo]
            
            
            for id,lm in enumerate(myhand.landmark):
                height,width,c = img.shape
                cx ,cy = int(lm.x*width),int(lm.y*height)
                
                # print(f"id->{id},x->{cx} y->{cy}")

                # will not append all the element in list for ease of access
                landmark_list.append([id,cx,cy])

                # if user wants custom draw then 
                if custom_draw:
                    # for hightlight will draw custom big circle
                    cv2.circle(img,(cx,cy),5,(0,255,0))
        
        return landmark_list

def main():

    vdo = cv2.VideoCapture(0)

    # for managing fps 
    previous_time=0
    current_time=0

    # object of handdetector class
    object  = Handtrack()


    while True:
        flag,img_frame=vdo.read()

        # updating new drawwing image frames 
        img_frame = object.track(img_frame)

        # for getting position list
        landmark_list = object.findposition(img_frame)
        if landmark_list:
            # by giving appropriate index of finger point will extract it's dimension
            print(landmark_list[4])

        # for managing fps

        current_time = time.time()
        fps = 1/(current_time-previous_time)
        previous_time = current_time

        # put this fps on screen or window
        cv2.putText(img_frame,"FPS: "+str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

        cv2.imshow("Vdo",img_frame)

        if cv2.waitKey(1) & 0xFF==ord('q') :
            break





if __name__ == '__main__':
    main()
    