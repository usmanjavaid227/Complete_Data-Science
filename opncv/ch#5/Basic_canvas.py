import cv2 as cv
import  numpy as np

# Draw a canvas 0 for Black
img=np.zeros((600,600))
# img1=np.ones((600,600))
colored=np.zeros((600,600,3),np.uint8) # color channel addition
colored[:]=255,190,90 # colored complete img
colored[150:250,150:250]=5,100,200 # colored complete img
cv.line(colored,(0,0),(600,600),(255,100,140),3)
# cv.line(colored,(30,30),(colored.shape[0],colored.shape[1]),(125,200,140),3)
cv.rectangle(colored,(50,50),(130,190),(240,0,255),cv.FILLED)
cv.circle(colored,(500,400),(50),(100,0,255),cv.FILLED)
cv.putText(colored,"Test",(200,500),cv.FONT_HERSHEY_DUPLEX,2,255,0,2)

# cv.imshow("Black",img)
# cv.imshow("White",img1)
cv.imshow("White",colored)



cv.waitKey(0)
cv.destroyAllWindows()