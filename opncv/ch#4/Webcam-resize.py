import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
cap.set(10,80) # key 10 is specific for brightness
cap.set(3,1920) # key 3 is for width
cap.set(4,1080) # key 4 is for height
while (True):
    (ret,frame)=cap.read()
    # grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # (thresh,b_w)=cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    if (ret==True):
        cv.imshow("Origional video",frame)
        if (cv.waitKey(1)& 0xFF==ord("q")):
            break
cap.release()
cv.destroyAllWindows()
