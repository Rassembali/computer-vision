import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

# Create a Hands object
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Convert the frame to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hands
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmarks
                landmarks = hand_landmarks.landmark

                # Calculate which fingers are raised
                fingers = []
                # Thumb
                if landmarks[mp_hands.HandLandmark.THUMB_TIP].x < landmarks[mp_hands.HandLandmark.THUMB_IP].x:
                    fingers.append(1)  # Raised
                else:
                    fingers.append(0)  # Not raised
                # Fingers
                for id in range(1, 5):
                    if landmarks[mp_hands.HandLandmark(id * 4 + 4)].y < landmarks[mp_hands.HandLandmark(id * 4 + 2)].y:
                        fingers.append(1)  # Raised
                    else:
                        fingers.append(0)  # Not raised

                # Count fingers
                total_fingers = sum(fingers)

                # Display the count
                cv2.putText(frame, f'Fingers: {total_fingers}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show the frame
        cv2.imshow("Finger Count", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
