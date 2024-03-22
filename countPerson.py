import cv2
import numpy as np

video = cv2.VideoCapture('elevator.mp4')
counter = 0
released = False

while True:
    ret,img = video.read()
    img = cv2.resize(img,(1100,720),)
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    x,y,w,h = 490,230,30,150
    imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)
    kernel = np.ones((8,8), np.uint8)
    imgDil = cv2.dilate(imgTh,kernel,iterations=2)

    cutout = imgDil[y:y+h,x:x+w]
    white = cv2.countNonZero(cutout)

    if white > 4000 and released == True:
        counter +=1
    if white < 4000:
        released = True
    else:
        released =False

    if released == False:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    else:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 255),4)

    cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 6)

    cv2.putText(img,str(white),(x-30,y-50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
    cv2.rectangle(img, (575,155), (575 + 88, 155 + 85), (255, 255, 255), -1)
    cv2.putText(img, str(counter), (x+100, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

    #print(counter)
    cv2.imshow('joevohan261_openCV',img)
    #cv2.imshow('video', cv2.resize(imgTh,(600,500)))
    cv2.waitKey(20)