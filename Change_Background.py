import cv2
import numpy as np

#capturing from the web cam
cap = cv2.VideoCapture(0)

#capturing from th mobile camera using ipwebcam
# url = "https://192.168.0.101:8080/video"
# cap = cv2.VideoCapture(url)

def resize(dst,img):
	width = img.shape[1]
	height = img.shape[0]
	dim = (width, height)
	resized = cv2.resize(dst, dim, interpolation = cv2.INTER_AREA)
	return resized

back=cv2.imread('./image.jpg')

while (cap.isOpened()):
    ret, frame=cap.read()
    back = resize(back,frame)
    # Here return is true if web cam is working and false otherwise
    # frame is the frames capturing by webcam

    if ret:
       hsvFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
       #cv2.imshow("hsv",hsvFrame)

       #lower=hue-10,100,100 higher:hue+10,100,100
       red=np.uint8([[[0,0,255]]]) #BGR of red colour

       #get HSV of red from BGR of red
       hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

       #threshold value to get red colour
       # lower_red=np.array([0,100,100])
       # higher_red=np.array([10,255,255])

       # lower_blue = np.array([110, 50, 50])
       # higher_blue = np.array([130, 255, 255])

       lower_blue = np.array([170, 50, 50])
       higher_blue = np.array([180, 255, 255])

       #all things are red
       mask=cv2.inRange(hsvFrame,lower_blue,higher_blue)
       #cv2.imshow("mask",mask)

       kernel = np.ones((5, 5), np.uint8)
       mask = cv2.dilate(mask, kernel, iterations=1)

       # part1 is all things that are red
       part1=cv2.bitwise_and(back,back,mask=mask)
       # cv2.imshow("part1",part1)

       mask=cv2.bitwise_not(mask)

       #part2 is all things that are not red
       part2 = cv2.bitwise_and(frame, frame, mask=mask)

       cv2.imshow("final", part1+part2)

    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()