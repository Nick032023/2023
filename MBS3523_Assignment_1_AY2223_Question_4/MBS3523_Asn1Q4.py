# import libraries
import cv2
import numpy as np

# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# Load the required xml file to detect frontal face
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame
    
# A loop for display Output frames
while (True):

    # Read frames from the capture.
    Success, Frame = capture.read()

    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale images to color images
    OutputFrame = cv2.cvtColor(GrayFrame, cv2.COLOR_RGB2BGR)

    # Locate the features in the face(s) and return 4 values: x, y, width and height of the detected faces
    faces = faceCascade.detectMultiScale(GrayFrame, 1.03, 5)

    for (x,y,w,h) in faces:

        # In the area where the face is detected, the original image is copied to the outputFrame.
        OutputFrame[y:y+h, x:x+w] = Frame[y:y+h, x:x+w]

        # Add a long box to frame the detected facial area
        OutputFrame = cv2.rectangle(OutputFrame, (x,y),(x+w,y+h),(255,0,0),2)

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