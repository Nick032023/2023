# import libraries
import cv2

# print out the version of libraries
print('cv2 version: ' + cv2.__version__)

# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
cap = cv2.VideoCapture(0)

# A loop for display Output frames
while(True):

    # Read frames from the capture. 
    ret, frame = cap.read()

    WinFrame = "WinFrame"

    # name the window WinFrame
    cv2.namedWindow(WinFrame)

    # move the window to (50,20)
    cv2.moveWindow(WinFrame, 50,20)

    # Display Frame in WinFrame
    cv2.imshow(WinFrame, frame)
    
    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    WinGrayFrame = "WinGrayFrame"

    # name the window WinGrayFrame
    cv2.namedWindow(WinGrayFrame)
    
    # move the window to (700,20)
    cv2.moveWindow(WinGrayFrame, 700,20)

    # Display GrayFrame in WinGrayFrame
    cv2.imshow(WinGrayFrame, GrayFrame)

    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and (cv2.getWindowProperty(WinFrame,cv2.WND_PROP_VISIBLE) < 1 or cv2.getWindowProperty(WinGrayFrame,cv2.WND_PROP_VISIBLE) < 1):        
        break

# release the capture
cap.release()

# Destroy all the window
cv2.destroyAllWindows()