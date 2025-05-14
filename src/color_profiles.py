from pathlib import Path
from typing import List, Tuple

IMAGE_SIZE = (600, 600)  # ancho, alto
NUM_VARIATIONS = 20      # variaciones por color
NOISE_RANGE = (0, 3)     # rango de ruido
FRESCO_THRESHOLD = 60    # colores con H ≥ 60 son frescos

DATASET_DIR = Path("dataset")
FRESCO_DIR = DATASET_DIR / "fresco"
ALTERADO_DIR = DATASET_DIR / "alterado"

COLORS: List[Tuple[int, int, int]] = [
    # ph bajo
    (150, 255, 255),  # fucsia
    (135, 255, 255),  # rosado
    (120, 255, 255),  # morado
    (100, 255, 255),  # púrpura
    # ph alto
    (85, 255, 255),   # violeta-azulado
    (70, 255, 255),   # celeste
    (50, 255, 255),   # verde-azulado
    (30, 255, 255),   # verde
    (15, 255, 255),   # verde-amarillento
]

