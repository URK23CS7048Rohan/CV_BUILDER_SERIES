# Importing OpenCV Library  
import cv2  

# Relative or absolute path of the input image file  
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\9c1318551dbc9159f5bcceb977bd7c94.jpg"  

# reading image (by default the flag is 1 if not specified)  
image = cv2.imread(path)  

median = image.copy()  
gaussian = image.copy()  

median = cv2.medianBlur(median, 7)  
gaussian = cv2.GaussianBlur(gaussian, (7, 7), cv2.BORDER_DEFAULT)  

# Display image in a window  
cv2.imshow("Original", image)  
cv2.imshow("Median Blur", median)  
cv2.imshow("Gaussian Blur", gaussian)  

# Wait until any key press (press any key to close the window)  
cv2.waitKey()  
# kill all the windows  
cv2.destroyAllWindows()