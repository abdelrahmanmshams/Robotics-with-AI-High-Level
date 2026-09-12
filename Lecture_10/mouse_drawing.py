import cv2 as cv
import numpy as np


# =========================
# Drawing with Mouse
# =========================

is_drawing = False
ix = -1
iy = -1

# Create blank image
blank_image = np.zeros((512, 512, 3), dtype=np.uint8)


def draw_rectangle(event, x, y, flags, param):
    global is_drawing, ix, iy

    # Mouse button pressed
    if event == cv.EVENT_LBUTTONDOWN:
        is_drawing = True
        ix = x
        iy = y

    # Mouse button released
    elif event == cv.EVENT_LBUTTONUP:
        is_drawing = False

        cv.rectangle(
            blank_image,
            (ix, iy),
            (x, y),
            (255, 0, 0),
            -1
        )

        ix = -1
        iy = -1

    # Mouse movement
    elif event == cv.EVENT_MOUSEMOVE:
        if is_drawing:
            cv.rectangle(
                blank_image,
                (ix, iy),
                (x, y),
                (255, 0, 0),
                -1
            )


# Create window
cv.namedWindow("Mouse Drawing")

# Set mouse callback
cv.setMouseCallback("Mouse Drawing", draw_rectangle)


while True:

    cv.imshow("Mouse Drawing", blank_image)

    # Press ESC to exit
    if cv.waitKey(5) & 0xFF == 27:
        cv.imwrite("Mouse_Drawing.jpg", blank_image)
        break


cv.destroyAllWindows()
