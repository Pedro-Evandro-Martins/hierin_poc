from hierin.io.image_loader import ImageData, ImageLoader


class HierINController:
    def __init__(self, image_path: str, depth: int = 0):
        self.payload = HierINPayload(image_path, depth)

    def process(self):
        image_data: ImageData = IOController.load_image(self.payload.image_path)
        print(image_data)

        parsed_image = ParsingController.parse(image_data, self.payload.depth)
        _ = parsed_image


class HierINPayload:
    def __init__(self, image_path: str, depth: int):
        self.image_path: str = image_path
        self.depth: int = depth


class IOController:
    @staticmethod
    def load_image(image_path: str):
        return ImageLoader(image_path).load_image()


class ParsingController:
    def __init__(self):
        pass

    @staticmethod
    def parse(image_data: ImageData, depth: int):
        pass


class ProcessingController:
    def __init__(self):
        pass

    def process(self):
        pass
