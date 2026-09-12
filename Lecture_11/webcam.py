import cv2 as cv


# =========================
# Real-Time Face Detection
# =========================

# Load Haar Cascade
face_cascade = cv.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Open webcam
cap = cv.VideoCapture(0)

while True:

    # Read frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to read from webcam")
        break

    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    # Show result
    cv.imshow("Face Detection", frame)

    # Press ESC to exit
    if cv.waitKey(1) & 0xFF == 27:
        break


# Release webcam
cap.release()
cv.destroyAllWindows()
