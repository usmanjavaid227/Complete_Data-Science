#how to change persepacticve of img
import cv2 as cv
import numpy as np
img=cv.imread("Resources/img.jpg")
# print(img.shape)
points1=np.float32([[227,243],[427,241],[199,471],[447,475]])
points2=np.float32([[0,0],[640,0],[0,640],[640,640]])

matrix=cv.getPerspectiveTransform(points1,points2)
output_img=cv.warpPerspective(img,matrix,(640,640))

cv.imshow("original",img)
cv.imshow("war",output_img)

cv.waitKey(0)
cv.destroyAllWindows()