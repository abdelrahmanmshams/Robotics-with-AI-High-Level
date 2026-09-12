import cv2 as cv


# =========================
# Drawing on Video
# =========================

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to read from webcam")
        break

    # Draw a rectangle
    cv.rectangle(
        frame,
        (100, 100),
        (500, 400),
        (255, 0, 0),
        2
    )

    # Add text
    cv.putText(
        frame,
        "Live Video",
        (120, 80),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv.LINE_AA
    )

    # Show video
    cv.imshow("Drawing on Video", frame)

    # Press ESC to exit
    if cv.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv.destroyAllWindows()
