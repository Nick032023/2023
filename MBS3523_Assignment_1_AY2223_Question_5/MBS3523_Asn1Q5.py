# import libraries
import cv2
import numpy as np

# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame

def nil(x):
    pass

# name the window 'Frame'
cv2.namedWindow('Frame')

# Create track bars
cv2.createTrackbar('X-POS','Frame',100,480,nil)
cv2.createTrackbar('Y-POS','Frame',100,480,nil)

# A loop for display Output frames
while (True):

    # Read frames from the capture.
    Success, Frame = capture.read()

    # Copy the Frame to OutputFrame
    OutputFrame = Frame

    # get the values of x and y
    x = cv2.getTrackbarPos('X-POS','Frame')
    y = cv2.getTrackbarPos('Y-POS','Frame')

    # draw two lines in image OutputFrame
    cv2.line(OutputFrame,(0,y),(640,y),(0,255,0),3)
    cv2.line(OutputFrame,(x,0),(x,480),(0,255,0),3)

    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q5    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

    # Display OutputFrame
    cv2.imshow('Frame',OutputFrame)

    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and cv2.getWindowProperty('Frame',cv2.WND_PROP_VISIBLE) < 1:        
        break

# release the capture
capture.release()

# Destroy all the window
cv2.destroyAllWindows()