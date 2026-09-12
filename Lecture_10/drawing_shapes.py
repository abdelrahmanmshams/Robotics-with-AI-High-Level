import cv2 as cv
import numpy as np


# =========================
# Drawing Shapes with OpenCV
# =========================

# Create a black image
image = np.zeros((512, 512, 3), np.uint8)


# Draw a line
cv.line(
    image,
    (50, 50),
    (450, 50),
    (255, 0, 0),
    3
)


# Draw a rectangle
cv.rectangle(
    image,
    (50, 100),
    (200, 250),
    (0, 255, 0),
    3
)


# Draw a circle
cv.circle(
    image,
    (350, 175),
    75,
    (0, 0, 255),
    3
)


# Draw a polygon
points = np.array([
    [100, 350],
    [200, 300],
    [300, 350],
    [200, 450]
])

cv.polylines(
    image,
    [points],
    True,
    (255, 255, 0),
    3
)


# Write text
cv.putText(
    image,
    "Robotics",
    (150, 490),
    cv.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv.LINE_AA
)


# Display image
cv.imshow("Drawing Shapes", image)

cv.waitKey(0)
cv.destroyAllWindows()
