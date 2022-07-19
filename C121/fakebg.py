import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("OIF.jpg") 
  
while True: 
  
    ret, frame = video.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
  
    lower_yellow = np.array([23, 80, 10])
    upper_yellow = np.array([35, 255,255])
  
    mask = cv2.inRange(frame, lower_yellow, upper_yellow) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows() 