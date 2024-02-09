from PIL import Image
import numpy as np

# Load the image
img_path = img_path = "C:\\Users\\xxxxxxxxxx.jpg"  

image = Image.open(img_path)

# Convert the image to grayscale
bw_image = image.convert('L')

# Now, convert the image to have a white background with black content
# This is done by ensuring that every pixel that is not completely black is turned white
threshold = 150
bw_image = bw_image.point(lambda p: p > threshold and 233)

# Save the resulting image
bw_image_path = img_path = "C:\\Users\\yyyyyyyyy.jpg"  
bw_image.save(bw_image_path)

bw_image_path



