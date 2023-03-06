# 加載所需的庫
# import libraries
import cv2

# 列出庫的版本
# print out the version of libraries
print('cv2 version: ' + cv2.__version__)

# 括號中的數字取決於你所使用的攝像頭
# You may need to change the number inside () to 0 1 or 2, 
# depending on which webcam you are using
cap = cv2.VideoCapture(0)

# 一個用於顯示輸出幀的循環
# A loop for display Output frames
while(True):

    # 從攝像頭中讀取影像。
    # Read frames from the capture. 
    ret, frame = cap.read()


    WinFrame = "WinFrame"

    # 命名視窗 WinFrame
    # name the window WinFrame
    cv2.namedWindow(WinFrame)

    # 移動視窗坐標
    # move the window to (50,20)
    cv2.moveWindow(WinFrame, 50,20)

    # 顯示 Frame 在視窗 WinFrame 中
    # Display Frame in WinFrame
    cv2.imshow(WinFrame, frame)
    
    # 將影像轉換灰階影像
    # Convert images to grayscale
    GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    WinGrayFrame = "WinGrayFrame"

    # 命名視窗 WinGrayFrame
    # name the window WinGrayFrame
    cv2.namedWindow(WinGrayFrame)
    
    # 移動視窗坐標
    # move the window to (700,20)
    cv2.moveWindow(WinGrayFrame, 700,20)

    # 顯示 GrayFrame 在視窗 WinGrayFrame 中
    # Display GrayFrame in WinGrayFrame
    cv2.imshow(WinGrayFrame, GrayFrame)

    # 若關閉視窗則退出迴圈
    # If window is closed, the loop is exited.
    if cv2.waitKey(20) and (cv2.getWindowProperty(WinFrame,cv2.WND_PROP_VISIBLE) < 1 or cv2.getWindowProperty(WinGrayFrame,cv2.WND_PROP_VISIBLE) < 1):        
        break

# 釋放攝像頭資源
# release the capture
cap.release()

# 摧毁所有窗口
# Destroy all the window
cv2.destroyAllWindows()
