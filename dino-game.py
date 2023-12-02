#program for hand detection and automate chrome dino game with it
#dependencies :
#cv2 - an openCV library used for open source projects
#mediapipe - google's hand detection algorithms and models
#pyautogui - To automate system

#importing modules
import cv2
import time
import mediapipe as mp
import pyautogui as pag

#set window measurements
wCam, hCam = 640, 680
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

#detect hand and draw coordinates
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
fingerCordinates = [(8,6), (12,10), (16,14), (20,18)]
thumbCordinates = (4,2)

#main while loop
while True:
    success, img = cap.read()                              #capturing video from webcam
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)        #converting colors (optional)
    results = hands.process(img)
    multiLandMarks = results.multi_hand_landmarks          #detetct any hand in the video and stores it in result var. multiLandMarks shows the coordinates
    # print(multiLandMarks)

    if multiLandMarks:
        handPoints = []                                    #Array to store Hand coordinates according to mediapipe model
        for handLms in multiLandMarks:                     #iterating through first coordinates
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):    #iterating through finger coordinates
                # print(idx,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)      #converting coordinates into pixel
                handPoints.append((cx, cy))

        #draw circle on track points
        #for point in handPoints:
            # print(point)
            #cv2.circle(img, point, 10, (0,0,255), cv2.FILLED)

        #check if hand is open or closed
        upCount = 0
        for coordinate in fingerCordinates:

            if handPoints[coordinate[0]][1] < handPoints[coordinate[1]][1]:
                upCount += 1
                pag.keyUp('SPACE')
                # print("Hand open")
            else:
                pag.keyDown('SPACE')
                # print("Hand Closed")



    #video displaying
    cv2.imshow("image",img)
    cv2.setWindowProperty("image", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)
