import cv2
import numpy as np
import os
import math

def calculate_angular_velocity(resolution, pixel_size, focal_length, time_between_frames, trail_length, known_speed_deg_per_sec):
    sensor_width = resolution * pixel_size
    fov_radians = sensor_width / focal_length
    fov_degrees = fov_radians * (180 / math.pi)
    angular_distance_per_frame = (fov_degrees / resolution) * trail_length
    angular_velocity = angular_distance_per_frame / time_between_frames
    
    # Adjust angular velocity using the known speed (4 degrees per arcsecond)
    # Convert the known speed from degrees per arcsecond to degrees per second
    known_speed_deg_per_sec *= 3600  # 1 arcsecond = 1/3600 degrees
    
    # Final angular velocity considering the known speed
    adjusted_angular_velocity = known_speed_deg_per_sec * (trail_length / resolution)
    
    return angular_velocity, adjusted_angular_velocity

def detect_trail_length(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return 0
    
    max_length = 0
    for contour in contours:
        length = cv2.arcLength(contour, False)
        if length > max_length:
            max_length = length
    
    return max_length

def process_images(image_files, camera_specs, known_speed_deg_per_sec):
    for image_file in image_files:
        trail_length = detect_trail_length(image_file)
        
        if trail_length > 0:
            angular_velocity, adjusted_angular_velocity = calculate_angular_velocity(
                camera_specs["resolution"],
                camera_specs["pixel_size"],
                camera_specs["focal_length"],
                camera_specs["time_between_frames"],
                trail_length,
                known_speed_deg_per_sec
            )
            print(f"Image: {os.path.basename(image_file)}")
            print(f"Trail Length: {trail_length:.2f} pixels")
            print(f"Calculated Angular Velocity: {angular_velocity:.6f} degrees/second")
            print(f"Adjusted Angular Velocity: {adjusted_angular_velocity:.6f} degrees/second\n")
        else:
            print(f"Image: {os.path.basename(image_file)} - No trail detected\n")

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

# Known speed of the satellite in degrees per arcsecond
known_speed_deg_per_arcsec = 4

# Process images for Camera 1
print("Processing images for Camera 1...\n")
process_images(image_files, camera_1, known_speed_deg_per_arcsec)

# Process images for Camera 2
print("Processing images for Camera 2...\n")
process_images(image_files, camera_2, known_speed_deg_per_arcsec)
