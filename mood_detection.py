import cv2
import numpy as np
import face_recognition

# Function to detect mood based on facial expression
def detect_mood(frame):
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Simulating mood recognition based on a simple threshold
        # Consider a smile if the bottom of the face is less than a threshold
        if face_encoding[0] < 0.4:
            return "smile"
        else:
            return "cry"

# Main program
video_capture = cv2.VideoCapture(0)

# Loop to capture video feed from the camera
while True:
    ret, frame = video_capture.read()

    # Detect the mood using the defined function
    mood = detect_mood(frame)

    # Output the result based on the detected mood
    if mood == "smile":
        print("System unlocked! 😊")
    elif mood == "cry":
        print("System locked. 😢")
    else:
        print("Unable to recognize mood. System remains unlocked! 😊")

    # Display the video frame
    cv2.imshow('Video', frame)

    # Check for key press to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()