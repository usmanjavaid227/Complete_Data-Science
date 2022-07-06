import cv2 as cv 
cap = cv.VideoCapture(0)
while(True):
  (ret, frame) = cap.read()
  grayframe = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
  (thresh, binary) = cv.threshold(grayframe, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
  # to showshow in player
  if ret == True:
    cv.imshow('My Video', frame)
    cv.imshow(' Video', grayframe)
    cv.imshow('2 Video', binary)
       
    # Press Q on keyboard to  exit
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break
cap.release()
# Closes all the frames
cv.destroyAllWindows()
