from typing import List, Optional, Self

from hierin.algorithms import HierIN
from hierin.io import ImageData


class InstructionSet:
    def __init__(self, base_depth: int, targets: Optional[List[int]]):
        self.base_depth: int = base_depth
        self.targets: List[int] = targets if targets else []

    def call_hierin(self, image_data: ImageData) -> HierIN:
        return HierIN()


class InstructionSetBuilder:
    def __init__(self):
        self.__base_depth: Optional[int] = None
        self.__targets: Optional[List[int]] = None

    def with_base_depth(self, base_depth: int) -> Self:
        self.__base_depth = base_depth
        return self

    def with_targets(self, targets: Optional[List[int]]) -> Self:
        self.__targets = targets
        return self

    def build(self) -> InstructionSet:
        if self.__base_depth is None:
            raise ValueError(
                "[ERROR] Base depth must be set before building the instruction set."
            )

        return InstructionSet(self.__base_depth, self.__targets)

    # IntructionSetBuilder can be extended with more methods to set other parameters as needed.
