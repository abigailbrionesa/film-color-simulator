# Implementation Issues: Film Color Simulator

## Milestone 1: Structure and Packaging

### Issue 1: Restructure project into an installable Python package

**Goal:** Move the project from loose scripts into a clean `src/film_color/` package.

**Tasks**

- Create `src/film_color/`.
- Add `__init__.py`.
- Move reusable logic into package modules.
- Keep scripts importable without relying on the current working directory.

**Acceptance Criteria**

- Package modules can be imported with `import film_color`.
- No core module depends on relative execution from the repo root.
- Existing generation logic still works after the move.

---

### Issue 2: Add `pyproject.toml` and dependency metadata

**Goal:** Make the project installable and easier to run locally.

**Tasks**

- Add `pyproject.toml`.
- Define project name, Python version, dependencies, and CLI entrypoint.
- Move dependency list out of `docs/requirements.txt` or mirror it clearly.

**Acceptance Criteria**

- `pip install -e .` works.
- `film-color --help` is available after install.
- Dependencies include image generation and ML packages needed by the project.

---

### Issue 3: Create typed config objects for generation settings

**Goal:** Replace hard-coded generation constants with explicit configuration.

**Tasks**

- Add a generation config object or dataclass.
- Include image size, sample count, output directory, random seed, noise range, and class labels.
- Keep default values simple and documented.

**Acceptance Criteria**

- Generator can run with default config.
- Generator can run with caller-provided settings.
- Config values are type hinted.

---

## Milestone 2: Generator Workflow

### Issue 4: Implement configurable synthetic dataset generation

**Goal:** Generate `fresh` and `altered` image datasets from HSV color profiles.

**Tasks**

- Create `profiles.py` for HSV color profiles.
- Create `generator.py` for image generation.
- Save images into `dataset/fresh/` and `dataset/altered/`.
- Add hue, saturation, brightness, and noise variation.

**Acceptance Criteria**

- Running generation creates both class folders.
- Images are saved as PNG files.
- Generated images have the configured dimensions.
- Output is compatible with Keras image dataset loading.

---

### Issue 5: Add deterministic generation with random seed support

**Goal:** Make generated datasets reproducible for demos and tests.

**Tasks**

- Accept a random seed in generation config.
- Use a local random number generator instead of uncontrolled global randomness.
- Record generation metadata in the output directory.

**Acceptance Criteria**

- Same seed and config produce the same metadata and file count.
- Different seeds produce different color variations.
- Metadata includes seed, sample count, image size, and class labels.

---

### Issue 6: Add `film-color generate` CLI command

**Goal:** Provide a simple command for dataset generation.

**Tasks**

- Add `cli.py`.
- Implement `film-color generate`.
- Support `--samples`, `--output`, `--image-size`, and `--seed`.
- Print a concise summary after generation.

**Acceptance Criteria**

- `film-color generate --samples 20 --output dataset --seed 123` works.
- Command creates `dataset/fresh/` and `dataset/altered/`.
- CLI exits with a non-zero status for invalid arguments.

---

### Issue 7: Add example generated images

**Goal:** Make the repo visually understandable from the README.

**Tasks**

- Generate a small set of representative images.
- Save examples under `examples/`.
- Include at least one `fresh` and one `altered` image.

**Acceptance Criteria**

- Example images are committed or documented clearly.
- README can reference the images.
- Images demonstrate the intended color transition.

---

## Milestone 3: Baseline Model

### Issue 8: Implement dataset loading utilities

**Goal:** Centralize image dataset loading and normalization.

**Tasks**

- Create `dataset.py`.
- Load generated images from class folders.
- Apply consistent resizing and normalization.
- Support train/validation split.

**Acceptance Criteria**

- Dataset loader works with generated output.
- Class names are stable and documented.
- Images are normalized consistently before training.

---

### Issue 9: Implement small CNN baseline model

**Goal:** Provide a simple model that validates generated classes are learnable.

**Tasks**

- Create `model.py`.
- Define a compact CNN for binary classification.
- Compile with a sensible optimizer, loss, and metrics.
- Keep architecture intentionally simple.

**Acceptance Criteria**

- Model accepts configured image shape.
- Model trains on generated dataset without code changes.
- Architecture is small enough for quick local runs.

---

### Issue 10: Add `film-color train` CLI command

**Goal:** Train the baseline classifier from the command line.

