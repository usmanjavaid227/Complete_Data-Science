import cv2 as cv

cap=cv.VideoCapture('Resources/video.mp4')

while (True):
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,b_w)=cv.threshold(frame,127,255,cv.THRESH_BINARY)
    
    if (ret==True):
        # cv.imshow("video",grayframe)
        cv.imshow("video",b_w)
        if (cv.waitKey(1)& 0xFF==ord("q")):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
