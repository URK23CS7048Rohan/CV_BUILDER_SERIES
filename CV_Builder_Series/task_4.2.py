import cv2
import numpy as np

# Global variables shared between the mouseClick function and the rest of the code
draw = False
reset = False
p1 = (0, 0)  # First point of the line segment
p2 = p1  # Second point of the line segment

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global draw, reset, p1, p2
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        reset = False
        p1 = (xPos, yPos)
        p2 = p1
    elif event == cv2.EVENT_MOUSEMOVE and draw:
        p2 = (xPos, yPos)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
    elif event == cv2.EVENT_RBUTTONDOWN:
        reset = True
        p1 = (0, 0)
        p2 = p1

# Creating a black image/frame (0 pixel value) of 500x500 size
frame = np.zeros((500, 500, 3), np.uint8)

# Creating a window to display image/frame
cv2.namedWindow('FRAME')

# This function detects every new event and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    # Draw the line on the frame
    if p1 != p2:
        cv2.line(frame, p1, p2, (0, 255, 0), 2)
    
    # Update p1 to p2 for next line segment
    p1 = p2
    
    # Show the frame
    cv2.imshow('FRAME', frame)
    
    # Reset the frame if right-clicked
    if reset:
        frame = np.zeros((500, 500, 3), np.uint8)
        reset = False
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
