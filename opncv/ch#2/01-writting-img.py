import cv2 as cv
# read image file
img=cv.imread("Resources/img.jpg")
# convert into gray format
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# write image
cv.imwrite("Resources/gray_img.jpg",gray)
# display image
cv.imshow("image",gray)
# delay image
cv.waitKey(0)
# Exit image
cv.destroyAllWindows()