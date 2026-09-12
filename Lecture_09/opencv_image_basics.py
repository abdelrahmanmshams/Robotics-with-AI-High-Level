import cv2 as cv


# =========================
# OpenCV Image Basics
# =========================

# Load image
image = cv.imread("bird.jpg")

# Check if image was loaded
if image is None:
    print("Image not found!")
else:

    # Convert BGR to RGB
    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Get image dimensions
    height = image.shape[0]
    width = image.shape[1]

    print(f"Height of Image: {height} pixels")
    print(f"Width of Image: {width} pixels")

    # Display original image
    cv.imshow("Image BGR", image)

    # Display RGB image
    cv.imshow("Image RGB", imageRGB)

    # Wait for a key
    cv.waitKey(0)

    # Close all windows
    cv.destroyAllWindows()
