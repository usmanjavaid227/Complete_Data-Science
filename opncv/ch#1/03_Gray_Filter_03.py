# Read as display an image and apply gray filter
import cv2 as cv

img=cv.imread("Resources\img.jpg")
img=cv.resize(img,(800,600))
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("tesri",img)
cv.imshow("4th",gray_img)
cv.waitKey(0)
cv.destroyAllWindows()