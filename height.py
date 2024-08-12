import numpy as np
from scipy.optimize import fsolve

# Constants
G = 6.67430e-11  # Gravitational constant in m³/kg/s²
M = 5.972e24  # Mass of Earth in kg
r_cp_km = 6371  # Distance from the center of the Earth to the observer in km
r_cp_m = r_cp_km * 1000  # Convert to meters for internal calculations

# Function to solve cubic equation
def cubic_eq(h, omega_p_squared, GM, r_cp):
    return h**3 + r_cp * h**2 - (2 * GM) / omega_p_squared

def calculate_height(omega_p1, omega_p2):
    omega_p_squared1 = omega_p1**2
    omega_p_squared2 = omega_p2**2
    
    # Calculate GM from Kepler's law
    GM = G * M  # GM in m³/s²
    
    # Define the cubic equation function for the given angular velocity
    def equation1(h):
        h_m = h * 1000  # Convert height from km to meters
        return cubic_eq(h_m, omega_p_squared1, GM, r_cp_m)
    
    def equation2(h):
        h_m = h * 1000  # Convert height from km to meters
        return cubic_eq(h_m, omega_p_squared2, GM, r_cp_m)
    
    # Initial guess for height (in km)
    initial_guess = 1000  # Assume 1000 km as an initial guess
    
    # Solve the cubic equation
    height_solution1, = fsolve(equation1, initial_guess)
    height_solution2, = fsolve(equation2, initial_guess)
    
    # Check if the result is reasonable
    if np.isnan(height_solution1) or np.isinf(height_solution1) or height_solution1 < 0:
        raise ValueError("No valid solution found for the height")
    if np.isnan(height_solution2) or np.isinf(height_solution2) or height_solution2 < 0:
        raise ValueError("No valid solution found for the height")
    
    # Convert height from meters to kilometers for the result
    height_km1 = height_solution1
    height_km2 = height_solution2
    return height_km1, height_km2

# Updated angular velocities from calculated value
omega_p1 = 0.0175  # Calculated angular velocity
omega_p2 = 0.0208  

# Calculate height
try:
    height_above_surface1, height_above_surface2 = calculate_height(omega_p1, omega_p2)
    average_height_above_surface = (height_above_surface1 + height_above_surface2) / 2
   
    print(f"Average Height Above Earth's Surface: {average_height_above_surface:.2f} km")
except ValueError as e:
    print(f"Error: {e}")
