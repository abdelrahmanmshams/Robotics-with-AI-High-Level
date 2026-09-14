import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import serial

bluetooth = serial.Serial("COM11", 9600)
bluetooth.flushInput()

cap = cv.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:

    success, img = cap.read()

    if not success:
        print("Camera error")
        break

    hands, img = detector.findHands(img)

    if len(hands) == 2:

        hand1 = hands[0]
        hand2 = hands[1]

        centerPoint1 = hand1["center"]
        centerPoint2 = hand2["center"]

        length, info, img = detector.findDistance(
            centerPoint1,
            centerPoint2,
            img
        )

        cv.circle(
            img,
            (info[4], info[5]),
            int(length) // 2,
            (100, 100, 30),
            5
        )

        leftY = centerPoint1[1]
        rightY = centerPoint2[1]

        if abs(leftY - rightY) <= 30:

            cv.putText(
                img,
                "Move Forward",
                (50, 50),
                cv.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                4
            )

            bluetooth.write(b"F")

        elif leftY > rightY + 30:

            cv.putText(
                img,
                "Move Left",
                (50, 50),
                cv.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                4
            )

            bluetooth.write(b"R")

        elif rightY > leftY + 30:

            cv.putText(
                img,
                "Move Right",
                (50, 50),
                cv.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                4
            )

            bluetooth.write(b"L")

        else:

            cv.putText(
                img,
                "Stop",
                (50, 50),
                cv.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                4
            )

            bluetooth.write(b"S")

    else:

        cv.putText(
            img,
            "Stop",
            (50, 50),
            cv.FONT_HERSHEY_PLAIN,
            2,
            (0, 0, 255),
            4
        )

        bluetooth.write(b"S")

    cv.imshow("Virtual Steering Wheel", img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
bluetooth.close()
cv.destroyAllWindows()
