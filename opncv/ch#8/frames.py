import cv2 as cv 
import numpy as np 

cap=cv.VideoCapture('Resources/video.mp4')
frameno=0

while True:
    ret,frame=cap.read()
    if ret:
        cv.imwrite(f"Resources/frames/Frame_{frameno}.jpg",frame)
    else:
        break
    frameno=frameno+1

cap.release()
cv.waitKey(0)
cv.destroyAllWindows()
    
