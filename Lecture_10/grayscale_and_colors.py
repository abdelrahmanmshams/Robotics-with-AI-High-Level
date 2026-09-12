import cv2 as cv
import numpy as np


# =========================
# Grayscale & Color Spaces
# =========================

# Load image
image = cv.imread("bird.jpg")

if image is None:
    print("Image not found!")

else:

    # Convert BGR to Grayscale
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Convert BGR to RGB
    RGB_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Convert BGR to HSV
    HSV_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Display images
    cv.imshow("Original Image", image)
    cv.imshow("Gray Image", gray_image)
    cv.imshow("RGB Image", RGB_image)
    cv.imshow("HSV Image", HSV_image)

    # Wait for a key
    cv.waitKey(0)

    # Close all windows
    cv.destroyAllWindows()
