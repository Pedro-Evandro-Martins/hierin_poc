from typing import Annotated

import typer

from hierin.cli.controllers import HierINController
from hierin.cli.validators import FileValidator

app = typer.Typer(
    help="HierIN POC CLI", add_completion=False, pretty_exceptions_short=True
)

image_validator = FileValidator(allowed_formats=["jpg", "jpeg"], max_size_mb=15)
target_validator = FileValidator(allowed_formats=["json"])


@app.command()
def main(
    image_path: Annotated[
        str,
        typer.Option(
            "--image",
            "-i",
            help="A filepath of the target image file",
            callback=image_validator.resolve,
        ),
    ],
    target_path: Annotated[
        str,
        typer.Option(
            "--targets",
            "-t",
            help="A filepath of the json targets configuration file",
            callback=target_validator.resolve,
        ),
    ],
):
    controller = HierINController(image_path=image_path, targets_path=target_path)
    _ = controller.process()
