import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from .dataset import DatasetConfig, load_dataset, normalize_dataset


@dataclass(frozen=True)
class EvaluationConfig:
    data_dir: Path = Path("dataset")
    model_path: Path = Path("artifacts/model.keras")
    output_path: Path = Path("artifacts/evaluation.json")
    image_size: tuple[int, int] = (600, 600)
    batch_size: int = 32
    seed: int = 123


def _tensorflow() -> Any:
    import tensorflow as tf

    return tf


def evaluate_model(config: EvaluationConfig | None = None) -> dict[str, Any]:
    config = config or EvaluationConfig()
    tf = _tensorflow()

    dataset_config = DatasetConfig(
        data_dir=config.data_dir,
        image_size=config.image_size,
        batch_size=config.batch_size,
        seed=config.seed,
    )
    validation_ds = normalize_dataset(load_dataset(dataset_config, subset="validation"))
    model = tf.keras.models.load_model(config.model_path)

    true_labels: list[int] = []
    predicted_labels: list[int] = []
    for images, labels in validation_ds:
        predictions = model.predict(images, verbose=0)
        true_labels.extend(labels.numpy().astype(int).tolist())
        predicted_labels.extend(np.argmax(predictions, axis=1).astype(int).tolist())

    num_classes = max(true_labels + predicted_labels, default=-1) + 1
    confusion = np.zeros((num_classes, num_classes), dtype=int)
    for actual, predicted in zip(true_labels, predicted_labels):
        confusion[actual, predicted] += 1

    accuracy = float(np.mean(np.array(true_labels) == np.array(predicted_labels))) if true_labels else 0.0
    metrics = {
        "model_path": str(config.model_path),
        "data_dir": str(config.data_dir),
        "validation_accuracy": accuracy,
        "confusion_matrix": confusion.tolist(),
        "num_examples": len(true_labels),
    }

    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    config.output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics
