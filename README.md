# Film Color Simulator

Film Color Simulator is a lightweight Python tool for generating synthetic image datasets of pH-sensitive freshness indicator films. It creates controlled color variations from HSV profiles and includes a baseline CNN workflow for validating whether the simulated `fresh` and `altered` classes are learnable.

The project is intentionally focused: synthetic data generation, reproducible dataset creation, a simple computer vision baseline, and clean Python packaging.

## Why It Exists

Real lab image data for freshness indicator films can be limited or expensive to collect. This project explores a practical first step: generate controlled synthetic images, train a small baseline classifier, and document the limitations clearly before moving toward real-world validation.

## Features

- Generate synthetic `fresh` and `altered` film images from HSV color profiles.
- Configure image size, output directory, random seed, and variation count.
- Save Keras-compatible image folders.
- Train a compact CNN baseline.
- Evaluate a trained model with validation accuracy and a confusion matrix.
- Run fast unit and CLI smoke tests.

## Example Output

| Fresh | Altered |
| --- | --- |
| ![Fresh synthetic film sample](examples/sample_dataset/fresh/fresh_0_0.png) | ![Altered synthetic film sample](examples/sample_dataset/altered/altered_1_0.png) |

## Quickstart

```powershell
py -m pip install -e . --no-deps
py -m pip install numpy opencv-python Pillow pytest
```

Generate a small synthetic dataset:

```powershell
film-color generate --samples 20 --output dataset --image-size 128 --seed 123
```

Train the baseline classifier in an environment with TensorFlow installed:

```powershell
film-color train --data dataset --epochs 10 --model-output artifacts/model.keras
```

Evaluate the trained model:

```powershell
film-color evaluate --data dataset --model artifacts/model.keras --output artifacts/evaluation.json
```

## Project Structure

```text
src/film_color/
  cli.py          # command-line interface
  config.py       # generation configuration
  dataset.py      # TensorFlow dataset loading
  evaluation.py   # validation metrics and confusion matrix
  generator.py    # synthetic image generation
  model.py        # baseline CNN architecture
  profiles.py     # HSV color profiles
  training.py     # training workflow
tests/
  test_cli.py
  test_generator.py
  test_profiles.py
```

## Development

Run the fast test suite:

```powershell
py -m pytest
```

The tests cover HSV profile validity, generated image dimensions, deterministic metadata, class folder creation, and CLI smoke behavior.

## Limitations

This project uses synthetic images only. It does not model real lab lighting, camera sensors, film texture, sample handling, or environmental noise. A classifier trained only on these images should be treated as a prototype baseline, not a validated food safety system.

## Future Work

- Calibrate HSV profiles against real lab measurements.
- Add optional lighting and texture simulation.
- Train on a mix of synthetic and real images.
- Add a lightweight single-image prediction command.
