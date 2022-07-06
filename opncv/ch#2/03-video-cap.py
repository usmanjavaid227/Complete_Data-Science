import cv2 as cv

cap=cv.VideoCapture('Resources/video.mp4')

if (cap.isOpened()==False):
    print("Cannot open video")

while (cap.isOpened()):
    ret,frame=cap.read()
    if (ret==True):
        cv.imshow("video",frame)
        if (cv.waitKey(1)& 0xFF==ord("q")):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
