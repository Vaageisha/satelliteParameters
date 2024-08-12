import cv2
import numpy as np

def find_satellite_position(image):
    # Convert to grayscale if the image is not already
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply edge detection
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assume the largest contour by area is the satellite trail
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Return the center of the bounding box as the satellite position
        return (x + w // 2, y + h // 2)
    else:
        return None

# Load the images
image1 = cv2.imread('satellite_trail_1.png')
image2 = cv2.imread('satellite_trail_5.png')

# Find satellite positions in each image
pos1 = find_satellite_position(image1)
pos2 = find_satellite_position(image2)

# Print the coordinates
print(f"Image 1 Coordinates: {pos1}")
print(f"Image 2 Coordinates: {pos2}")

# Calculate the pixel distance if both positions are found
if pos1 and pos2:
    x1, y1 = pos1
    x2, y2 = pos2
    pixel_distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Define the image scale (arcseconds per pixel)
    scale = 1  # arcseconds per pixel

    # Convert pixel distance to angular distance in degrees
    # 1 arcsecond = 1/3600 degree
    angular_distance = pixel_distance * scale / 3600  # in degrees

    # Time interval in seconds
    delta_t = 60  # 1 minute*4

    # Calculate angular velocity in degrees per second
    angular_velocity = (angular_distance / delta_t)*(3.14159265359/180)

    print(f"Angular Distance: {angular_distance} degrees")
    print(f"Angular Velocity: {angular_velocity} radians/second")
else:
    print("Satellite position not found in one or both images.")
