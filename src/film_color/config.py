from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Tuple

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
    enable_lighting: bool = False
    enable_texture: bool = False
    colors: Tuple[Tuple[int, int, int], ...] = field(default_factory=lambda: tuple(COLORS))

    @property
    def fresh_dir(self) -> Path:
        return self.output_dir / self.fresh_label

    @property
    def altered_dir(self) -> Path:
        return self.output_dir / self.altered_label

    @classmethod
    def from_calibration_file(cls, path: Path, **kwargs: Any) -> "GenerationConfig":
        from .calibration import load_calibrated_colors

        return cls(colors=load_calibrated_colors(path), **kwargs)
