import random
import os
from PIL import Image, ImageDraw, ImageFont


# Function to generate random numbers, ensuring it doesn't start with zero
def generate_random_number(length):
    first_digit = random.choice('123456789')  # First digit can't be zero
    remaining_digits = ''.join(random.choices('0123456789', k=length - 1))
    return first_digit + remaining_digits


# Function to format the number with spaces every three digits
def format_number_with_spaces(number):
    return ' '.join([number[max(i - 3, 0):i] for i in range(len(number), 0, -3)][::-1])


# Define the paths to the existing folders
background_dir = "coc_images_resized_crops"  # Changed to use the crops directory
output_dir = "numbers"
images_dir = os.path.join(output_dir, "images")
labels_dir = os.path.join(output_dir, "labels")

# Ensure the 'images' and 'labels' directories exist
os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

# Generate images and labels
for i in range(1000):  # Create 1000 images as an example
    length = random.choice([3, 4, 5, 6, 7, 8])  # Randomly choose a length from 3 to 8
    # Generate a random number
    label = generate_random_number(length)

    # Format the label for display (with spaces)
    formatted_label = format_number_with_spaces(label)

    # Load a random background image from the coc_images_resized_crops folder
    background_files = [f for f in os.listdir(background_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    background_file = random.choice(background_files)
    background_path = os.path.join(background_dir, background_file)
    background_image = Image.open(background_path)

    # Get the dimensions of the background image
    bg_width, bg_height = background_image.size

    # Define the cropping dimensions (400x100)
    cropped_width = 300
    cropped_height = 100

    # Ensure the cropping coordinates stay within the bounds of the original image
    left = random.randint(0, bg_width - cropped_width)
    top = random.randint(0, bg_height - cropped_height)
    right = left + cropped_width
    bottom = top + cropped_height

    # Crop the background image to the desired random portion
    cropped_background = background_image.crop((left, top, right, bottom))

    # Define the font path and font size
    font_path = "Clash-Regular.ttf"  # Replace with your font file path
    font_size = 35  # Adjust as needed

    # Load the font and create a drawing context
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(cropped_background)

    # Get the text size to center the numbers using bbox
    bbox = draw.textbbox((0, 0), formatted_label, font=font)  # Get bounding box of the formatted text
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text
    text_x = (cropped_background.width - text_width) // 2
    text_y = (cropped_background.height - text_height) // 2

    # Draw a shaded effect (shadow) under the number
    shadow_offset = 3  # Offset for the shadow effect
    draw.text((text_x + shadow_offset, text_y + shadow_offset), formatted_label, font=font,
              fill='black')  # Black shadow
    draw.text((text_x, text_y), formatted_label, font=font, fill='white')  # White number

    # Save the image with a unique name based on its number
    image_name = f"image_{i + 1}.png"
    image_path = os.path.join(images_dir, image_name)

    # Resize the image to a smaller size (optional)
    small_image = cropped_background.resize((300, 100), Image.LANCZOS)  # Resize to 350x100 pixels

    # Save the image with quality parameter for compression
    small_image.save(image_path, format='PNG', quality=85)  # Adjust quality for PNG

    # Save the label in a corresponding text file (without spaces)
    label_file_name = f"image_{i + 1}.txt"
    label_file_path = os.path.join(labels_dir, label_file_name)

    # Write the label (random number without spaces) to the label file
    with open(label_file_path, 'w') as label_file:
        label_file.write(label)

# Optionally show one of the images
small_image.show()
