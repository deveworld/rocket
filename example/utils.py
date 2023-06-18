from io import TextIOWrapper
import os
from pathlib import Path
from typing import Optional

from sympy import Float


class FileUtils:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        os.makedirs(self.filepath.parent.absolute(), exist_ok=True)
        self.f: Optional[TextIOWrapper] = None

    def open(self):
        self.f = open(self.filepath, 'wb+')
        self.f.write("time,acceleration,velocity,height,mass\n".encode('utf-8'))

    def close(self):
        self.f.close()

    def file_callback(self, time: Float, acceleration: Float, velocity: Float, height: Float, mass: Float):
        self.f.write(f"{time},{acceleration},{velocity},{height},{mass}\n".encode('utf-8'))