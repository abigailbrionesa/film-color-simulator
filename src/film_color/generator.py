import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import cv2
import numpy as np
from PIL import Image

from .config import GenerationConfig
from .profiles import (
    IMAGE_SIZE,
    NOISE_RANGE,
    NUM_VARIATIONS,
)


@dataclass(frozen=True)
class GeneratedImage:
    path: Path
    label: str
    hsv_color: Tuple[int, int, int]


def setup_directories(config: GenerationConfig | None = None) -> None:
    config = config or GenerationConfig()
    config.fresh_dir.mkdir(parents=True, exist_ok=True)
    config.altered_dir.mkdir(parents=True, exist_ok=True)


def generate_color_variations(
    base_color: Tuple[int, int, int],
    num_variations: int = NUM_VARIATIONS,
    rng: random.Random | None = None,
) -> List[Tuple[int, int, int]]:
    rng = rng or random.Random()
    variations = []
    for _ in range(num_variations):
        h = int(np.clip(base_color[0] + rng.randint(-5, 5), 0, 179))
        s = int(np.clip(base_color[1] + rng.randint(-15, 15), 100, 255))
        v = int(np.clip(base_color[2] + rng.randint(-15, 15), 180, 255))
        variations.append((h, s, v))
    return variations


def create_image(
    hsv_color: Tuple[int, int, int],
    size: Tuple[int, int] = IMAGE_SIZE,
    noise_range: Tuple[int, int] = NOISE_RANGE,
    rng: np.random.Generator | None = None,
    enable_lighting: bool = False,
    enable_texture: bool = False,
) -> Image.Image:
    rng = rng or np.random.default_rng()
    bgr_color = cv2.cvtColor(np.uint8([[hsv_color]]), cv2.COLOR_HSV2BGR)[0][0]
    image = np.full((size[1], size[0], 3), bgr_color, dtype=np.uint8)

    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    noise = rng.integers(noise_range[0], noise_range[1], hsv_img.shape, dtype=np.uint8)
    noisy_img = cv2.add(hsv_img, noise)
    if enable_lighting:
        gradient = np.linspace(0.85, 1.08, size[0], dtype=np.float32)
        value = noisy_img[:, :, 2].astype(np.float32) * gradient[np.newaxis, :]
        noisy_img[:, :, 2] = np.clip(value, 0, 255).astype(np.uint8)
    if enable_texture:
        texture = rng.normal(0, 3, noisy_img[:, :, 2].shape)
        value = noisy_img[:, :, 2].astype(np.float32) + texture
        noisy_img[:, :, 2] = np.clip(value, 0, 255).astype(np.uint8)
    rgb_img = cv2.cvtColor(noisy_img, cv2.COLOR_HSV2RGB)
    return Image.fromarray(rgb_img)


def get_label_for_color(base_color: Tuple[int, int, int], config: GenerationConfig) -> str:
    return config.fresh_label if base_color[0] >= config.fresh_threshold else config.altered_label


def write_metadata(config: GenerationConfig, generated: list[GeneratedImage]) -> Path:
    metadata_path = config.output_dir / "metadata.json"
    metadata = {
        "random_seed": config.random_seed,
        "image_size": list(config.image_size),
        "num_variations": config.num_variations,
        "noise_range": list(config.noise_range),
        "fresh_threshold": config.fresh_threshold,
        "fresh_label": config.fresh_label,
        "altered_label": config.altered_label,
        "colors": [list(color) for color in config.colors],
        "generated_count": len(generated),
        "class_counts": {
            config.fresh_label: sum(item.label == config.fresh_label for item in generated),
            config.altered_label: sum(item.label == config.altered_label for item in generated),
        },
    }
    metadata_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return metadata_path


def generate_images(config: GenerationConfig | None = None) -> list[GeneratedImage]:
    config = config or GenerationConfig()
    setup_directories(config)
    generated: list[GeneratedImage] = []
    variation_rng = random.Random(config.random_seed)
    noise_rng = np.random.default_rng(config.random_seed)

    for i, base_color in enumerate(config.colors):
        category = get_label_for_color(base_color, config)
        target_dir = config.fresh_dir if category == config.fresh_label else config.altered_dir
        variations = generate_color_variations(base_color, config.num_variations, variation_rng)
        for j, color in enumerate(variations):
            img = create_image(
                color,
                config.image_size,
                config.noise_range,
                noise_rng,
                config.enable_lighting,
                config.enable_texture,
            )
            filename = target_dir / f"{category}_{i}_{j}.png"
            img.save(filename, format="PNG", optimize=True)
            generated.append(GeneratedImage(path=filename, label=category, hsv_color=color))
            print(f"Imagen guardada: {filename}")

    write_metadata(config, generated)
    return generated


if __name__ == "__main__":
    generate_images()
