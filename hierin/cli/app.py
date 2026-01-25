from typing import Annotated

import typer

from hierin.cli.controllers import HierINController
from hierin.cli.validators import FileValidator

app = typer.Typer(
    help="HierIN POC CLI", add_completion=False, pretty_exceptions_short=True
)

file_validator = FileValidator(allowed_formats=["jpg", "jpeg"], max_size_mb=15)


@app.command()
def main(
    image_path: Annotated[
        str,
        typer.Option(
            "--image",
            "-i",
            help="A filepath of the target image file",
            callback=file_validator.resolve,
        ),
    ],
):
    controller = HierINController(image_path=image_path)
    _ = controller.process()
