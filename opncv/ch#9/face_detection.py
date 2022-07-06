import cv2 as cv 
 
face_cascade =cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img=cv.imread('Resources/group-faces.WEBP')
# print(img.shape)
img=cv.resize(img,(426,455))
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,1.1,4)

# draw a rectengele
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()