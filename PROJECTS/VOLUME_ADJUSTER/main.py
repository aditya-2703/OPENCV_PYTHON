# Here i use previously made module named hand tracking which u will find in hand tracking repo
# for controlling module i used pycaw which is opensource library
import Hand_tracking_module as htm
import  cv2
import numpy as np
import time
import math


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# setting custom width and height of screen or window
width=1280
height=720


# capturing vdo
vdo = cv2.VideoCapture(0)
vdo.set(3,width)
vdo.set(4,height)

# manage fps
current_time=0
previous_time=0

# using hand tracking module
detector = htm.Handtrack(detectionCon=0.7)

# initialization of pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_obj = cast(interface, POINTER(IAudioEndpointVolume))


# volume.GetMute()
# volume.GetMasterVolumeLevel()

# the volume range is between -65.25 to 0
volume_range = volume_obj.GetVolumeRange()
min_vol_range = volume_range[0]
max_vol_range = volume_range[1]


# initialization of variable
volume=0
volume_percentage=0
volume_bar=400


while True:

    flag,img_frame = vdo.read()

    # for updating image
    img_frame = detector.track(img_frame)
    
    # for finding position of hand dimensions
    landmark_list = detector.findposition(img_frame,custom_draw=False)

    # now will have the list of landmarks so first will check if the list is exists or not if exists then will do next move
    if landmark_list:
        # as we see in image and our aim we only need two fingers one is thumb and the first finger so index or id of those is 4 and 8
        print(landmark_list[4],landmark_list[8])

        # list[[id,x,y],[id,x,y]]
        thumb_x ,thumb_y =landmark_list[4][1] ,landmark_list[4][2]
        finger_x ,finger_y =landmark_list[8][1] ,landmark_list[8][2]
        # center of line
        center_x,center_y = (thumb_x+finger_x)//2,  (thumb_y+finger_y)//2


        # now we have to hightlight it so that we see the changes or marks
        cv2.circle(img_frame,(thumb_x,thumb_y),15,(255,255,255),cv2.FILLED)
        cv2.circle(img_frame,(finger_x,finger_y),15,(255,255,255),cv2.FILLED)
        cv2.circle(img_frame,(center_x,center_y),15,(255,255,255),cv2.FILLED)
        
        # line between those two thumb and finger
        cv2.line(img_frame,(thumb_x,thumb_y),(finger_x,finger_y),(255,255,0),3)

        # for finding length between those two circles so that we adjust volume 
        length = math.hypot(finger_x-thumb_x,finger_y-thumb_y)
        print(length)

        # hand range is between 50-300 
        # volume range is between -65.25 to 0 
        # so we have to make both equal somehow
        # for that will have functoin in numpy 
        volume = np.interp(length,[50,300],[min_vol_range,max_vol_range])
        print(volume)

        # for bar you can see below
        volume_bar= np.interp(length,[150,300],[400,150])
        
        # now our volume is ready so we have to set to 
        volume_obj.SetMasterVolumeLevel(volume, None)

        # for percentage of volume
        volume_percentage = np.interp(length,[50,300],[0,100])

        if length<50:
            cv2.circle(img_frame,(center_x,center_y),15,(0,0,0),cv2.FILLED)

    # for showing volume bar in screen or window for nice ux
    # bar len is 85  - 50 = 35 which is our length
    # initialization of bar
    cv2.rectangle(img_frame,(50,150),(85,400),(255,0,255),3)
    # change in bar after changing volume
    # for this bar again we have to change range

    # when the height/volume is full bar should be 150
    # when the height/volume is 0 bar should be 400

    # this initializatoin of bar is you can see above

    cv2.rectangle(img_frame,(50,int(volume_bar)),(85,400),(255,0,255),cv2.FILLED)




    # setting fps
    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time

    # draw fps 
    cv2.putText(img_frame,"FPS : "+str(int(fps)),(20,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,0),2)

    # for draw percentage of volume 
    cv2.putText(img_frame,str(int(volume_percentage))+"%",(20,460),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,255),2)

    cv2.imshow("img",img_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
