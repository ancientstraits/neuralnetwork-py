import numpy as np


def parse_img(filename: str, width: int,
              height: int) -> (np.array, int | None):
    """returns the data of an image"""

    f = open(filename, 'rb')

    data = f.read(width * height)
    buffer = np.frombuffer(data, dtype=np.uint8)

    ident_byte = f.read(1)
    if ident_byte == b'':
        identifier = None
    else:
        identifier = int.from_bytes(f.read(1), 'little')

    f.close()
    return buffer, identifier
