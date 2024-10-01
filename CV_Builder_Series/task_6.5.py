# Importing OpenCV Library  
import cv2  

# Relative or absolute path of the input image file  
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\9c1318551dbc9159f5bcceb977bd7c94.jpg" 

# reading image (by default the flag is 1 if not specified)  
image = cv2.imread(path)  

edges = cv2.Canny(image, 200, 300)  

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
contoured = image.copy()  
cv2.drawContours(contoured, contours, -1, (0, 255, 0), 3)  

# Display image in a window  
cv2.imshow("Output", image)  
cv2.imshow("Edges", contoured)  

# Wait until any key press (press any key to close the window)  
cv2.waitKey()  
# kill all the windows  
cv2.destroyAllWindows()