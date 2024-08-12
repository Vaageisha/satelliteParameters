import numpy as np
import matplotlib.pyplot as plt
import cv2

# Parameters
num_images = 5  # Number of consecutive images
image_size = (500, 500)  # Size of the image in pixels
num_stars = 50  # Number of stars
trail_length = 200  # Length of the satellite trail
trail_width = 2.5  # Width of the satellite trail
trail_brightness = 220  # Brightness of the satellite trail (0-255)
noise_level = 0.005  # Level of noise in the background

# Create starfield
np.random.seed(42)  # For reproducibility
stars_x = np.random.uniform(0, image_size[0], num_stars).astype(int)
stars_y = np.random.uniform(0, image_size[1], num_stars).astype(int)

# Generate consecutive images
for i in range(num_images):
    # Create a black image
    image = np.zeros((image_size[0], image_size[1]), dtype=np.uint8)

    # Draw stars
    for x, y in zip(stars_x, stars_y):
        cv2.circle(image, (x, y), radius=1, color=(255), thickness=-1)

    # Calculate satellite trail positions for this image
    trail_start = (50 + i * 20, 450 - i * 20)
    trail_end = (450 + i * 20, 50 - i * 20)

    # Draw satellite trail
    cv2.line(image, trail_start, trail_end, color=(trail_brightness), thickness=int(trail_width))

    # Annotate selected stars
    selected_stars = [(100, 400, 'C1'), (200, 300, 'C2'), (350, 150, 'C3')]
    for x, y, label in selected_stars:
        cv2.circle(image, (x, y), radius=5, color=(255), thickness=1)
        cv2.putText(image, label, (x + 6, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255), 1)

    # Add Gaussian noise
    noise = np.random.normal(0, noise_level * 255, image_size).astype(np.uint8)
    noisy_image = cv2.add(image, noise)

    # Plot and save the image
    plt.figure(figsize=(6, 6))
    plt.imshow(noisy_image, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.title(f"Simulated Satellite Trail - Image {i+1}")
    plt.savefig(f'satellite_trail_{i+1}.png', dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
    plt.close()

print("Consecutive satellite trail images generated.")
