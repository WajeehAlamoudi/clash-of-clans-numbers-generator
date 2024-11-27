# CoC Number Generator
This project is designed to generate Clash of Clans (CoC) number images for the purpose of training models (e.g., OCR or deep learning models) to detect numbers in CoC screenshots. The repository contains scripts for cropping, resizing images, and adding labels (such as numbers) to the cropped images. The generated images and labels are saved in a structured way for easy access and further model training.
# Project Structure
```
coc_number_generator/
├── coc_image/                      # Original CoC background images
│   ├── image1.png                  # Example CoC background image
│   ├── image2.png                  # Example CoC background image
│   └── ...
│
├── coc_images_resized/             # Resized original CoC background images
│   ├── image1_resized.png          # Resized CoC image
│   ├── image2_resized.png          # Another resized CoC image
│   └── ...
│
├── coc_images_resized_crops/       # cropping small sizes of images
│   ├── image1_cropped.png          # Cropped and resized image
│   ├── image2_cropped.png          # Another cropped image
│   └── ...
│
├── numbers/                        # Genrated numbers with it's labels                 
│   └── images/
│        ├── image1.png
│    └── labels/
│        ├── image1.txt
│
└── Clash-Regular.ttf               # coc font 

```
# Description
This repository provides tools for creating a dataset of number images from Clash of Clans (CoC) backgrounds. It includes the following functionalities:
- Resizing the backgrounds images to unify the process.
- cropping a rectangls from each resized images.
- write on the cropped images random numbers to imitate coc numbers and store the image with it's labeled number.
- The number generator apply most effects thats are in the real game (shadow, spacing,..).

# How to Use the Project
- ensure downloading the backgrounds images folder.
- first run ```crop_from_resized_images.py``` be sure that folder is exist after runing the python file.
- run the next python file ```write_on_crop_images.py```

# Generated numbers usage
- you can train EasyOCR model to automate attacks searching:
https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md