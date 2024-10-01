# Importing OpenCV Library
import cv2

# Relative or absolute path of the input image file
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\5ad30b721ae28a6748be82130f9828ec.jpg"

# Reading the image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not read the image.")
else:
    # Get the dimensions of the image
    height, width = image.shape[:2]  # shape returns (height, width, channels)

    # Resize the image to half its original size
    image_resize = cv2.resize(image, (width // 2, height // 2))

    # Display the original image in a window
    cv2.imshow("Output", image)

    # Display the resized image in a window
    cv2.imshow("Resize", image_resize)

    # Wait until any key press (press any key to close the window)
    cv2.waitKey(0)

    # Kill all the windows
    cv2.destroyAllWindows()