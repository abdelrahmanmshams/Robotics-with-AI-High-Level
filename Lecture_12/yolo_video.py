from ultralytics import YOLO
import cv2 as cv


# =========================
# YOLO Object Detection
# Recorded Video
# =========================

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load video
cap = cv.VideoCapture("input.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Display video
    cv.imshow("YOLO Video Detection", annotated_frame)

    # Press ESC to exit
    if cv.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv.destroyAllWindows()
