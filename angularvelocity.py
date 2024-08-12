import cv2
import numpy as np
import os
import math

def calculate_angular_velocity(resolution, pixel_size, focal_length, time_between_frames, trail_length):
    sensor_width = resolution * pixel_size
    fov_radians = sensor_width / focal_length
    fov_degrees = fov_radians * (180 / math.pi)
    angular_distance_per_frame = (fov_degrees / resolution) * trail_length
    angular_velocity = angular_distance_per_frame / time_between_frames
    return angular_velocity

def detect_trail_length(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply threshold to binarize the image
    _, thresh = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
    
    # Detect contours which correspond to the trails
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return 0
    
    # Find the longest contour which should correspond to the satellite trail
    max_length = 0
    for contour in contours:
        length = cv2.arcLength(contour, False)
        if length > max_length:
            max_length = length
    
    return max_length

def process_images(image_files, camera_specs):
    total_angular_velocity = 0
    count = 0
    
    for image_file in image_files:
        trail_length = detect_trail_length(image_file)
        
        if trail_length > 0:
            angular_velocity = calculate_angular_velocity(
                camera_specs["resolution"],
                camera_specs["pixel_size"],
                camera_specs["focal_length"],
                camera_specs["time_between_frames"],
                trail_length
            )
            total_angular_velocity += angular_velocity
            count += 1
            
            print(f"Image: {os.path.basename(image_file)}")
            print(f"Trail Length: {trail_length:.2f} pixels")
            print(f"Angular Velocity: {angular_velocity:.6f} degrees/second\n")
        else:
            print(f"Image: {os.path.basename(image_file)} - No trail detected\n")
    
    if count > 0:
        average_angular_velocity = total_angular_velocity / count
        print(f"Average Angular Velocity for {count} frames: {average_angular_velocity:.6f} degrees/second\n")
    else:
        print("No valid trails detected in the provided images.")

# Camera specifications
camera_1 = {
    "resolution": 2048,  # Resolution in pixels
    "pixel_size": 13.5e-3,  # Pixel size in mm
    "focal_length": 1000,  # Focal length in mm (assumed)
    "time_between_frames": 10  # Time between frames in seconds
}

camera_2 = {
    "resolution": 512,  # Resolution in pixels
    "pixel_size": 16e-3,  # Pixel size in mm
    "focal_length": 1000,  # Focal length in mm (assumed)
    "time_between_frames": 10  # Time between frames in seconds
}

# List of image files
image_files = [
    'satellite_trail_1.png',
    'satellite_trail_2.png',
    'satellite_trail_3.png',
    'satellite_trail_4.png',
    'satellite_trail_5.png'
]


# Process images for Camera 1
print("Processing images for Camera 1...\n")
process_images(image_files, camera_1)

# Process images for Camera 2
print("Processing images for Camera 2...\n")
process_images(image_files, camera_2)
