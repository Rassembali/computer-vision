import cv2
import mediapipe as mp
import pyautogui  # Install using: pip install pyautogui

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

# Screen dimensions for mouse control
screen_width, screen_height = pyautogui.size()

# Create a Hands object
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Flip the frame horizontally for natural interaction
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Convert the frame to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame to detect hands
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the tip of the index finger
                x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
                y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)

                # Map hand position to screen size
                screen_x = int(x / w * screen_width)
                screen_y = int(y / h * screen_height)

                # Move the mouse
                pyautogui.moveTo(screen_x, screen_y)

        # Show the frame
        cv2.imshow("Virtual Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
