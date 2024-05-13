import cv2
import numpy as np

def detect_and_label_corners(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect corners using Shi-Tomasi corner detection
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=12, qualityLevel=0.01, minDistance=10)

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
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read the frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Detect and label corners
        labeled_frame = detect_and_label_corners(frame)

        # Display the frame with detected and labeled corners
        cv2.imshow('Camera Feed with Labeled Corners', labeled_frame)

        # Break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
