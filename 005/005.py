from PIL import Image
import os
import sys

# iphone5's resolving power: 1136*640

# the current path and list of dirs
root_dir = sys.path[0]
all_files = os.listdir(root_dir)
index = all_files.index('images')
image_dir = root_dir + '/' + all_files[index]
print(image_dir)

all_images = os.listdir(image_dir)
print(all_images)

for file in all_images:
    image = Image.open(image_dir + '/' + file)
    size = image.size
    width, height = size
    if height > 640:
        height = 640
    if width > 1136:
        width = 1136
    image.resize((width, height))
    image.save(file)

