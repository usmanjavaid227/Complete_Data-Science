import cv2 as cv 
# Create a VideoCapture object and read from input file
cap = cv.VideoCapture('Resources/video.mp4')
# cap = cv2.cvtColor(cap, cv2.COLOR_RGB2GRAY)
frame_width = int(cap.get(3)) # 3 is used to get the width 
frame_height = int(cap.get(4)) # 4 is used to get the height 
# for mp4 use ("M", "J", "P", "J") while for avi use ("M", "J", "P", "G") depeds on type you want to save
out = cv.VideoWriter("Resources/out_video.mp4", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width, frame_height), isColor = False )
while(True):
  (ret, frame) = cap.read()
  grayframe = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
  # (thresh, grayframe) = cv2.threshold(grayframe, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  # to showshow in player
  if ret == True:
    #  write the frame
    out.write(grayframe)
    # Display the resulting frame
    cv.imshow('My Video', grayframe)
   
    # Press Q on keyboard to  exit
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break
cap.release()
out.release()
   
# Closes all the frames
cv.destroyAllWindows()
