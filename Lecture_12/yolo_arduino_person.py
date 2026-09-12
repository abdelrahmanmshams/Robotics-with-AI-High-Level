from ultralytics import YOLO
import cv2 as cv
import serial
import time


# =========================
# YOLO + Arduino
# Person Detection
# =========================

# Connect Arduino
arduino = serial.Serial("COM9", 9600)
time.sleep(2)

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to read from webcam")
        break

    # Run YOLO detection
    results = model(frame)

    # Get detected objects
    objects = results[0].boxes.cls.tolist()

    # Check if person is detected
    if 0 in objects:
        arduino.write(b"1")
    else:
        arduino.write(b"0")

    # Draw detections
    annotated_frame = results[0].plot()

    # Display result
    cv.imshow("YOLO + Arduino", annotated_frame)

    # Press ESC to exit
    if cv.waitKey(1) & 0xFF == 27:
        break


# Close everything
cap.release()
arduino.close()
cv.destroyAllWindows()
