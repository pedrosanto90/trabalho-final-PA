from cv2 import *

cam_port = 0
cam = VideoCapture(cam_port) 

result, image = cam.read() 

if result: 

    imshow("GeeksForGeeks", image) 

    imwrite("GeeksForGeeks.png", image) 

    waitKey(0) 
    destroyWindow("GeeksForGeeks") 

else: 
    print("No image detected. Please! try again")
