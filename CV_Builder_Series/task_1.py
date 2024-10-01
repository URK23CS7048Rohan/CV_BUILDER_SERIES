import cv2
path = r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\f90a84272a0eb8729a55816ac563d677.jpg"
image = cv2.imread(path)
cv2.imshow("Output",image)
cv2.waitKey()
cv2.destroyAllWindows()