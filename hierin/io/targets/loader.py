import json
from typing import Callable

from hierin.io import TargetsData


class TargetsLoader:
    def __init__(self, targets_path: str, extension: str = "json"):
        self.targets_path: str = targets_path
        self.extension: str = extension

    def load_targets_list(self) -> TargetsData:
        load: Callable = self._get_file_loader_callback()
        targets_list = load()

        return TargetsData(targets_list)

    def _get_file_loader_callback(self) -> Callable:
        if self.extension == "json":
            return self.__from_json
        else:
            raise ValueError(f"[ERROR] Unsupported file extension: {self.extension}")

    def __from_json(self, targets_path: str) -> TargetsData:
        with open(targets_path, "r") as file:
            try:
                config = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"[ERROR] error while decoding JSON from {targets_path}: {e}"
                )

        target = config.get("target")
        paths = target.get("paths") if target else None

        targets = []
        if paths:
            for path in paths:
                try:
                    route_stack = []
                    values = path.strip().split(">").map(lambda x: int(x.strip()))
                    for value in values:
                        route_stack.insert(0, value)

                    targets.append(route_stack)
                except Exception as e:
                    raise ValueError(
                        f"[ERROR] error while parsing targets json file: {e}"
                    )
        else:
            raise ValueError(
                f"[ERROR] Missing 'paths' in target configuration in {targets_path}"
            )

        targets_data: TargetsData = TargetsData(targets)
        return targets_data
