import cv2
import numpy as np

# Variables for RGB channel values (initially 0)
R = 0
G = 0
B = 0

# Callback function for RED slider
def redValue(value):
    global R
    R = value

# Callback function for GREEN slider
def greenValue(value):
    global G
    G = value

# Callback function for BLUE slider
def blueValue(value):
    global B
    B = value

# Creating a black image/frame (0 pixel value) of 500x500 size
frame = np.zeros((500, 500, 3), np.uint8)

# Creating a window for trackbars and frame
cv2.namedWindow('FRAME')
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 500, 130)

# Creating three different trackbars for RGB channels
cv2.createTrackbar('RED', 'Trackbars', R, 255, redValue)
cv2.createTrackbar('GREEN', 'Trackbars', G, 255, greenValue)
cv2.createTrackbar('BLUE', 'Trackbars', B, 255, blueValue)

while True:
    # Update the frame with current RGB values
    frame[:, :, 2] = R  # Red channel
    frame[:, :, 1] = G  # Green channel
    frame[:, :, 0] = B  # Blue channel

    # Display the frame
    cv2.imshow('FRAME', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
