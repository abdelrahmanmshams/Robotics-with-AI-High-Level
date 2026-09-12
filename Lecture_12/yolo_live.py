from ultralytics import YOLO
import cv2 as cv


# =========================
# YOLO Real-Time Detection
# =========================

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

    # Draw detections
    annotated_frame = results[0].plot()

    # Display result
    cv.imshow("YOLO Live Detection", annotated_frame)

    # Press ESC to exit
    if cv.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv.destroyAllWindows()
