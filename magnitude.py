import numpy as np

# Constants
earth_radius = 6371000  # Earth radius in meters

# Given parameters
height_above_surface = 563.91  # Given height in meters
angular_velocity_camera1 = 0.0175  # Angular velocity for Camera 1 in rad/s
angular_velocity_camera2 = 0.0208  # Angular velocity for Camera 2 in rad/s

# Constants for photon calculations
M = 0  # Magnitude of the reference star (VEGA)
F = 3.63e-11  # Reference flux in W/m²/nm
E = 3.625e-19  # Energy per photon in J
A = 1.327  # Telescope aperture area in m²
efficiency = 0.35
mirror_loss = 0.65
exposure_time = 60  # seconds
photon_divisor = 31910621 #(pie*r^2/563.91(surface area))

# Function to calculate apparent magnitude
def calculate_apparent_magnitude(M, F, A, E, distance_factor):
    term = (F * A) / E
    m = M - 2.5 * np.log10(term) + 2.5 * np.log10(distance_factor)
    return m

# Function to calculate flux for Starlink
def calculate_flux_starlink(M, apparent_magnitude):
    f = 3.63e-11  # Reference flux of Vega
    return f * 10**(-0.4 * apparent_magnitude)

# Function to calculate the number of photons
def calculate_photons(flux_starlink, A, E, efficiency, mirror_loss, exposure_time):
    photon_count = (flux_starlink * A) / E
    adjusted_photon_count = photon_count * efficiency * mirror_loss * exposure_time
    return adjusted_photon_count

# Calculate the surface area factor
distance_to_satellite = earth_radius + height_above_surface
surface_area = 4 * np.pi * (distance_to_satellite ** 2)
distance_factor = surface_area / (4 * np.pi * (earth_radius ** 2))

# Use Camera 1 angular velocity for calculations
angular_velocity = angular_velocity_camera1

# Calculate apparent magnitude
apparent_magnitude = calculate_apparent_magnitude(M, F, A, E, distance_factor)

# Calculate flux for Starlink
flux_starlink = calculate_flux_starlink(M, apparent_magnitude)

# Calculate adjusted photon count
adjusted_photon_count = calculate_photons(
    flux_starlink, A, E, efficiency, mirror_loss, exposure_time
)

# Divide the final photon count
final_photon_count_per_second = adjusted_photon_count / photon_divisor

# Print results
print(f"Apparent Magnitude: {apparent_magnitude:.2f}")
print(f"Flux for Starlink: {flux_starlink:.2e} W/m²/nm")
print(f"Adjusted Photon Count: {adjusted_photon_count:.2e}")
print(f"Final Photon Count per Second: {final_photon_count_per_second:.2e}")

# Output results for Camera 2 as well
angular_velocity = angular_velocity_camera2

# Calculate apparent magnitude for Camera 2
apparent_magnitude_camera2 = calculate_apparent_magnitude(M, F, A, E, distance_factor)

# Calculate flux for Starlink for Camera 2
flux_starlink_camera2 = calculate_flux_starlink(M, apparent_magnitude_camera2)

# Calculate adjusted photon count for Camera 2
adjusted_photon_count_camera2 = calculate_photons(
    flux_starlink_camera2, A, E, efficiency, mirror_loss, exposure_time
)

# Divide the final photon count by 31,910,621 for Camera 2
final_photon_count_per_second_camera2 = adjusted_photon_count_camera2 / photon_divisor

# Print results for Camera 2
print(f"Apparent Magnitude (Camera 2): {apparent_magnitude_camera2:.2f}")
print(f"Flux for Starlink (Camera 2): {flux_starlink_camera2:.2e} W/m²/nm")
print(f"Adjusted Photon Count (Camera 2): {adjusted_photon_count_camera2:.2e}")
print(f"Final Photon Count per Second (Camera 2): {final_photon_count_per_second_camera2:.2e}")
