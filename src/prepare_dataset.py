import tensorflow as tf
from pathlib import Path

DATASET_DIR = Path("dataset")
FRESCO_DIR = DATASET_DIR / "fresco"
ALTERADO_DIR = DATASET_DIR / "alterado"

IMAGE_SIZE = (600, 600)
BATCH_SIZE = 32

def load_dataset():
    # cada carpeta se etiqueta con el nombre de la carpeta: "fresco" o "alterado"
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        DATASET_DIR,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        validation_split=0.2,
        subset="training", 
        seed=123
    )
    return dataset

def normalize_dataset(dataset):
    def normalize(image, label):
        return tf.cast(image, tf.float32) / 255.0, label
    return dataset.map(normalize)


def get_datasets():
    train_ds = load_dataset()
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        DATASET_DIR,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        validation_split=0.2,
        subset="validation", 
        seed=123
    )
    return normalize_dataset(train_ds), normalize_dataset(val_ds)