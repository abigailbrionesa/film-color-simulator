from pathlib import Path
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DatasetConfig:
    data_dir: Path = Path("dataset")
    image_size: tuple[int, int] = (600, 600)
    batch_size: int = 32
    validation_split: float = 0.2
    seed: int = 123


def _tensorflow() -> Any:
    import tensorflow as tf

    return tf


def load_dataset(config: DatasetConfig | None = None, subset: str = "training"):
    config = config or DatasetConfig()
    tf = _tensorflow()
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        config.data_dir,
        image_size=config.image_size,
        batch_size=config.batch_size,
        validation_split=config.validation_split,
        subset=subset,
        seed=config.seed,
    )
    return dataset


def normalize_dataset(dataset):
    tf = _tensorflow()

    def normalize(image, label):
        return tf.cast(image, tf.float32) / 255.0, label

    return dataset.map(normalize)


def get_datasets(config: DatasetConfig | None = None):
    config = config or DatasetConfig()
    train_ds = load_dataset(config, subset="training")
    val_ds = load_dataset(config, subset="validation")
    return normalize_dataset(train_ds), normalize_dataset(val_ds)
