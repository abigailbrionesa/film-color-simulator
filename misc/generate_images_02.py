import numpy as np
import cv2
from PIL import Image
import os

fresco_dir = "dataset/fresco"
alterado_dir = "dataset/alterado"

def generar_imagenes():
    ancho, alto = 600, 600 
    colores = [
    (150, 255, 255),  # fucsia
    (120, 255, 255),  # morado
    (100, 255, 255),  # púrpura
    (70, 255, 255),   # celeste
    (30, 255, 255),   # verde

    ]

    for i, color in enumerate(colores):
        # HSV a BGR
        color_bgr = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2BGR)[0][0]
        # con fondo de ese color
        imagen = np.full((alto, ancho, 3), color_bgr, dtype=np.uint8)
        # a formato PIL
        pil_image = Image.fromarray(imagen)
        # + ruido para simular variaciones
        pil_image = pil_image.convert("HSV")
        np_image = np.array(pil_image)
        np_image = np_image + np.random.randint(0, 2, np_image.shape, dtype=np.uint8)
        np_image = np.clip(np_image, 0, 255)

        pil_image = Image.fromarray(np_image, "HSV")
        pil_image = pil_image.convert("RGB")

        # guardar imagen
        if i <= 2:  # "fresco" = fucsia a púrpura
            filename = os.path.join(fresco_dir, f"fresco_{i}.png")
            pil_image.save(filename)
        else:  # "alterado" = celeste a verde
            filename = os.path.join(alterado_dir, f"alterado_{i}.png")
            pil_image.save(filename)
        
        print(f"Imagen guardada como: {filename}")

generar_imagenes()
