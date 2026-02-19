from typing import Optional

from hierin.io import ImageData, TargetsData
from hierin.parsing import InstructionSetBuilder


class Parser:
    @staticmethod
    def parse(
        image: ImageData, base_depth: int = 0, targets: Optional[TargetsData] = None
    ):
        instruction_set_builder = InstructionSetBuilder()

        instruction_set = (
            instruction_set_builder.with_base_depth(base_depth)
            .with_targets(targets.targets_list if targets else None)
            .build()
        )

        # TODO

        return None
