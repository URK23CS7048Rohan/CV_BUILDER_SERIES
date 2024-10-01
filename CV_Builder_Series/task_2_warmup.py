import cv2
import numpy as np
import time

def create_checkerboard(size):
    """Create a 4x4 checkerboard of the given size."""
    block_size = size // 4
    checkerboard = np.zeros((size, size), dtype=np.uint8)

    for i in range(4):
        for j in range(4):
            # Fill the blocks alternating between black and white
            if (i + j) % 2 == 0:
                checkerboard[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size] = 255
    
    return checkerboard

# Create a 4x4 checkerboard where each block is 100x100 pixels (total 400x400)
checkerboard = create_checkerboard(400)

while True:
    # Show the normal checkerboard
    cv2.imshow("Checkerboard", checkerboard)
    
    # Wait for 1 second
    cv2.waitKey(1000)

    # Invert the checkerboard colors
    inverted_checkerboard = cv2.bitwise_not(checkerboard)

    # Show the inverted checkerboard
    cv2.imshow("Checkerboard", inverted_checkerboard)

    # Wait for 1 second
    cv2.waitKey(1000)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()
