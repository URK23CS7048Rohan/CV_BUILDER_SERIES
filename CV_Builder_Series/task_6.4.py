# Importing OpenCV Library  
import cv2  

# Relative or absolute path of the input image file  
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\9c1318551dbc9159f5bcceb977bd7c94.jpg"  

# reading image (by default the flag is 1 if not specified)  
image = cv2.imread(path)  

edges = cv2.Canny(image, 200, 300)  
# Display image in a window  
cv2.imshow("Output", image)  
cv2.imshow("Edges", edges)  

# Wait until any key press (press any key to close the window)  
cv2.waitKey()  
# kill all the windows  
cv2.destroyAllWindows()