import cv2
import time
import numpy as np

#Starting the webcam
cap = cv2.VideoCapture(0)
bg=cv2.imread("OIF.jpg")
while (cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.resize(frame,(650,450))
    bg=cv2.resize(bg,(650,450))

    lower_yellow = np.array([23, 80, 10])
    upper_yellow = np.array([35, 255,255])
    mask=cv2.inRange(frame,lower_yellow,upper_yellow)
    r=cv2.bitwise_and(frame,frame,mask=mask)
    f=frame-r
    f=np.where(f==0,bg,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release() 
cv2.destroyAllWindows()






























