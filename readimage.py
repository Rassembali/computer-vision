import cv2

# Read an image from a file
image = cv2.imread("image.jpg")

# Display the image
cv2.imshow("Image", image)

# Save the image
cv2.imwrite("output.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 2)
# Parameters:
# - image: Image on which to draw
# - (50, 50): Top-left corner
# - (200, 200): Bottom-right corner
# - (255, 0, 0): Color in BGR (Blue, Green, Red)
# - 2: Thickness of the rectangle

# Draw a circle
cv2.circle(image, (300, 300), 50, (0, 255, 0), 3)
# Parameters:
# - image: Image on which to draw
# - (300, 300): Center of the circle
# - 50: Radius of the circle
# - (0, 255, 0): Color in BGR (Blue, Green, Red)
# - 3: Thickness of the circle

# Draw a line
cv2.line(image, (0, 0), (400, 400), (0, 0, 255), 2)
# Parameters:
# - image: Image on which to draw
# - (0, 0): Starting point of the line
# - (400, 400): Ending point of the line
# - (0, 0, 255): Color in BGR (Blue, Green, Red)
# - 2: Thickness of the line

# Add text
cv2.putText(image, "OpenCV Basics", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
# Parameters:
# - image: Image on which to draw text
# - "OpenCV Basics": The text to display
# - (50, 400): Bottom-left corner of the text
# - cv2.FONT_HERSHEY_SIMPLEX: Font style
# - 1: Font scale (size)
# - (0, 255, 255): Color in BGR
# - 2: Thickness of the text

cv2.imshow("Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert to grayscale
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSV
#hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#cv2.imshow("Grayscale", gray_image)
#cv2.imshow("HSV", hsv_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Gaussian blur
#gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Median blur
#median_blur = cv2.medianBlur(image, 5)

# Simple average blur
#average_blur = cv2.blur(image, (15, 15))

#cv2.imshow("Gaussian Blur", gaussian_blur)
#cv2.imshow("Median Blur", median_blur)
#cv2.imshow("Average Blur", average_blur)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


