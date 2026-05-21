from keras import layers, models

from .dataset import get_datasets

normalized_dataset, validation_dataset = get_datasets()


def create_model():
    model = models.Sequential(
        [
            layers.Input(shape=(600, 600, 3)),
            layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Conv2D(128, (3, 3), activation="relu", padding="same"),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation="relu"),
            layers.Dense(2, activation="softmax"),
        ]
    )
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


model = create_model()

history = model.fit(
    normalized_dataset,
    validation_data=validation_dataset,
    epochs=10,
    verbose=2,
)

test_loss, test_acc = model.evaluate(validation_dataset)
print(f"Test accuracy: {test_acc * 100:.2f}%")
