# Read as display an image and resize it.
import cv2 as cv

img=cv.imread("Resources\img.jpg")
img1=cv.resize(img,(800,600))

cv.imshow("pahli",img)
cv.imshow("Dusri",img1)
cv.waitKey(0)
cv.destroyAllWindows()