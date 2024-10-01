import cv2
import numpy as np

# Initialize a list to hold corner points
pts = []

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global pts  # Use the global variable to append points

    # Left click press event
    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (xPos, yPos)
        print(p1)  # Print the clicked point
        pts.append(p1)  # Collecting corner points

# Reading image
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\9c1318551dbc9159f5bcceb977bd7c94.jpg" 
frame = cv2.imread(path)

# Check if the image was loaded successfully
if frame is None:
    print("Error: Could not read the image.")
    exit()

# Creating a window to display the image/frame
cv2.namedWindow('FRAME')

# This function detects every new event and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    cv2.imshow('FRAME', frame)

    # Check if we have enough points to perform the transformation
    if len(pts) >= 4:
        pts_src = np.float32(pts[:4])  # Take the first four points
        pts_dst = np.float32([[0, 0], [200, 0], [200, 400], [0, 400]])  # Destination points
        matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)  # Get the transformation matrix
        warped = cv2.warpPerspective(frame, matrix, (200, 400))  # Apply the perspective warp
        cv2.imshow('Warped', warped)  # Display the warped image

    # Wait for a key press; to quit press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()