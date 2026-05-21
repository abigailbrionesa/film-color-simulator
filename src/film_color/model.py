from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    image_shape: tuple[int, int, int] = (600, 600, 3)
    num_classes: int = 2
    learning_rate: float = 0.001


def create_model(config: ModelConfig | None = None):
    config = config or ModelConfig()

    from tensorflow.keras import layers, models, optimizers

    model = models.Sequential(
        [
            layers.Input(shape=config.image_shape),
            layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Conv2D(128, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation="relu"),
            layers.Dense(config.num_classes, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=optimizers.Adam(learning_rate=config.learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model
