# Read as display an image
import cv2 as cv
    # To read a file
img=cv.imread("Resources\img.jpg")
    # To display an image
cv.imshow("Pahli",img)
    # delay execution
cv.waitKey(0)
cv.destroyAllWindows()
