from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .dataset import DatasetConfig, get_datasets
from .model import ModelConfig, create_model


@dataclass(frozen=True)
class TrainingConfig:
    data_dir: Path = Path("dataset")
    epochs: int = 10
    batch_size: int = 32
    image_size: tuple[int, int] = (600, 600)
    model_output: Path = Path("artifacts/model.keras")
    seed: int = 123


def train_model(config: TrainingConfig | None = None) -> dict[str, Any]:
    config = config or TrainingConfig()
    dataset_config = DatasetConfig(
        data_dir=config.data_dir,
        image_size=config.image_size,
        batch_size=config.batch_size,
        seed=config.seed,
    )
    train_ds, val_ds = get_datasets(dataset_config)

    model_config = ModelConfig(image_shape=(*config.image_size, 3))
    model = create_model(model_config)
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=config.epochs,
        verbose=2,
    )
    loss, accuracy = model.evaluate(val_ds, verbose=0)

    config.model_output.parent.mkdir(parents=True, exist_ok=True)
    model.save(config.model_output)

    return {
        "model_path": str(config.model_output),
        "validation_loss": float(loss),
        "validation_accuracy": float(accuracy),
        "history": history.history,
    }
