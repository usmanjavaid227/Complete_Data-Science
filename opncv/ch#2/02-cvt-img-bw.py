import cv2 as cv

img=cv.imread("Resources/img2.png")
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh,b_w=cv.threshold(gray,127,255,cv.THRESH_BINARY)

cv.imshow("image",b_w)
cv.waitKey(0)
cv.destroyAllWindows()