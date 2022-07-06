import cv2 as cv
import numpy as np

img=cv.imread('Resources/img2.png') 
img.shape 
# resized img
r_img=cv.resize(img,(300,200))
# gray img
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blured img 
blurred=cv.GaussianBlur(img,(23,23),0)
#edge Detction
edge=cv.Canny(img,47,47)
# edge thikness
# thikness=cv.dilate(edge,(7,7),iterations=1)
mat_kernal=np.ones((7,7),np.uint8)
thikness=cv.dilate(edge,(mat_kernal),iterations=1)

# thinner edge        
thinner=cv.erode(thikness,(mat_kernal),iterations=1)
# cropped img 
cropped=img[:200,100:]

cv.imshow('Origional',img)
# cv.imshow('resized img',r_img)
# cv.imshow('gray img',gray_img)
# cv.imshow('blured img',blurred)
# cv.imshow('Edged',edge)
# cv.imshow('dilated',thikness)
# cv.imshow('eroted',thinner)
cv.imshow('cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()
