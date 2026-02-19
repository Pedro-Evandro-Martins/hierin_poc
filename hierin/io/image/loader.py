import numpy as np
from PIL import Image

from hierin.io import ImageData


class ImageLoader:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def load_image(self) -> ImageData:
        image = Image.open(self.image_path).convert("RGB")
        rgb_matrix = np.array(image)

        return ImageData(rgb_matrix, self.image_path)
