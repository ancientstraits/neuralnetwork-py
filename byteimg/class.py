import numpy as np
from .util import parse_img


class ByteImg:
    """A class which facilitates the reading to and writing from
    a `byteimg` file."""

    width = 32
    height = 32

    buffer: np.array
    identifier: int | None

    def __init__(self, identifier=None):
        self.buffer = np.full((self.width, self.height), 0, dtype=np.uint8)
        self.identifier = identifier

    @classmethod
    def from_file(cls, filename):
        self = cls()
        self.buffer, self.identifier = parse_img(
            filename, self.width, self.height)
        return self

    def write(self, outfile):
        ...
