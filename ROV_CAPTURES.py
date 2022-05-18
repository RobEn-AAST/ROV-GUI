import cv2
import os
from rovlib.cameras import RovCam

shots=[]
n=1
cap = RovCam.FRONT
print("Cam Loaded...")
# while(True):
#     ret, frame = cap.read()

#     file_name = 'Frame'+str(n)+'.jpg' 
   
#     key = cv2.waitKey(0)
   
#     # if key == 83:
        
#     #     file_name = 'Frame'+str(n)+'.jpg' 
#     #     cv2.imwrite(os.path.join('camera 1', file_name), frame)
#     if (key == ord('q')):
#             break
#     cv2.imshow('window', frame)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        
        file_name = 'Frame'+str(n)+'.jpg' 
        cv2.imwrite(os.path.join('camera 1', file_name), frame)  
        n=n+1  
