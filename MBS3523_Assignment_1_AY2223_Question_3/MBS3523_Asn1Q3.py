# import libraries
import cv2
import numpy as np
import math 

# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# Load the required xml file to detect frontal face
eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')
mouthCascade = cv2.CascadeClassifier("Resources/haarcascade_mcs_mouth.xml")

# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame

# Declare variables for the calculation of positive box coordinates
mx, my, mw, mh, ex, ey, ew, eh = 0,0,0,0,0,0,0,0

# Declare variable to the last obtained value.
mx1, my1, mw1, mh1, ex1, ey1, ew1, eh1 = 0,0,0,0,0,0,0,0

# A loop for display Output frames
while (True):
    
    # Read frames from the capture. 
    Success, Frame = capture.read()

    # Copy the Frame to OutputFrame
    OutputFrame = Frame

    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    # detect eyes and mouths
    mouths = mouthCascade.detectMultiScale(GrayFrame)
    eyes = eyeCascade.detectMultiScale(GrayFrame)

    # if the detection is success
    if (len(mouths) != 0 and len(eyes) != 0):

        # Save the details into variables
        (mx1, my1, mw1, mh1) = mouths[0]
        (ex1, ey1, ew1, eh1) = eyes[0]

        # If the detected eye in the face is the left eye
        if (mx1 > ex1 and my1 > ey1):

            # Save the details into variables and use they to calculation
            (mx, my, mw, mh) = mouths[0]
            (ex, ey, ew, eh) = eyes[0]

    # Calculate and display graphs
    cv2.arrowedLine(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (ex,ey), (255, 0, 0), 2 )
    cv2.line(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (mx,(my+mh)), (255, 0, 0), 2)
    cv2.rectangle(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))-40) , (my+mh-40) ), ( int(ex-((my+mh-ey)/math.sqrt(3))+40), (my+mh+40)), (255, 0, 0), 2)
    cv2.ellipse(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (70,70), 0, -60, 0,(255, 0, 0), 2)
    cv2.putText(OutputFrame, '60', ( int(ex-((my+mh-ey)/math.sqrt(3)))+70 , (my+mh-50) ), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1,cv2.LINE_AA,False)
    
    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q3    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

    # Display OutputFrame
    cv2.imshow('Faces Detected',OutputFrame)

    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and cv2.getWindowProperty('Faces Detected',cv2.WND_PROP_VISIBLE) < 1:        
        break

# release the capture
capture.release()

# Destroy all the window
cv2.destroyAllWindows()