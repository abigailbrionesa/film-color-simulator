from pathlib import Path

import cv2
import numpy as np


class ColorExtractor:
    def __init__(self):
        self.color_space = "LAB"
        self.num_colors = 1
        self.conversion_to = cv2.COLOR_BGR2LAB

    def get_dominant_color(self, image_path):
        img = cv2.imread(str(image_path))
        if img is None:
            raise ValueError(f"no se pudo leer la imagen: {image_path}")

        lab_img = cv2.cvtColor(img, self.conversion_to)
        lab_img = cv2.resize(lab_img, (100, 100), interpolation=cv2.INTER_AREA)
        pixel_values = lab_img.reshape((-1, 3)).astype(np.float32)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(
            pixel_values,
            self.num_colors,
            None,
            criteria,
            10,
            cv2.KMEANS_RANDOM_CENTERS,
        )
        dominant_color = centers[0].astype(np.uint8)
        return dominant_color

    def analyze_dataset(self, dataset_dir, max_images=None):
        dataset_dir = Path(dataset_dir)
        image_paths = list(dataset_dir.glob("*.png")) + list(dataset_dir.glob("*.jpg"))

        if max_images:
            image_paths = image_paths[:max_images]

        stats = {
            "l_values": [],
            "a_values": [],
            "b_values": [],
            "dominant_colors": [],
        }

        for img_path in image_paths:
            color = self.get_dominant_color(img_path)
            stats["l_values"].append(color[0])
            stats["a_values"].append(color[1])
            stats["b_values"].append(color[2])
            stats["dominant_colors"].append(tuple(color))

        return stats
