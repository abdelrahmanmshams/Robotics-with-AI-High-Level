from ultralytics import YOLO
import cv2 as cv


# =========================
# YOLO Object Detection
# =========================

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load image
image = cv.imread("image.jpg")

if image is None:
    print("Image not found!")

else:

    # Run object detection
    results = model(image)

    # Draw detections
    annotated_image = results[0].plot()

    # Display result
    cv.imshow("YOLO Object Detection", annotated_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
