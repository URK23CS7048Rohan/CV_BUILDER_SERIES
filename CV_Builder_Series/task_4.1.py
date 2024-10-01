import cv2
import numpy as np

# Global variables shared between the mouseClick function and the rest of the code
draw = False
p1 = (0, 0)  # top left corner point
p2 = p1  # bottom right corner point

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global draw, p1, p2

    # Start drawing when left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (xPos, yPos)
        p2 = p1

    # Update bottom-right corner point as the mouse moves, while the button is pressed
    elif event == cv2.EVENT_MOUSEMOVE and draw:
        p2 = (xPos, yPos)

    # Stop drawing when the left mouse button is released
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False

# Creating a black image/frame (0 pixel value) of 500x500 size
frame = np.zeros((500, 500, 3), np.uint8)

# Creating a window to display the image/frame
cv2.namedWindow('FRAME')

# Set the mouse callback function to trigger the "mouseClick" function on mouse events
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    # Refresh the black frame in every loop (this simulates a video frame update)
    temp_frame = frame.copy()  # Use a temporary frame so the original frame isn't overwritten
    cv2.rectangle(temp_frame, p1, p2, (0, 255, 0), 2)  # Draw rectangle from p1 to p2
    
    # Display the frame
    cv2.imshow('FRAME', temp_frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows when finished
cv2.destroyAllWindows()
