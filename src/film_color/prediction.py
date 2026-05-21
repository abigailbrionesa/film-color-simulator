from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


@dataclass(frozen=True)
class PredictionConfig:
    image_path: Path
    model_path: Path = Path("artifacts/model.keras")
    image_size: tuple[int, int] = (600, 600)
    class_names: tuple[str, str] = ("altered", "fresh")


def _tensorflow() -> Any:
    import tensorflow as tf

    return tf


def load_image_array(path: Path, image_size: tuple[int, int]) -> np.ndarray:
    image = Image.open(path).convert("RGB").resize(image_size)
    array = np.asarray(image, dtype=np.float32) / 255.0
    return np.expand_dims(array, axis=0)


def predict_image(config: PredictionConfig) -> dict[str, Any]:
    tf = _tensorflow()
    model = tf.keras.models.load_model(config.model_path)
    batch = load_image_array(config.image_path, config.image_size)
    predictions = model.predict(batch, verbose=0)[0]
    class_index = int(np.argmax(predictions))
    confidence = float(predictions[class_index])
    class_name = config.class_names[class_index]

    return {
        "image_path": str(config.image_path),
        "model_path": str(config.model_path),
        "predicted_class": class_name,
        "confidence": confidence,
    }
