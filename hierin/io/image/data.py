import pathlib

import numpy as np


class ImageData:
    def __init__(self, rgb_matrix: np.ndarray, image_path: str):
        self.image_path: pathlib.Path = pathlib.Path(image_path)
        self.filename: str = self.image_path.stem
        self.rgb_matrix: np.ndarray = rgb_matrix
        self.avg_color: np.ndarray = rgb_matrix.mean(axis=(0, 1)).astype(np.uint8)
        # TODO - calculate the floor and ceil based
        # on the standard deviation for reduced outliers
        self.floor_avg_color: np.ndarray = rgb_matrix.min(axis=(0, 1))
        self.ceil_avg_color: np.ndarray = rgb_matrix.max(axis=(0, 1))
        # ----------------------------------------------
        self.height: int = rgb_matrix.shape[0]
        self.width: int = rgb_matrix.shape[1]
        self.channels: int = rgb_matrix.shape[2]

    def __str__(self):
        return (
            "IMAGE DATA:\n"
            + f"\timage_path: {self.image_path}\n"
            + f"\tfilename: {self.filename}\n"
            + f"\tavg_color: {self.avg_color}\n"
            + f"\tfloor_avg_color: {self.floor_avg_color}\n"
            + f"\tceil_avg_color: {self.ceil_avg_color}\n"
            + f"\twidth: {self.width}\n\t"
            + f"height: {self.height}\n\tchannels: {self.channels}"
        )
