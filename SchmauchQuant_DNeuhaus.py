# -*- coding: utf-8 -*-
"""

----
SchmauchQuant
----


Created on Tue Sep 24 15:36:31 2024

@author: Dominique Neuhaus

Quantification of gunshot residues


# Description of main steps
1. Import Necessary Libraries: Import OpenCV (cv2), NumPy (np), and OS module.
2. Define the Function: segment_by_refined_threshold(input_path, output_dir) to 
segment an image based on thresholding.
3. Load the Image: Use OpenCV to read the image from the specified input_path.
4. Check Image Validity: Ensure the image is loaded correctly; otherwise, print 
an error message and exit the function.
5. Convert Colour Space: Transform the image from RGB (Red, Green, Blue) to 
HSV (Hue, Saturation, Value) colour space.
6. Extract Value Channel: Isolate the Value channel from the HSV image, which 
is useful for intensity-based segmentation.
7. Dynamic Threshold Calculation:
Compute the minimum and maximum pixel values of the Value channel.
8. Calculate a threshold value as the mean of these extremes, adjusted by a 
factor (0.5 in this case).
9. Threshold Application: Apply a binary inverse threshold to the Value channel 
using the calculated threshold value.
10. Morphological Cleaning (Optional): Perform opening and closing operations 
to refine the segmented areas, improving the quality.
11. Connected Components Analysis:
Identify connected components in the cleaned image to detect and count distinct 
particles.
12. Calculate the number of detected particles and the total area covered 
by them.
13. Prepare Output:
Extract filename and extension from input_path.
Construct the output filename and path.
Save Segmented Image: Write the processed image to the specified output_dir.
14. Print Details: Output information about the image processing, 
including threshold values, number of particles, total area, and the save 
location of the segmented image.

"""



# %% Use Value channel and adaptive threshold
import cv2
import numpy as np
import os

def segment_by_refined_threshold(input_path, output_dir):
    # Load the original image
    image = cv2.imread(input_path)
    if image is None:
        print("Error: Image not found.")
        return

    # Convert the image from RGB to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Extract the Value channel
    value_channel = hsv_image[:, :, 2]

    # Calculate the dynamic threshold based on pixel statistics
    min_val = np.min(value_channel)
    max_val = np.max(value_channel)
    threshold_value = min_val + 0.5 * (max_val - min_val)  # Adjust the range increment here if necessary

    print(f"Min pixel value: {min_val}, Max pixel value: {max_val}, Threshold: {threshold_value}")

    # Apply the adjusted threshold
    _, segmented_image = cv2.threshold(value_channel, threshold_value, 255, cv2.THRESH_BINARY_INV)

    # Optional: Morphological cleaning to refine the segmented areas
    kernel = np.ones((1, 1), np.uint8)
    cleaned_image = cv2.morphologyEx(segmented_image, cv2.MORPH_OPEN, kernel, iterations=1)
    cleaned_image = cv2.morphologyEx(cleaned_image, cv2.MORPH_CLOSE, kernel, iterations=2)

    # cleaned_image = segmented_image


    # Find connected components (particles)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(cleaned_image, connectivity=8)

    # Calculate the number of particles and total area
    num_particles = num_labels - 1  # Subtract one for the background
    total_area = np.sum(stats[1:, cv2.CC_STAT_AREA])  # Exclude area for the background

    print(f"Number of particles: {num_particles}")
    print(f"Total area of particles: {total_area} pixels")

    # Prepare output path
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}_segmented{ext}"
    output_path = os.path.join(output_dir, output_filename)

    # Save the segmented image
    cv2.imwrite(output_path, cleaned_image)
    print(f"Segmented image saved to {output_path}")

# Example usage
input_path = 'C:/Users/Dominique/Documents/00_Diverses/25_Schmauch_Joel/01_Fotos/03_FilmoluxFolien/D7_Filmolux.PNG'
output_dir = 'C:/Users/Dominique/Documents/00_Diverses/25_Schmauch_Joel/03_Output/03_Filmolux'
segment_by_refined_threshold(input_path, output_dir)



