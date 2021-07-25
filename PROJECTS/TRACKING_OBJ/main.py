import cv2

webcam = cv2.VideoCapture(0)
tracker = cv2.TrackerMOSSE_create()   
flag,img_frame = webcam.read()
bounding_box = cv2.selectROI("Tracking",img_frame,False)
tracker.init(img_frame,bounding_box)

def draw(img,bounding_box):
    x,y,width,height = int(bounding_box[0]),int(bounding_box[1]),int(bounding_box[2]),int(bounding_box[3])
    cv2.rectangle(img,(x,y),(x+width,y+height),(255,255,0),3,1)
    cv2.puText(img_frame,"Tracking Enable",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

while True:
    timer = cv2.getTickCount()

    flag,img_frame = webcam.read()
    flag,img_frame = tracker.update(img_frame)
    if flag:
        draw(img_frame,bounding_box)
    else:
        cv2.puText(img_frame,"Can't Track",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

    fps = cv2.getTickFrequency()/(cv2.getTickCount() -timer)
    cv2.putText(img_frame,"FPS : "+str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255))
    cv2.imshow("webcam",img_frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break