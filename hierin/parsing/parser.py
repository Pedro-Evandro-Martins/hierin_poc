from typing import Optional

from hierin.algorithms import HierINProcessor
from hierin.io import ImageData, TargetsData
from hierin.parsing import InstructionSet, InstructionSetBuilder


class Parser:
    @staticmethod
    def parse_processor(
        image: ImageData, base_depth: int = 0, targets: Optional[TargetsData] = None
    ) -> HierINProcessor:
        instruction_set_builder = InstructionSetBuilder()

        instruction_set: InstructionSet = (
            instruction_set_builder.with_base_depth(base_depth)
            .with_targets(targets.targets_list if targets else None)
            .build()
        )

        # TODO

        return HierINProcessor()
