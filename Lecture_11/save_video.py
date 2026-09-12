import cv2 as cv


# =========================
# Save Webcam Video
# =========================

cap = cv.VideoCapture(0)

# Get video properties
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Create video writer
fourcc = cv.VideoWriter_fourcc(*"XVID")

out = cv.VideoWriter(
    "output.avi",
    fourcc,
    20.0,
    (frame_width, frame_height)
)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to read from webcam")
        break

    # Show webcam frame
    cv.imshow("Webcam", frame)

    # Save frame to video
    out.write(frame)

    # Press ESC to stop recording
    if cv.waitKey(1) & 0xFF == 27:
        break


# Release everything
cap.release()
out.release()
cv.destroyAllWindows()

print("Video saved successfully!")
