import cv2
import numpy as np

# Paths to the images
path1 = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\5ad30b721ae28a6748be82130f9828ec.jpg"
path2 = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\9c1318551dbc9159f5bcceb977bd7c94.jpg"

# Read the two images
image1 = cv2.imread(path1)
image2 = cv2.imread(path2)

# Check if both images are loaded successfully
if image1 is None or image2 is None:
    print("Error: One or both images could not be loaded.")
else:
    # Resize the images to ensure they have the same height
    height = min(image1.shape[0], image2.shape[0])  # Minimum height of the two images
    width1 = int(image1.shape[1] * height / image1.shape[0])  # Adjust width proportionally
    width2 = int(image2.shape[1] * height / image2.shape[0])  # Adjust width proportionally
    image1_resized = cv2.resize(image1, (width1, height))
    image2_resized = cv2.resize(image2, (width2, height))

    # Concatenate the two images side by side (horizontally)
    concatenated_color = np.hstack((image1_resized, image2_resized))

    # Convert the concatenated image to grayscale
    concatenated_gray = cv2.cvtColor(concatenated_color, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale image to 3 channels to match the color images
    concatenated_gray_3channel = cv2.cvtColor(concatenated_gray, cv2.COLOR_GRAY2BGR)

    # Stack the color images on top and the grayscale images on the bottom
    final_image = np.vstack((concatenated_color, concatenated_gray_3channel))

    # Save the final image
    cv2.imwrite('A1_solution.jpg', final_image)

    # Display the final image (optional)
    cv2.imshow("Final Image", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
