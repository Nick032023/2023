# 加載所需的庫
# import libraries
import cv2
import numpy as np

# 列出庫的版本
# print out the version of libraries
print("cv2 version: "+ cv2.__version__)

# 括號中的數字取決於你所使用的攝像頭
# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
capture = cv2.VideoCapture(0)

# 設定攝像頭視窗大小
# Below 2 lines are used to set the webcam window size 
capture.set(3,640) # 3 is the width of the Frame 
capture.set(4,480) # 4 is the height of the Frame

# 建立全黑的新圖片
shape = (480, 640, 3) # y, x, RGB
OutputFrame = np.zeros(shape, np.uint8)

def nil(x):
    pass

# 命名視窗 'Frame'
# name the window 'Frame'
cv2.namedWindow('Frame')

# 創建滑動條
# Create track bars
cv2.createTrackbar('X-POS','Frame',100,480,nil)
cv2.createTrackbar('Y-POS','Frame',100,480,nil)

# 一個用於顯示輸出幀的循環
# A loop for display Output frames
while (True):

    # 從攝像頭中讀取影像。
    # Read frames from the capture.
    Success, Frame = capture.read()

    # 將攝像頭中讀取的影像寫入至圖像OutputFrame
    # Copy the Frame to OutputFrame
    OutputFrame = Frame

    # 取得 x 和 y 的值
    # get the values of x and y
    x = cv2.getTrackbarPos('X-POS','Frame')
    y = cv2.getTrackbarPos('Y-POS','Frame')

    # 在 OutputFrame 上繪製線條
    # draw two lines in image OutputFrame
    cv2.line(OutputFrame,(0,y),(640,y),(0,255,0),3)
    cv2.line(OutputFrame,(x,0),(x,480),(0,255,0),3)

    # 在圖像OutputFrame的頂部寫上課程編號和姓名
    # Write the course number and name at the top of OutputFrame.
    cv2.putText(OutputFrame, 'MBS3523 Assignment 1 - Q5    Name: Cheung Yuk Yeung 220118756', (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,cv2.LINE_AA,False)

    # 顯示 OutputFrame
    # Display OutputFrame
    cv2.imshow('Frame',OutputFrame)

    # 若關閉視窗則退出迴圈
    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and cv2.getWindowProperty('Frame',cv2.WND_PROP_VISIBLE) < 1:        
        break

# 釋放攝像頭資源
# release the capture
capture.release()

# 摧毁所有窗口
# Destroy all the window
cv2.destroyAllWindows()
