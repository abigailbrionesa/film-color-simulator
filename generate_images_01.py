import cv2
import numpy as np

img_fresh = np.full((300, 300, 3), (255, 0, 255), dtype=np.uint8)
cv2.imwrite("fresco_1.jpg", img_fresh)

img_fermentado = np.full((300, 300, 3), (0, 255, 0), dtype=np.uint8)
cv2.imwrite("fermentado_1.jpg", img_fermentado)
