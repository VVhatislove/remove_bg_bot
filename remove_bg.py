from rembg.bg import remove
import numpy as np
import io
from PIL import Image, ImageFile
import os


async def remove_background(file_name):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    png_name = os.path.splitext(file_name)[0] + '.png'
    input_path = './original_photos/' + file_name
    output_path = './no_bg_photos/' + png_name

    f = np.fromfile(input_path)
    result = remove(f)
    img = Image.open(io.BytesIO(result)).convert("RGBA")
    img.save(output_path)
    print('remove_bg')
    return png_name
