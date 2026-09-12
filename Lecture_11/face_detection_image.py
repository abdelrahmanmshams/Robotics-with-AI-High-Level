import cv2 as cv


# =========================
# Face Detection using Haar Cascade
# =========================

# Load image
image = cv.imread("person.jpg")

if image is None:
    print("Image not found!")

else:

    # Load Haar Cascade classifier
    face_cascade = cv.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    # Convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Number of faces detected:", len(faces))

    # Draw rectangle around each face
    for (x, y, w, h) in faces:
        cv.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    # Display result
    cv.imshow("Face Detection", image)

    cv.waitKey(0)
    cv.destroyAllWindows()
