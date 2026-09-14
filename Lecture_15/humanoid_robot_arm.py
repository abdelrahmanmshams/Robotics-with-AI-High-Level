import cv2 as cv
import mediapipe as mp
from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM9")

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

while True:

    success, img = cap.read()

    if not success:
        print("Camera error")
        break

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append([id, cx, cy])

            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

    if len(lmList) != 0:

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            arduino.sendData([1])
        else:
            arduino.sendData([2])

        # Index finger
        if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]:
            arduino.sendData([3])
        else:
            arduino.sendData([4])

        # Middle finger
        if lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]:
            arduino.sendData([5])
        else:
            arduino.sendData([6])

        # Ring finger
        if lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
            arduino.sendData([7])
        else:
            arduino.sendData([8])

        # Pinky
        if lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]:
            arduino.sendData([9])
        else:
            arduino.sendData([10])

    cv.imshow("Humanoid Robot Arm", img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
