import cv2 as cv
import mediapipe as mp

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

            fingerState = []

            for id in range(1, 5):

                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingerState.append(1)
                else:
                    fingerState.append(0)

            fingers = fingerState.count(1)

            cv.rectangle(
                img,
                (0, 0),
                (120, 120),
                (0, 0, 0),
                -1
            )

            cv.putText(
                img,
                str(fingers),
                (20, 100),
                cv.FONT_HERSHEY_COMPLEX,
                4,
                (255, 0, 0),
                5
            )

    cv.imshow("Hand Tracking", img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
