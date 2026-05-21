import random
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


def setup_directories(config: GenerationConfig | None = None) -> None:
    config = config or GenerationConfig()
    config.fresh_dir.mkdir(parents=True, exist_ok=True)
    config.altered_dir.mkdir(parents=True, exist_ok=True)


def generate_color_variations(
    base_color: Tuple[int, int, int],
    num_variations: int = NUM_VARIATIONS,
) -> List[Tuple[int, int, int]]:
    variations = []
    for _ in range(num_variations):
        h = np.clip(base_color[0] + random.randint(-5, 5), 0, 179)
        s = np.clip(base_color[1] + random.randint(-15, 15), 100, 255)
        v = np.clip(base_color[2] + random.randint(-15, 15), 180, 255)
        variations.append((h, s, v))
    return variations


def create_image(
    hsv_color: Tuple[int, int, int],
    size: Tuple[int, int] = IMAGE_SIZE,
    noise_range: Tuple[int, int] = NOISE_RANGE,
) -> Image.Image:
    bgr_color = cv2.cvtColor(np.uint8([[hsv_color]]), cv2.COLOR_HSV2BGR)[0][0]
    image = np.full((size[1], size[0], 3), bgr_color, dtype=np.uint8)

    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    noise = np.random.randint(noise_range[0], noise_range[1], hsv_img.shape, dtype=np.uint8)
    noisy_img = cv2.add(hsv_img, noise)
    rgb_img = cv2.cvtColor(noisy_img, cv2.COLOR_HSV2RGB)
    return Image.fromarray(rgb_img)


def generate_images(config: GenerationConfig | None = None) -> None:
    config = config or GenerationConfig()
    setup_directories(config)

    for i, base_color in enumerate(config.colors):
        is_fresh = base_color[0] >= config.fresh_threshold
        category = config.fresh_label if is_fresh else config.altered_label
        target_dir = config.fresh_dir if is_fresh else config.altered_dir
        variations = generate_color_variations(base_color, config.num_variations)
        for j, color in enumerate(variations):
            img = create_image(color, config.image_size, config.noise_range)
            filename = target_dir / f"{category}_{i}_{j}.png"
            img.save(filename, format="PNG", optimize=True)
            print(f"Imagen guardada: {filename}")


if __name__ == "__main__":
    generate_images()
