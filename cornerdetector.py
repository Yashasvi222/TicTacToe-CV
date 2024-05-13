import cv2
import numpy as np

def detect_and_label_corners(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect corners using Shi-Tomasi corner detection
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=14, qualityLevel=0.01, minDistance=10)

    # If no corners are found, return the original image
    if corners is None:
        return image
    
    # Convert corners to integers
    corners = np.int0(corners)
    
    # Sort corners by x-coordinate
    corners = sorted(corners, key=lambda x: x[0][0])
    
    # Draw circles at the corner positions and label them sequentially
    labeled_image = image.copy()
    for i, corner in enumerate(corners):
        x, y = corner.ravel()
        cv2.circle(labeled_image, (x, y), 5, (0, 255, 0), -1)
        cv2.putText(labeled_image, f"Corner {i+1}", (x+10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    return labeled_image

def main():
    # Read the input image
    image = cv2.imread("TicTacToe-CV\\TTT.png")  # Replace 'input_image.jpg' with your image file name
    
    if image is None:
        print("Error: Unable to load image.")
        return

    # Detect and label corners
    labeled_image = detect_and_label_corners(image)

    # Display the image with detected and labeled corners
    cv2.imshow('Image with Labeled Corners', labeled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()