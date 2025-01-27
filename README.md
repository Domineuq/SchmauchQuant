# SchmauchQuant
<img src="https://github.com/user-attachments/assets/3cbffa52-4978-4b24-b59d-6db8a1b08bca" width="400" height="400">



### Automatic gunshot residue quantification
This tool is intended to automatically qunatify gunshot residues (number and area)

Created by the [Forensic Medicine and Imaging Research Group](https://dbe.unibas.ch/en/research/imaging-modelling-diagnosis/forensic-medicine-imaging-research-group/).
If you use it, please cite our publication: 
tbd

# Requirements
+ cv2
+ numpy
+ OS

# Pipeline
Preparatory steps:
+ A digitised high-resolution image of gunshot residues is required

Script:
+ Import Necessary Libraries: Import OpenCV (cv2), NumPy (np), and OS module.
+ Define the Function: segment_by_refined_threshold(input_path, output_dir) to 
segment an image based on thresholding.
+ Load the Image: Use OpenCV to read the image from the specified input_path.
+ Check Image Validity: Ensure the image is loaded correctly; otherwise, print 
an error message and exit the function.
+ Convert Colour Space: Transform the image from RGB (Red, Green, Blue) to 
HSV (Hue, Saturation, Value) colour space.
+ Extract Value Channel: Isolate the Value channel from the HSV image, which 
is useful for intensity-based segmentation.
+ Dynamic Threshold Calculation:
Compute the minimum and maximum pixel values of the Value channel.
+ Calculate a threshold value as the mean of these extremes, adjusted by a 
factor (0.5 in this case).
+ Threshold Application: Apply a binary inverse threshold to the Value channel 
using the calculated threshold value.
+ Morphological Cleaning (Optional): Perform opening and closing operations 
to refine the segmented areas, improving the quality.
+ Connected Components Analysis:
Identify connected components in the cleaned image to detect and count distinct 
particles.
+ Calculate the number of detected particles and the total area covered 
by them.
+ Prepare Output:
  + Extract filename and extension from input_path.
  + Construct the output filename and path.
  + Save Segmented Image: Write the processed image to the specified output_dir.
+ Print Details: Output information about the image processing, 
including threshold values, number of particles, total area, and the save 
location of the segmented image.

# Usage
+ Download the python script
+ Define the path where you have located your digitised image 
+ Define the path where you want to save the segmented image

# MIT License


