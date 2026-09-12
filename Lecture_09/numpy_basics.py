import numpy as np
import cv2 as cv


# =========================
# NumPy Basics
# =========================

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)


numbers = np.arange(1, 10, 2)

print("\nArange:")
print(numbers)


p = np.random.randint(0, 100, 10)

print("\nRandom numbers:")
print(p)


minimum = p.min()
print("\nMinimum:")
print(minimum)


maximum = p.max()
print("\nMaximum:")
print(maximum)


min_index = p.argmin()
print("\nIndex of minimum:")
print(min_index)


max_index = p.argmax()
print("\nIndex of maximum:")
print(max_index)


# =========================
# OpenCV Image Basics
# =========================

image = cv.imread("bird.jpg")

if image is None:
    print("\nImage not found!")
else:

    # Convert BGR to RGB
    imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Image dimensions
    height = image.shape[0]
    width = image.shape[1]

    print("\nImage Information:")
    print(f"Height of Image: {height} pixels")
    print(f"Width of Image: {width} pixels")

    cv.imshow("Image BGR", image)
    cv.imshow("Image RGB", imageRGB)

    cv.waitKey(0)
    cv.destroyAllWindows()
