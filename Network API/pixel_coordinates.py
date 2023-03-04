import cv2
import numpy as np
import json

# Load the image
image = cv2.imread("output.png")

# Convert the image from BGR to RGB color space
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the lower and upper bounds for the red color in RGB color space
red_lower = np.array([220, 0, 0])
red_upper = np.array([255, 50, 50])

# Create a mask for the red color using the lower and upper bounds
red_mask = cv2.inRange(image, red_lower, red_upper)

# Find the contours of the red dots
red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the coordinates of the centers of the red dots
red_points = []
for contour in red_contours:
    # Get the bounding rectangle of the contour
    (x, y, w, h) = cv2.boundingRect(contour)
    # Calculate the center of the bounding rectangle
    cx = x + int(w/2)
    cy = y + int(h/2)
    red_points.append((cx, cy))

# Print the coordinates of the red points
#print("Red points:")
#print(red_points)
print("Length",len(red_points))
red_points.reverse()
print(red_points)
my_dict = {(index+1): item for index, item in enumerate(red_points)}

# Print the dictionary
#print(my_dict)

with open('coord_dict.json', 'w') as f:
    json.dump(my_dict, f )

