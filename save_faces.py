import cv2
import os
# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a video capture object
video_capture = cv2.VideoCapture(0)
new_dir = ''
# Start capturing the video feed
i = 203
j = 0
main_path = "C:/Users/Admin/Desktop/Detection-systems/CNN_DAAT/Train/Satwik/"

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    # Convert the frame to grayscale
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

     # Detect faces in the frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(0, 40))
    # Draw bounding boxes on the frame and save face regions
    for (x, y, w, h) in faces:
        # Draw the bounding box on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Save only the face region
        face = frame[y:y+h, x:x+w]
        
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(f"{main_path}paras{str(i)}.jpg", face)
            print(i)
            i+=1
    
    if cv2.waitKey(1) == ord('q'):
        break
        
    # Display the frame with bounding boxes
    cv2.imshow("Face Detection", frame)
    # cv2.imshow("Face Detection5", face)qq
    
# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()