**Tasks**

- Implement `film-color train`.
- Support `--data`, `--epochs`, `--batch-size`, and `--model-output`.
- Save trained model to `artifacts/model.keras`.
- Print train and validation accuracy.

**Acceptance Criteria**

- Training runs against a generated dataset.
- Model file is saved successfully.
- Command prints final metrics.

---

### Issue 11: Add evaluation metrics and confusion matrix output

**Goal:** Make model results easy to inspect and include in the README.

**Tasks**

- Create `evaluation.py`.
- Load a trained model and validation dataset.
- Compute accuracy and confusion matrix.
- Save metrics to `artifacts/evaluation.json`.

**Acceptance Criteria**

- Evaluation command outputs validation accuracy.
- `artifacts/evaluation.json` is created.
- Confusion matrix values are included in the saved metrics.

---

### Issue 12: Add `film-color evaluate` CLI command

**Goal:** Provide a complete generate/train/evaluate workflow.

**Tasks**

- Implement `film-color evaluate`.
- Support `--data`, `--model`, and `--output`.
- Print a concise evaluation summary.

**Acceptance Criteria**

- `film-color evaluate --data dataset --model artifacts/model.keras` works.
- Evaluation results are saved.
- CLI fails clearly if model or dataset path is missing.

---

## Milestone 4: Tests and Portfolio Polish

### Issue 13: Add unit tests for color profiles and generator

**Goal:** Prove the core generator logic is reliable.

**Tasks**

- Add `tests/test_profiles.py`.
- Add `tests/test_generator.py`.
- Test HSV values, image dimensions, class folders, and file counts.

**Acceptance Criteria**

- Tests pass locally with `pytest`.
- Tests avoid requiring TensorFlow unless needed.
- Temporary directories are used for generated files.

---

### Issue 14: Add CLI smoke tests

**Goal:** Verify the command-line experience works.

**Tasks**

- Test `film-color generate` with a small sample count.
- Verify output folders and files exist.
- Test invalid arguments where useful.

**Acceptance Criteria**

- CLI smoke test passes in CI.
- Test runtime stays short.
- Generated test files are isolated in temporary folders.

---

### Issue 15: Add GitHub Actions workflow

**Goal:** Show basic SWE hygiene with automated tests.

**Tasks**

- Add `.github/workflows/tests.yml`.
- Install package in editable mode.
- Run `pytest`.
- Use a current Python version.

**Acceptance Criteria**

- Workflow runs on push and pull request.
- Tests pass in GitHub Actions.
- Workflow avoids expensive model training.

---

### Issue 16: Rewrite README for SWE/AI portfolio positioning

**Goal:** Make the project clear and impressive in the first ten seconds.

**Tasks**

- Explain the project in one concise paragraph.
- Add quickstart commands.
- Add example output images.
- Add baseline model results section.
- Add limitations section.

**Acceptance Criteria**

- README communicates: synthetic data generator plus baseline classifier.
- Quickstart can be followed by a new user.
- Limitations avoid overclaiming real-world performance.

---

### Issue 17: Add concise results artifact for portfolio review

**Goal:** Give reviewers a fast way to see what the project achieved.

**Tasks**

- Add a short `docs/RESULTS.md`.
- Include dataset size, model config, validation accuracy, and confusion matrix.
- Include a note about synthetic-only limitations.

**Acceptance Criteria**

- Results are reproducible from documented commands.
- Metrics are easy to scan.
- Claims are modest and technically accurate.

---

## Backlog / Future Work

### Issue 18: Add lighting and texture simulation

**Goal:** Make synthetic images more realistic without overcomplicating the core project.

**Acceptance Criteria**

- Generator can optionally add lighting gradients or texture.
- Feature is disabled by default.
- README explains this is still synthetic-only.

---

### Issue 19: Calibrate profiles against real lab samples

**Goal:** Improve scientific grounding if real pH/color data becomes available.

**Acceptance Criteria**

- Profiles can be loaded from a small calibration file.
- Documentation explains the source of calibration data.
- Defaults still work without calibration data.

---

### Issue 20: Add lightweight inference command

**Goal:** Let users run prediction on one image.

**Tasks**

- Implement `film-color predict --image path --model artifacts/model.keras`.
- Print predicted class and confidence.

**Acceptance Criteria**

- Command works on generated sample images.
- Output is concise.
- README marks this as optional/future functionality.

