# import modules
import cv2
import time 
import hand_track_module as htm
import os


# initaialization of htm
obj = htm.Handtrack()

# loading all images into one array
folder = "images"
img_list  =os.listdir("images")
# load this so that we not get error of path 
image_list = []
for i in img_list:
    image = cv2.imread(f"{folder}/{i}")
    image_list.append(image)

# for video capturing
vdo = cv2.VideoCapture(1)
vdo.set(3,1000)
vdo.set(4,700)

# fingers array
fingers = [4,8,12,16,20]

while True:
    flag,img_frames = vdo.read()
    # to show actual vdo not mirror one 
    img_frames = cv2.flip(img_frames,1)

    # for tracking hand
    img_frames = obj.track(img_frames)

    # displaying images
    img_frames[:image_list[0].shape[0],:image_list[0].shape[1]] = image_list[0]

    # tracking position list
    tracking_pos_list = obj.findposition(img_frames)
    # in those  list we perticularly want this the id which present in fingers array
    # [4,8,12,16,20]

    Countingarr = []
    


    if len(tracking_pos_list)>1:
        if tracking_pos_list[fingers[0]][1] > tracking_pos_list[fingers[0]-1][1]:
            Countingarr.append(0)
        else:
            Countingarr.append(1)

        for id in fingers[1:]:
            if tracking_pos_list[id][2] < tracking_pos_list[id-2][2]:
                Countingarr.append(1)
            else:
                Countingarr.append(0)
    
        # now we have our counting array ready which has 1 if finger is up and 0 if is not 
        # will sum that and find out what is count
        count = sum(Countingarr)
        # now will simply show this with images 
        # image shape 
        w , h = image_list[count-1].shape[0],image_list[count-1].shape[1]
        img_frames[:w,:h] = image_list[count-1]
        cv2.putText(img_frames , f"Count : {count}",(10,200),cv2.FONT_HERSHEY_PLAIN,2,(0, 0, 0),4)

    cv2.imshow("images",img_frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
