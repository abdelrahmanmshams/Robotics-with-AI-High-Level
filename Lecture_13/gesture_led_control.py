import cv2 as cv
import mediapipe as mp
import math
import serial
import time

arduino = serial.Serial("COM8", 9600)
time.sleep(2)

cap = cv.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils


def calculate_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    frame = cv.flip(frame, 1)

    rgb_frame = cv.cvtColor(
        frame,
        cv.COLOR_BGR2RGB
    )

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

            h, w, _ = frame.shape

            x1 = int(thumb_tip.x * w)
            y1 = int(thumb_tip.y * h)

            x2 = int(index_tip.x * w)
            y2 = int(index_tip.y * h)

            cv.line(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 0, 0),
                2
            )

            cv.circle(
                frame,
                (x1, y1),
                5,
                (0, 255, 0),
                -1
            )

            cv.circle(
                frame,
                (x2, y2),
                5,
                (0, 255, 0),
                -1
            )

            distance = calculate_distance(
                x1, y1, x2, y2
            )

            pwm_value = int(
                (distance - 30)
                / (200 - 30)
                * 255
            )

            pwm_value = max(
                0,
                min(255, pwm_value)
            )

            arduino.write(
                f"{pwm_value}\n".encode()
            )

            cv.putText(
                frame,
                f"Distance: {int(distance)}",
                (10, 50),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            cv.putText(
                frame,
                f"PWM: {pwm_value}",
                (10, 90),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

    cv.imshow("Gesture LED Control", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
arduino.close()
cv.destroyAllWindows()
