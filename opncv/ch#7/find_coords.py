import cv2 as cv
import numpy as np

# Define a function
def find_coords(event,x,y,flags,params):
    # left mouse button
    if event==cv.EVENT_LBUTTONDOWN:
        print(x,'',y)
        font=cv.FONT_HERSHEY_DUPLEX
        cv.putText(img,str(x)+","+str(y),(x,y),font,1,(255,0,90))
        cv.imshow("image",img)
# for color finding
    if event==cv.EVENT_RBUTTONDOWN:
        print(x,"",y)
        font =cv.FONT_HERSHEY_TRIPLEX
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        cv.putText(img,str(b)+","+str(g)+","+str(r),(x,y),font,1,(255,100,0),2)

if __name__=="__main__":
    # reading an image 
    img=cv.imread("REsources/img.jpg",1)
    cv.imshow("image",img)
    cv.setMouseCallback("image",find_coords)
    cv.waitKey(0)
    cv.destroyAllWindows()
