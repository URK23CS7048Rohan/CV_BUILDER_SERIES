#Changing Colours


import cv2
# Relative or absolute path of the input image file
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\f90a84272a0eb8729a55816ac563d677.jpg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
# converting image to Grayscale (also OpenCV reads image in BGR format and hence BGR to Gray)

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# Display image in a window
cv2.imshow("Output",image)
cv2.imshow("Output_gray",image_gray)
# Wait until any key press (press any key to close the window)
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()