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

# Declare variables
ix,iy,w,h = -1,-1,0,0

# Create a new blank image
shape = (480, 640, 3) # y, x, RGB
OutputFrame = np.zeros(shape, np.uint8)

# Display FrameROI
def getFrameROI(event,x,y,flags,param):
    global ix,iy,w,h,OutputFrame,Frame

    # if left button of mouse is down
    if event == cv2.EVENT_LBUTTONDOWN:
        w,h = 0,0
        ix,iy = x,y

    # if left button of mouse is up
    if event == cv2.EVENT_LBUTTONUP:

        # the weight of rectangle
        w = x - ix

        # the height of rectangle
        h = y - iy

        # get the image inside the rectangle 
        FrameROI = Frame[iy:iy+h, ix:ix+w]

        # Display FrameROI
        cv2.imshow('Frame ROI',FrameROI)

    # if right button of mouse is up
    if event == cv2.EVENT_RBUTTONUP:

        # reset the variables
        ix,iy,w,h = -1,-1,0,0

        # destroy the window 'Frame ROI'
        cv2.destroyWindow('Frame ROI')

# name the window 'Faces Detected'
cv2.namedWindow('Faces Detected')

# add a event listener 
cv2.setMouseCallback('Faces Detected',getFrameROI)

# A loop for display Output frames
while (True):

    # Read frames from the capture.
    Success, Frame = capture.read()

    # Copy the Frame to OutputFrame
    OutputFrame = Frame 

    # draw a rectangle
    cv2.rectangle(OutputFrame, (ix,iy),(ix+w,iy+h),(255,0,0),2)

    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q4    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

    # Display OutputFrame
    cv2.imshow('Faces Detected',OutputFrame)

    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and cv2.getWindowProperty('Faces Detected',cv2.WND_PROP_VISIBLE) < 1:        
        break

# release the capture
capture.release()

# Destroy all the window
cv2.destroyAllWindows()
