import numpy as np
import cv2  # type: ignore
from PIL import Image
from scipy import ndimage  # type: ignore

# Burulish burchagini aniqlash uchun yordamchi funksiya
def find_angle(x1, y1, x2, y2):
    return np.degrees(np.arctan2(y2 - y1, x2 - x1))


# Burulish burchagini aniqlaymiz va rasmni ag'daramiz
def detect_and_rotate(image):
    try:
        if image is None:
            return None

        # Convert PIL Image to numpy array (RGB to BGR for OpenCV)
        img_before = np.array(image)
        
        # Check if the image is in the correct format
        if img_before.dtype != np.uint8:
            img_before = img_before.astype(np.uint8)

        img_before = cv2.cvtColor(img_before, cv2.COLOR_RGB2BGR)
        
        # Convert image to grayscale
        img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
        
        # Detect edges using Canny
        img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)

        # Detect lines using Hough Transform
        lines = cv2.HoughLinesP(
            img_edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=5
        )

        # If no lines are detected, return the original image
        if lines is None:
            return Image.fromarray(cv2.cvtColor(img_before, cv2.COLOR_BGR2RGB))

        # Calculate angles from detected lines
        angles = [find_angle(x1, y1, x2, y2) for line in lines for x1, y1, x2, y2 in line]
        filtered_angles = [angle for angle in angles if 45 <= abs(angle) <= 135]

        # If no significant angles are found, return the original image
        if not filtered_angles:
            return Image.fromarray(cv2.cvtColor(img_before, cv2.COLOR_BGR2RGB))

        # Get the median angle to correct the rotation
        median_angle = np.median(filtered_angles)
        
        # Rotate the image based on the median angle
        img_rotated = ndimage.rotate(img_before, median_angle)

        # Convert back to PIL image and return
        return Image.fromarray(cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB))

    except Exception as e:
        print(f"Xato: {e}")
        return None
