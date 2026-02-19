from typing import Optional

from hierin.io import ImageData, ImageLoader, TargetsData, TargetsLoader
from hierin.parsing import Parser


class HierINController:
    def __init__(
        self, image_path: str, targets_path: Optional[str] = None, base_depth: int = 0
    ):
        self.payload = HierINPayload(image_path, targets_path, base_depth)

    def process(self):
        image_data: ImageData = IOController.load_image(self.payload.image_path)

        targets_data: Optional[TargetsData] = None
        if self.payload.targets_path:
            targets_data = IOController.load_targets_list(self.payload.targets_path)

        print(image_data)

        parsed = ParsingController.parse(
            image_data, self.payload.base_depth, targets_data
        )

        pass


class HierINPayload:
    def __init__(self, image_path: str, targets: Optional[str], base_depth: int):
        self.image_path: str = image_path
        self.targets_path: Optional[str] = targets
        self.base_depth: int = base_depth


class IOController:
    @staticmethod
    def load_image(image_path: str) -> ImageData:
        return ImageLoader(image_path).load_image()

    @staticmethod
    def load_targets_list(targets_path: str) -> TargetsData:
        return TargetsLoader(targets_path).load_targets_list()


class ParsingController:
    @staticmethod
    def parse(image_data: ImageData, base_depth: int, targets: Optional[TargetsData]):
        parsed = Parser.parse(image_data, base_depth, targets)

        pass


class ProcessingController:
    def process(self):
        pass
