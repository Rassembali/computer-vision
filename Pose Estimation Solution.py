# Import necessary libraries
import cv2
import mediapipe as mp

# Initialize Mediapipe Pose and Drawing utilities
mp_pose = mp.solutions.pose  # Load the Mediapipe Pose model
mp_draw = mp.solutions.drawing_utils  # Utility to draw landmarks and connections

# Open the webcam for video input
cap = cv2.VideoCapture(0)

# Create a Mediapipe Pose object
with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Convert the BGR frame to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect pose landmarks
        results = pose.process(img_rgb)

        # Check if a pose was detected
        if results.pose_landmarks:
            # Draw pose landmarks and connections on the frame
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display the frame with pose estimation
        cv2.imshow("Pose Estimation", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()
