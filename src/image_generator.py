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
        # Pequeñas variaciones en matiz, saturación y valor
        variation = (
            base_color[0] + random.randint(-5, 5),
            base_color[1] + random.randint(-10, 10),
            base_color[2] + random.randint(-10, 10)
        )
        # valores en rangos válidos
        variation = (
            np.clip(variation[0], 0, 179),
            np.clip(variation[1], 100, 255),
            np.clip(variation[2], 200, 255)
        )
        variations.append(variation)
    return variations

def create_image(hsv_color: Tuple[int, int, int], 
                size: Tuple[int, int] = IMAGE_SIZE) -> Image.Image:
    # HSV a BGR para OpenCV
    color_bgr = cv2.cvtColor(np.uint8([[hsv_color]]), cv2.COLOR_HSV2BGR)[0][0]
    # imagen base
    image = np.full((size[1], size[0], 3), color_bgr, dtype=np.uint8)
    # a PIL y añadir variaciones
    pil_image = Image.fromarray(image).convert('HSV')
    np_image = np.array(pil_image)
    # añadir ruido
    noise = np.random.randint(NOISE_RANGE[0], NOISE_RANGE[1], np_image.shape, dtype=np.uint8)
    np_image = np.clip(np_image + noise, 0, 255)
    return Image.fromarray(np_image, 'HSV').convert('RGB')

def generate_images() -> None:
    setup_directories()
    
    for i, base_color in enumerate(COLORS):
        if base_color[0] >= FRESCO_THRESHOLD:  # es fresco de fucsia a púrpura
            category = "fresco"
            directory = FRESCO_DIR
        else:  # es alterado de celeste a verde-amarillento
            category = "alterado"
            directory = ALTERADO_DIR
        
        # generar variaciones
        color_variations = generate_color_variations(base_color)
        
        for variation_idx, color in enumerate(color_variations):
            img = create_image(color)
            filename = directory / f"{category}_{i}_{variation_idx}.png"
            img.save(filename, optimize=True, quality=95)
            
            print(f"Imagen generada: {filename}")

if __name__ == "__main__":
    generate_images()