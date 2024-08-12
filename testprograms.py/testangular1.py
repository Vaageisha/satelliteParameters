import numpy as np
import cv2

# Constants
satellite_velocity_m_per_s = 7599.68  # Linear velocity of Starlink satellites in meters per second
earth_radius = 6371000  # Earth radius in meters

# Given data for Camera 1 and Camera 2
camera_1 = {
    "resolution": 2048,  # Resolution in pixels
    "pixel_size": 13.5e-3,  # Pixel size in mm
    "focal_length": 1000,  # Focal length in mm (assumed)
    "trail_length": 100,  # length of satellite trail across pixels
    "time_between_frames": 10  # Time between frames in seconds
}

camera_2 = {
    "resolution": 512,  # Resolution in pixels
    "pixel_size": 16e-3,  # Pixel size in mm
    "focal_length": 1000,  # Focal length in mm (assumed)
    "trail_length": 100,  # length of satellite trail across pixels
    "time_between_frames": 10  # Time between frames in seconds
}

# Function to calculate FOV, angular displacement, angular velocity, and distance
def calculate_satellite_distance(camera, satellite_velocity):
    # Calculate sensor size in mm
    sensor_size_mm = camera["resolution"] * camera["pixel_size"]
    
    # Calculate FOV in radians
    fov_radians = 2 * np.arctan(sensor_size_mm / (2 * camera["focal_length"]))
    
    # Calculate angular displacement in radians 
    angular_displacement_radians = (camera["trail_length"] / camera["resolution"]) * fov_radians
    
    # Calculate angular velocity in radians per second
    angular_velocity_radians_per_second = angular_displacement_radians / camera["time_between_frames"]
    
    return {
        "fov_radians": fov_radians,
        "angular_displacement_radians": angular_displacement_radians,
        "angular_velocity_radians_per_second": angular_velocity_radians_per_second,
    }

# Function to process an image
def process_image(image_path, camera, satellite_velocity):
    # Read the image
    image = cv2.imread(image_path)
    
    # Ensure image is read correctly
    if image is None:
        print(f"Error reading image {image_path}")
        return None
    
    # Perform calculations (assuming you might use image data here)
    # For this example, we'll just perform the calculations as before
    camera_properties = calculate_satellite_distance(camera, satellite_velocity)
    
    return camera_properties

# Function to calculate and print average angular displacement and velocity
def calculate_and_print_averages(camera_1_displacements, camera_1_velocities, camera_2_displacements, camera_2_velocities):
    average_camera_1_angular_displacement = np.mean(camera_1_displacements)
    average_camera_1_angular_velocity = np.mean(camera_1_velocities)
    average_camera_2_angular_displacement = np.mean(camera_2_displacements)
    average_camera_2_angular_velocity = np.mean(camera_2_velocities)

    print(f"Average Camera 1 Angular Displacement: {average_camera_1_angular_displacement:.4f} rad")
    print(f"Average Camera 1 Angular Velocity: {average_camera_1_angular_velocity:.4f} rad/s")
    print(f"Average Camera 2 Angular Displacement: {average_camera_2_angular_displacement:.4f} rad")
    print(f"Average Camera 2 Angular Velocity: {average_camera_2_angular_velocity:.4f} rad/s")

# List of image paths
image_paths = [
    'satellite_trail_1.png',
    'satellite_trail_2.png',
    'satellite_trail_3.png',
    'satellite_trail_4.png',
    'satellite_trail_5.png'
]

# Process images with Camera 1 and Camera 2
camera_1_angular_displacements = []
camera_1_angular_velocities = []
camera_2_angular_displacements = []
camera_2_angular_velocities = []

for image_path in image_paths:
    print(f"Processing image: {image_path}")
    
    # Process with Camera 1
    camera_1_properties = process_image(image_path, camera_1, satellite_velocity_m_per_s)
    if camera_1_properties:
        print(f"Camera 1 - FOV: {camera_1_properties['fov_radians']:.4f} rad")
        print(f"Camera 1 - Angular Displacement: {camera_1_properties['angular_displacement_radians']:.4f} rad")
        print(f"Camera 1 - Angular Velocity: {camera_1_properties['angular_velocity_radians_per_second']:.4f} rad/s")
        camera_1_angular_displacements.append(camera_1_properties['angular_displacement_radians'])
        camera_1_angular_velocities.append(camera_1_properties['angular_velocity_radians_per_second'])
        print("\n" + "_"*40 + "\n")
    
    # Process with Camera 2
    camera_2_properties = process_image(image_path, camera_2, satellite_velocity_m_per_s)
    if camera_2_properties:
        print(f"Camera 2 - FOV: {camera_2_properties['fov_radians']:.4f} rad")
        print(f"Camera 2 - Angular Displacement: {camera_2_properties['angular_displacement_radians']:.4f} rad")
        print(f"Camera 2 - Angular Velocity: {camera_2_properties['angular_velocity_radians_per_second']:.4f} rad/s")
        camera_2_angular_displacements.append(camera_2_properties['angular_displacement_radians'])
        camera_2_angular_velocities.append(camera_2_properties['angular_velocity_radians_per_second'])
        print("\n" + "_"*40 + "\n")
       
    print("\n" + "="*40 + "\n")

# Calculate and print averages
calculate_and_print_averages(camera_1_angular_displacements, camera_1_angular_velocities, camera_2_angular_displacements, camera_2_angular_velocities)
