import cv2

# Read the image
img = cv2.imread('car.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray = cv2.GaussianBlur(gray, (3,3), 0)

# Apply adaptive thresholding to binarize the image
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours in the binary image
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours
for contour in contours:
    # Approximate the contour to a polygon
    polygon = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    # Check if the polygon has 4 sides (i.e. it is a rectangle)
    if len(polygon) == 4:
        # Get the bounding rectangle of the rectangle
        x, y, w, h = cv2.boundingRect(polygon)

        # Check if the aspect ratio of the rectangle is close to 4.5
        aspect_ratio = float(w)/h
        print("alll",aspect_ratio)

        if aspect_ratio > 4.5 and aspect_ratio < 5:
            print("hedha ey" ,aspect_ratio)
            # Draw a rectangle around the license plate
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            # Crop the license plate from the image
            plate = img[y:y+h, x:x+w]
            cv2.imshow("License Plate", plate)
            cv2.waitKey()

cv2.destroyAllWindows()
