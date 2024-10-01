import cv2
import numpy as np

# Function to apply filters, zoom, rotate, blur, and sketch effect
def apply_changes():
    global image, zoom_level, rotate_angle, blur_value, sketch_value, filter_choice
    
    modified_image = image.copy()

    # Apply zoom
    if zoom_level > 0:
        modified_image = cv2.resize(modified_image, None, fx=zoom_level, fy=zoom_level, interpolation=cv2.INTER_LINEAR)

    # Apply rotation
    rows, cols = modified_image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotate_angle, 1)
    modified_image = cv2.warpAffine(modified_image, M, (cols, rows))

    # Apply blur
    if blur_value > 0:
        modified_image = cv2.GaussianBlur(modified_image, (blur_value * 2 + 1, blur_value * 2 + 1), 0)
    
    # Apply sketch (edge detection)
    if sketch_value > 0:
        gray = cv2.cvtColor(modified_image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        modified_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # Apply filter
    if filter_choice == 1:
        modified_image = cv2.applyColorMap(modified_image, cv2.COLORMAP_JET)
    elif filter_choice == 2:
        modified_image = cv2.applyColorMap(modified_image, cv2.COLORMAP_HOT)
    elif filter_choice == 3:
        modified_image = cv2.applyColorMap(modified_image, cv2.COLORMAP_COOL)
    
    # Display the modified image
    cv2.imshow("Photo Editor", modified_image)

# Function to save the cropped image
def save_cropped_image():
    global x_start, y_start, x_end, y_end, image

    if x_start and y_start and x_end and y_end:
        cropped_image = image[y_start:y_end, x_start:x_end]
        cv2.imwrite('cropped_image.jpg', cropped_image)
        print("Cropped image saved as 'cropped_image.jpg'")

# Callback functions for trackbars
def update_zoom(val):
    global zoom_level
    zoom_level = val / 10.0
    apply_changes()

def update_rotate(val):
    global rotate_angle
    rotate_angle = val
    apply_changes()

def update_blur(val):
    global blur_value
    blur_value = val
    apply_changes()

def update_sketch(val):
    global sketch_value
    sketch_value = val
    apply_changes()

def update_filter(val):
    global filter_choice
    filter_choice = val
    apply_changes()

# Mouse callback function for cropping
def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            x_end, y_end = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False
        save_cropped_image()

# Initialize global variables
image = cv2.imread(r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\5ad30b721ae28a6748be82130f9828ec.jpg"  )
zoom_level = 1.0
rotate_angle = 0
blur_value = 0
sketch_value = 0
filter_choice = 0
x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False

# Create a window and trackbars
cv2.namedWindow("Photo Editor")
cv2.createTrackbar("Zoom", "Photo Editor", 10, 20, update_zoom)
cv2.createTrackbar("Rotate", "Photo Editor", 0, 360, update_rotate)
cv2.createTrackbar("Blur", "Photo Editor", 0, 10, update_blur)
cv2.createTrackbar("Sketch", "Photo Editor", 0, 1, update_sketch)
cv2.createTrackbar("Filter", "Photo Editor", 0, 3, update_filter)

# Set the mouse callback function for cropping
cv2.setMouseCallback("Photo Editor", mouse_crop)

# Display the image
apply_changes()

# Wait for user interaction
cv2.waitKey(0)
cv2.destroyAllWindows()
