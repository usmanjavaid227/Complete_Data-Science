import cv2 as cv 
cap = cv.VideoCapture(0)
frame_width = int(cap.get(3)) # 3 is used to get the width 
frame_height = int(cap.get(4)) # 4 is used to get the height 
# for mp4 use ("M", "J", "P", "J") while for avi use ("M", "J", "P", "G") depeds on type you want to save
out = cv.VideoWriter("Resources/cam_video.mp4", cv.VideoWriter_fourcc("M", "J", "P", "G"), 30, (frame_width, frame_height))
while(True):
  (ret, frame) = cap.read()
  # to showshow in player
  if ret == True:
    #  write the frame
    out.write(frame)
    # Display the resulting frame
    cv.imshow('My Video', frame)
   
    # Press Q on keyboard to  exit
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break
cap.release()
out.release()
   
# Closes all the frames
cv.destroyAllWindows()
