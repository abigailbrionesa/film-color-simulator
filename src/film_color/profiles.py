from pathlib import Path
from typing import List, Tuple

IMAGE_SIZE = (600, 600)  # width, height
NUM_VARIATIONS = 20  # variations per color
NOISE_RANGE = (0, 3)  # noise range
FRESCO_THRESHOLD = 60  # colors with H >= 60 are fresh

DATASET_DIR = Path("dataset")
FRESCO_DIR = DATASET_DIR / "fresco"
ALTERADO_DIR = DATASET_DIR / "alterado"

COLORS: List[Tuple[int, int, int]] = [
    # low pH
    (150, 255, 255),  # fuchsia
    (135, 255, 255),  # pink
    (120, 255, 255),  # purple
    (100, 255, 255),  # violet
    # high pH
    (85, 255, 255),  # blue-violet
    (70, 255, 255),  # light blue
    (50, 255, 255),  # blue-green
    (30, 255, 255),  # green
    (15, 255, 255),  # yellow-green
]
