# Import required libraries
import cv2
import mediapipe as mp

# Video capture object where 0 is the camera number for a USB camera (or webcam)
# cam = cv2.VideoCapture(0)  # Uncomment this line to use webcam
# For video file, use this:
cam = cv2.VideoCapture(r"C:\Users\rohan\OneDrive\Desktop\Build club\CV_Builder_Series\DH064.mov")

# Frame width and height, will be useful later to find exact pixel locations
# from normalized locations of faces
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Creating a face detector object from Mediapipe solutions
faces = mp.solutions.face_detection.FaceDetection()

while True:
    ret, frame = cam.read()  # Reading one frame from the camera object
    if not ret:  # If frame is not received, break the loop
        print("Error: No frame received.")
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for processing
    faceResults = faces.process(frameRGB)  # This returns list of locations for all the faces in the current frame

    if faceResults.detections:  # If detection is non-empty or if at least one face detected, proceed
        for face in faceResults.detections:  # Iterate through each face location
            bBox = face.location_data.relative_bounding_box  # Collect bounding boxes for each face
            # Splitting into variables and converting to integer for drawing rectangle around detected faces
            x, y, w, h = (
                int(bBox.xmin * width),
                int(bBox.ymin * height),
                int(bBox.width * width),
                int(bBox.height * height),
            )
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around detected faces

    cv2.imshow('Webcam', frame)  # Display the frame with detected faces

    # Waits for 1ms and check for the pressed key
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the camera
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()