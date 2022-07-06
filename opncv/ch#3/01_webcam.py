import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
if (cap.isOpened()==False):
    print("Can't Capture")
while (cap.isOpened()):
    (ret,frame)=cap.read()
    # grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # (thresh,b_w)=cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    if (ret==True):
        cv.imshow("video",frame)
        if (cv.waitKey(1)& 0xFF==ord("q")):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
