# Import necessary libraries
import cv2
import mediapipe as mp

# Initialize Mediapipe Face Mesh and Drawing utilities
mp_face_mesh = mp.solutions.face_mesh  # Load the Mediapipe Face Mesh model
mp_draw = mp.solutions.drawing_utils  # Utility to draw landmarks and connections

# Open the webcam for video input
cap = cv2.VideoCapture(0)

# Create a Mediapipe Face Mesh object
with mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Convert the BGR frame to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect facial landmarks
        results = face_mesh.process(img_rgb)

        # Check if a face was detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Draw the face landmarks on the frame
                mp_draw.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACE_CONNECTIONS,
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    mp_draw.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1)
                )

        # Display the frame with face mesh
        cv2.imshow("Face Mesh", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
