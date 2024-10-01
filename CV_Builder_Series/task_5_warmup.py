import cv2
import numpy as np

# Function to replace the green screen background with a new image
def replace_background(frame, background, lower_bound, upper_bound):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create mask for green color in the HSV range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Invert the mask to get the foreground (person)
    mask_inv = cv2.bitwise_not(mask)
    
    # Isolate the foreground
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Resize background to match the frame size
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
    # Isolate the background
    bg = cv2.bitwise_and(background, background, mask=mask)
    
    # Combine the background and foreground
    final = cv2.add(bg, fg)
    
    return final

# Start webcam capture
cap = cv2.VideoCapture(1)

# Load background image
background = cv2.imread(r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\images.jpeg")

# Define the lower and upper bounds for the green color in HSV
lower_bound = np.array([35, 100, 100])
upper_bound = np.array([85, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Replace the green background
    result = replace_background(frame, background, lower_bound, upper_bound)
    
    # Show the output
    cv2.imshow('Original', frame)
    cv2.imshow('Green Screen Replacement', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
