import numpy as np
import cv2
from PIL import Image
from pathlib import Path
from typing import List, Tuple
import random
from color_profiles import ( 
    IMAGE_SIZE,
    NUM_VARIATIONS,
    NOISE_RANGE,
    FRESCO_DIR,
    ALTERADO_DIR,
    COLORS,
    FRESCO_THRESHOLD
)

# crear folderes si no existen
def setup_directories() -> None:
    FRESCO_DIR.mkdir(parents=True, exist_ok=True)
    ALTERADO_DIR.mkdir(parents=True, exist_ok=True)

def generate_color_variations(base_color: Tuple[int, int, int], 
                            num_variations: int = NUM_VARIATIONS) -> List[Tuple[int, int, int]]:
    variations = []
    for _ in range(num_variations):
        h = np.clip(base_color[0] + random.randint(-5, 5), 0, 179)
        s = np.clip(base_color[1] + random.randint(-15, 15), 100, 255)
        v = np.clip(base_color[2] + random.randint(-15, 15), 180, 255)
        variations.append((h, s, v))
    return variations

def create_image(hsv_color: Tuple[int, int, int], 
                size: Tuple[int, int] = IMAGE_SIZE) -> Image.Image:
    # HSV a BGR para OpenCV
    bgr_color = cv2.cvtColor(np.uint8([[hsv_color]]), cv2.COLOR_HSV2BGR)[0][0]
    # imagen base
    image = np.full((size[1], size[0], 3), bgr_color, dtype=np.uint8)
    # añadir ruido
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    noise = np.random.randint(NOISE_RANGE[0], NOISE_RANGE[1], hsv_img.shape, dtype=np.uint8)
    noisy_img = cv2.add(hsv_img, noise)
    rgb_img = cv2.cvtColor(noisy_img, cv2.COLOR_HSV2RGB)
    return Image.fromarray(rgb_img)

def generate_images() -> None:
    setup_directories()
    
    for i, base_color in enumerate(COLORS):
        category = "fresco" if base_color[0] >= FRESCO_THRESHOLD else "alterado"
        target_dir = FRESCO_DIR if category == "fresco" else ALTERADO_DIR
        variations = generate_color_variations(base_color, NUM_VARIATIONS)
        for j, color in enumerate(variations):
            img = create_image(color, IMAGE_SIZE)
            filename = target_dir / f"{category}_{i}_{j}.png"
            img.save(filename, format='PNG', optimize=True)
            print(f"Imagen guardada: {filename}")

if __name__ == "__main__":
    generate_images()