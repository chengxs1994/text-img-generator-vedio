import os
from PIL import Image
import numpy


def preprocess_pics(pics_dir, width=None, height=None):
    list_of_images = []

    for image_file in os.listdir(pics_dir):
        if image_file.endswith('.png') or image_file.endswith('.jpg'):
            image_path = os.path.join(pics_dir, image_file)
            image = Image.open(image_path)

            image_width, image_height = image.size
            if width is None:
                width = image_width
            if height is None:
                height = image_height

            if width != image_width or height != image_height:
                image = image.resize((width, height), Image.LANCZOS)

            shp = numpy.array(image).shape
            if len(shp) == 3 and shp[-1] == 3:
                list_of_images.append(image)

    return list_of_images


def adjust(pics_prompt, width=None, height=None):
    input_dir = './input/pics/' + pics_prompt.replace(' ', '_')
    output_dir = './output/pics/' + pics_prompt.replace(' ', '_')

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_dir, filename)
            img = Image.open(image_path)

            if img.mode != 'RGB':
                img = img.convert('RGB')

            image_width, image_height = img.size
            if width is None:
                width = image_width
            if height is None:
                height = image_height

            img_resized = img.resize((width, height), Image.LANCZOS)

            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)
