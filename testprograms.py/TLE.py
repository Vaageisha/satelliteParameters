
from sgp4.api import Satrec
from sgp4.api import jday
import numpy as np

# TLE data for Starlink 1113
tle_line1 = "1 44926U 20001N   24210.25001157  .00140456  00000-0  11446-2 0  9996"
tle_line2 = "2 44263  53.2074 237.7381 0003052 192.9686 167.1760 15.12659484716176"

# Create satellite object
satellite = Satrec.twoline2rv(tle_line1, tle_line2)

# Current Julian date
jd, fr = jday(2024, 7, 29, 0, 0, 0)  # Example for July 29, 2024

# Get satellite position and velocity vectors
e, r, v = satellite.sgp4(jd, fr)
 
9
# Convert position (r) and velocity (v) from km and km/s to meters and meters/second
r = np.array(r) * 1000
v = np.array(v) * 1000

# Calculate the distance from the center of Earth
distance_from_earth_center = np.linalg.norm(r)

# Calculate the height above Earth's surface
earth_radius = 6371000  # Earth radius in meters
height_above_surface = distance_from_earth_center - earth_radius

# Calculate the velocity magnitude
velocity_magnitude = np.linalg.norm(v)

# Results
print(f"Height above Earth's surface: {height_above_surface:.2f} meters")
print(f"Velocity magnitude: {velocity_magnitude:.2f} meters/second")

#Magnitude calculation.

# Constants
M = 0  # Magnitude of the reference star (VEGA)
F_reference = 3.63e-11  # Reference flux of VEGA in W/m²
E = 3.625e-19  # Energy per photon in J
A_telescop = 1.327  # Aperture area of the telescope in m²

# Given Parameters
efficiency = 0.35
mirror_loss = 0.65
exposure_time = 60  # seconds

# Calculate Apparent Magnitude
def calculate_apparent_magnitude(M, F, A, E):
    term = (F * A) / E
    m = M - 2.5 * np.log10(term)
    return m

# Calculate Flux for Starlink
def calculate_flux(F_reference, m):
    return F_reference + 10**(-0.4 * m)

# Calculate Number of Photons
def calculate_photon_count(F, A, E):
    return (F * A) / E

# Calculate Adjusted Photon Count
def calculate_adjusted_photon_count(photon_count, efficiency, mirror_loss, exposure_time):
    return photon_count * efficiency * mirror_loss * exposure_time/31910621


# Calculate the apparent magnitude
apparent_magnitude = calculate_apparent_magnitude(M, F_reference, A_telescop, E)
print(f"Apparent Magnitude: {apparent_magnitude:.2f}")

# Calculate the flux for Starlink
flux_starlink = calculate_flux(F_reference, apparent_magnitude)
print(f"Flux for Starlink: {flux_starlink:.2e} W/m²")

# Calculate the number of photons
photon_count = calculate_photon_count(flux_starlink, A_telescop, E)
print(f"Photon Count per Second: {photon_count:.2e}")

# Calculate the adjusted photon count
adjusted_photon_count = calculate_adjusted_photon_count(photon_count, efficiency, mirror_loss, exposure_time)
print(f"Adjusted Photon Count: {adjusted_photon_count:.2e}")
