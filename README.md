# Satellite Trail Analysis

## Project Overview

This project involves analyzing a set of 5 simulated satellite trail images to extract key information,
including the angular velocity, height, and magnitude of the satellite. The images are captured from two 
different cameras with varying specifications. The main goal is to process these images, detect the satellite
trails, and compute the angular velocity, height, and magnitude of the satellite based on the observed trails.

## 1. Angular Velocity

We will analysize a set of simulated satellite trail images captured by two different cameras.
The primary objective is to calculate the angular velocity of the satellite by detecting the trail length in each image.
The program processes the images, computes the angular velocity for each frame, and then provides the average angular velocity for all frames.

## Prerequisites :
  
- Python 3.7+
- OpenCV for image processing (`opencv-python`)
- NumPy for numerical computations (`numpy`)

## Features:

1. Satellite Trail Detection:
  Detects the satellite trail in the provided images using contour detection.
  
2. Angular Velocity Calculation:
  Calculates the angular velocity of the satellite based on the trail length detected in each image and the known camera specifications.
  
3. Average Angular Velocity:
  Computes the average angular velocity over all the provided images.


## 2. Satellite Height Calculation (using Zenith ranging):

We will calculate the height of a satellite above Earth's surface using the concept of zenith ranging.
Zenith ranging leverages the angular velocity of the satellite as observed from Earth, along with gravitational 
and orbital mechanics principles, to derive the satellite's altitude. The height is determined by solving a cubic
equation that incorporates key orbital parameters.

## Features:

1. Height calculation:
   Utilizes the zenith ranging method to determine the satellite's height above Earth's surface.
   Solves a cubic equation derived from the relationship between the satellite's angular velocity, linear velocity, and gravitational forces.
   

## 3. Number of Photons collected Calculation:

 We will calculate the number of photons collected by the sensor, by calculating the apparent magnitude, flux and photon count for the same.
    
## Features:

1.Apparent Magnitude Calculation:
  Calculates the apparent magnitude of a satellite based on its flux, telescope aperture, and distance from Earth.
    
2.Flux Calculation:
  Determines the flux received from the satellite, adjusted for its apparent magnitude.
    
 3.Photon Count Calculation:
   Computes the number of photons detected by the telescope during the observation period, considering telescope efficiency and mirror loss.
    




