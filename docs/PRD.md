# Product Requirements Document: Film Color Simulator

## Overview

Film Color Simulator is a lightweight Python tool for generating synthetic image datasets of pH-sensitive freshness indicator films. The project simulates controlled color transitions from fresh to altered states and includes a simple baseline classifier to validate whether the generated classes are learnable.

This project should remain a focused supporting portfolio project. Its purpose is to demonstrate practical ML engineering fundamentals: synthetic data generation, reproducible dataset creation, baseline computer vision training, and clean Python packaging.

## Problem

Real lab image data for pH-sensitive freshness films can be limited, expensive, or difficult to collect consistently. A synthetic generator can help prototype classification workflows before real-world data is available.

The current project shows the core idea, but it needs stronger structure and presentation to read as a polished SWE and applied-AI project.

## Goals

- Generate synthetic `fresh` and `altered` film images from configurable HSV color profiles.
- Provide a simple command-line workflow for dataset generation, model training, and evaluation.
- Train a baseline CNN classifier to validate that generated color profiles are separable.
- Document the project clearly enough that someone can clone and run it in under five minutes.
- Add basic engineering polish: package layout, type hints, tests, and CI.

## Non-Goals

- Building a production ML platform.
- Deploying cloud infrastructure.
- Adding a complex web application.
- Claiming synthetic data generalizes to real lab images without validation.
- Implementing advanced experiment tracking, monitoring, or MLOps workflows.

## Target Users

- Recruiters and engineers reviewing the project as part of a SWE/AI portfolio.
- Students or researchers prototyping freshness-indicator image classification.
- Developers who want a small example of synthetic data generation for computer vision.

## Core User Story

As a developer, I want to clone the repo, generate a synthetic dataset, train a baseline classifier, and inspect evaluation results so I can understand the full applied-ML workflow quickly.

## Functional Requirements

### Dataset Generation

- Generate PNG images for two classes: `fresh` and `altered`.
- Use HSV color profiles to define pH-inspired color ranges.
- Add controlled variation in hue, saturation, brightness, and noise.
- Save images into a folder structure compatible with Keras image datasets:

```text
dataset/
  fresh/
  altered/
```

- Allow sample count, output directory, image size, and random seed to be configured.

### CLI

The project should expose three primary commands:

```bash
film-color generate --samples 500 --output dataset
film-color train --data dataset --epochs 10
film-color evaluate --data dataset --model artifacts/model.keras
```

### Model Training

- Train a small CNN baseline for binary classification.
- Normalize images consistently.
- Use a validation split.
- Save the trained model to an `artifacts/` directory.
- Print training and validation accuracy.

### Evaluation

- Report validation accuracy.
- Generate a confusion matrix.
- Save evaluation output to `artifacts/evaluation.json`.
- Optionally save a confusion matrix image to `artifacts/confusion_matrix.png`.

### Documentation

The README should explain:

- What the project does.
- Why synthetic data is useful here.
- Quickstart commands.
- Example generated images.
- Baseline model results.
- Limitations of synthetic-only data.

## Suggested Repository Structure

```text
film-color-simulator/
  src/
    film_color/
      __init__.py
      cli.py
      profiles.py
      generator.py
      dataset.py
      model.py
      evaluation.py
  tests/
    test_profiles.py
    test_generator.py
  docs/
    PRD.md
  examples/
  pyproject.toml
  README.md
```

## Success Metrics

- A new user can run the full workflow in under five minutes.
- The generator produces deterministic output when given a fixed seed.
- Tests pass in CI.
- README clearly communicates the project in the first ten seconds.
- Baseline classifier produces measurable validation results.

## Technical Requirements

- Python 3.10 or newer.
- Use `numpy`, `opencv-python`, `Pillow`, and TensorFlow/Keras.
- Use a `pyproject.toml` for packaging.
- Keep functions small, typed, and testable.
- Avoid hidden global state where possible.
- Use structured config values instead of hard-coded constants inside scripts.

## Testing Requirements

Minimum useful tests:

- Color profiles return valid HSV values.
- Generated images have the expected dimensions and mode.
- Dataset generation creates the expected class folders.
- Fixed random seed produces repeatable output metadata.
- CLI smoke test for `generate`.

## Risks and Limitations

- Synthetic images may be too simple and produce inflated model accuracy.
- Real-world lighting, camera sensors, film texture, and lab conditions are not modeled.
- A classifier trained only on synthetic data should not be presented as production-ready.
- The project should be framed as a prototype and learning tool, not a validated food safety system.

## Milestones

### Milestone 1: Structure and Packaging

- Move scripts into `src/film_color/`.
- Add `pyproject.toml`.
- Add importable modules and CLI entrypoint.

### Milestone 2: Generator Workflow

- Implement configurable dataset generation.
- Add reproducible random seed support.
- Add sample output images.

### Milestone 3: Baseline Model

- Add training command.
- Save trained model.
- Add evaluation command and metrics output.

### Milestone 4: Portfolio Polish

- Rewrite README.
- Add tests.
- Add GitHub Actions.
- Add concise limitations and future work sections.

## Future Work

- Calibrate color profiles against real lab measurements.
- Add lighting and texture simulation.
- Train on mixed synthetic and real images.
- Add a small notebook for visual exploration.
- Export the classifier for lightweight inference.

