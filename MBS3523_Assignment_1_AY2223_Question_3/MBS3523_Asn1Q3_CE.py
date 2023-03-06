# 加載所需的庫
# import libraries
import cv2
import numpy as np
import math 

# 列出庫的版本
# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# 載入檢測面部所需的 xml檔
# Load the required xml file to detect frontal face
eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')
mouthCascade = cv2.CascadeClassifier("Resources/haarcascade_mcs_mouth.xml")
faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# 括號中的數字取決於你所使用的攝像頭
# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# 設定攝像頭視窗大小
# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame

# 宣告變數用於計算正方框坐標
# Declare variables for the calculation of positive box coordinates
mx, my, mw, mh, ex, ey, ew, eh = 0,0,0,0,0,0,0,0

# 宣告變數用於儲存上一次所得的值
# Declare variable to the last obtained value.
mx1, my1, mw1, mh1, ex1, ey1, ew1, eh1 = 0,0,0,0,0,0,0,0

# 一個用於顯示輸出幀的循環
# A loop for display Output frames
while (True):

    # 從攝像頭中讀取影像。
    # Read frames from the capture. 
    Success, Frame = capture.read()

    # 將攝像頭中讀取的影像寫入至圖像OutputFrame
    # Copy the Frame to OutputFrame
    OutputFrame = Frame

    # 將影像轉換灰階影像
    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    # 定位人臉的特徵，並返回4個值：檢測到的人臉的x、y、寬度和高度。
    # Locate the features in the face(s) and return 4 values: x, y, width and height of the detected faces
    faces = faceCascade.detectMultiScale(GrayFrame, 1.03, 5)

    # 檢測面部中眼睛和嘴巴
    # detect eyes and mouths
    mouths = mouthCascade.detectMultiScale(GrayFrame)
    eyes = eyeCascade.detectMultiScale(GrayFrame)

    # 若檢測到面部中眼睛和嘴巴
    # if the detection is success
    if (len(mouths) != 0 and len(eyes) != 0):

        # 儲存資料到變數
        # Save the details into variables
        (mx1, my1, mw1, mh1) = mouths[0]
        (ex1, ey1, ew1, eh1) = eyes[0]

        # 若檢測到面部中眼睛為左眼
        # If the detected eye in the face is the left eye
        if (mx1 > ex1 and my1 > ey1):

            # 儲存資料到變數並用於下列計算
            # Save the details into variables and use they to calculation
            (mx, my, mw, mh) = mouths[0]
            (ex, ey, ew, eh) = eyes[0]

    # 計算並顯示圖形
    # Calculate and display graphs
    cv2.arrowedLine(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (ex,ey), (255, 0, 0), 2 )
    cv2.line(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (mx,(my+mh)), (255, 0, 0), 2)
    cv2.rectangle(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))-40) , (my+mh-40) ), ( int(ex-((my+mh-ey)/math.sqrt(3))+40), (my+mh+40)), (255, 0, 0), 2)
    cv2.ellipse(OutputFrame,( int(ex-((my+mh-ey)/math.sqrt(3))) , (my+mh) ), (70,70), 0, -60, 0,(255, 0, 0), 2)
    cv2.putText(OutputFrame, '60', ( int(ex-((my+mh-ey)/math.sqrt(3)))+70 , (my+mh-50) ), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1,cv2.LINE_AA,False)
    
    # 在圖像OutputFrame的頂部寫上課程編號和姓名
    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q3    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

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
