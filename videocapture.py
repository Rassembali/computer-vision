# Import the OpenCV library
import cv2  # OpenCV is used for computer vision tasks

# Open the default camera (0 is the default ID for the first webcam)
cap = cv2.VideoCapture(0)

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Read and display frames from the camera
while True:
    ret, frame = cap.read()  # Read a single frame from the camera
    if not ret:  # If the frame could not be read, stop the loop
        print("Error: Could not read a frame from the webcam.")
        break

    # Display the frame in a window
    cv2.imshow("Webcam Feed", frame)

    # Wait for a key press; exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the display window
cap.release()
cv2.destroyAllWindows()
