# 加載所需的庫
# import libraries
import cv2
import numpy as np

# 列出庫的版本
# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# 載入檢測面部所需的 xml檔
# Load the required xml file to detect frontal face
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# 括號中的數字取決於你所使用的攝像頭
# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# 設定攝像頭視窗大小
# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame
    
# 一個用於顯示輸出幀的循環
# A loop for display Output frames
while (True):

    # 從攝像頭中讀取影像。
    # Read frames from the capture.
    Success, Frame = capture.read()

    # 將影像轉換灰階影像
    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    # 將灰階影像轉換成彩色影像的格式並寫入至圖像OutputFrame
    # Convert grayscale images to color images
    OutputFrame = cv2.cvtColor(GrayFrame, cv2.COLOR_RGB2BGR)

    # 定位人臉的特徵，並返回4個值：檢測到的人臉的x、y、寬度和高度。
    # Locate the features in the face(s) and return 4 values: x, y, width and height of the detected faces
    faces = faceCascade.detectMultiScale(GrayFrame, 1.03, 5)

    for (x,y,w,h) in faces:

        # 在檢測到人臉的區域中,將原始圖像複製到圖像OutputFrame中。
        # In the area where the face is detected, the original image is copied to the outputFrame.
        OutputFrame[y:y+h, x:x+w] = Frame[y:y+h, x:x+w]

        # 加入長方框來框起檢測到人臉的區域
        # Add a long box to frame the detected facial area
        OutputFrame = cv2.rectangle(OutputFrame, (x,y),(x+w,y+h),(255,0,0),2)

    # 在圖像OutputFrame的頂部寫上課程編號和姓名
    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q4    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

    # 顯示 OutputFrame
    # Display OutputFrame
    cv2.imshow('Faces Detected',OutputFrame)

    # 若關閉視窗則退出迴圈
    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and cv2.getWindowProperty('Faces Detected',cv2.WND_PROP_VISIBLE) < 1:        
        break

# 釋放攝像頭資源
# release the capture
capture.release()

# 摧毁所有窗口
# Destroy all the window
cv2.destroyAllWindows()
