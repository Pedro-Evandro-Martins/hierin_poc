import os
import pathlib
from typing import List, Optional

from typer import BadParameter


class FileValidator:
    def __init__(
        self,
        allowed_formats: Optional[List[str]] = None,
        max_size_mb: Optional[int] = None,
    ):
        if allowed_formats:
            allowed_formats = [fmt.lower() for fmt in allowed_formats]
        self.allowed_formats = allowed_formats or ["jpg", "jpeg"]
        self.max_size_mb = max_size_mb

    def resolve(self, file_path: str) -> str:
        if not self._validate(file_path):
            raise BadParameter(f"File validation failed for {file_path}")

        abs_path = str(pathlib.Path(file_path).resolve())

        return abs_path

    def _validate(self, file_path: str) -> bool:
        is_file = os.path.isfile(file_path)
        if not is_file:
            raise BadParameter(f"The file {file_path} does not exist.")

        resolved_path = pathlib.Path(file_path).resolve()
        file_extension = resolved_path.suffix.lower().lstrip(".")

        if file_extension not in self.allowed_formats:
            raise BadParameter(
                f"Invalid file format: .{file_extension}. Allowed formats are: {
                    self.allowed_formats
                }"
            )

        if self.max_size_mb is not None:
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if file_size_mb > self.max_size_mb:
                raise BadParameter(
                    f"File size exceeds the maximum limit of {
                        self.max_size_mb}MB"
                )

        return True
