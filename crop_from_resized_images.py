import os
from PIL import Image

# Define the paths
input_folder = 'coc_images_resized'
output_folder = 'coc_images_resized_crops'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Crop dimensions
crop_width = 300
crop_height = 100

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Check for image files
        # Open an image file
        with Image.open(os.path.join(input_folder, filename)) as img:
            img_width, img_height = img.size

            # Calculate the number of crops that can be taken
            # We will use a step size of 100 pixels to allow for overlap
            step_size = 100

            # Iterate to create crops
            for left in range(0, img_width - crop_width + 1, step_size):
                upper = 0  # Start from the top of the image
                right = left + crop_width
                lower = upper + crop_height

                # Crop the image
                img_cropped = img.crop((left, upper, right, lower))

                # Save the cropped image
                crop_filename = f"{os.path.splitext(filename)[0]}_crop_{left // step_size + 1}.png"  # Save as PNG
                img_cropped.save(os.path.join(output_folder, crop_filename))

print("All crops have been created and saved in 'coc_images_resized_crops'.")
