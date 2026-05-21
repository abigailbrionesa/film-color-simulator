from dataclasses import dataclass, field
from pathlib import Path
from typing import Tuple

from .profiles import COLORS


@dataclass(frozen=True)
class GenerationConfig:
    image_size: Tuple[int, int] = (600, 600)
    num_variations: int = 20
    noise_range: Tuple[int, int] = (0, 3)
    fresh_threshold: int = 60
    output_dir: Path = Path("dataset")
    fresh_label: str = "fresh"
    altered_label: str = "altered"
    random_seed: int | None = None
    colors: Tuple[Tuple[int, int, int], ...] = field(default_factory=lambda: tuple(COLORS))

    @property
    def fresh_dir(self) -> Path:
        return self.output_dir / self.fresh_label

    @property
    def altered_dir(self) -> Path:
        return self.output_dir / self.altered_label
