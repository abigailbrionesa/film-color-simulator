# Plan: Issue 1 - Restructure Project Into an Installable Python Package

## Summary

Move the current loose Python scripts under `src/` into a proper importable package at `src/film_color/` while preserving the existing behavior. This issue should only handle package structure and import correctness; CLI, packaging metadata, configs, tests, and model improvements belong to later issues.

## User Story

As a developer reviewing the project,
I want the source code organized as a Python package,
So that the project reads like maintainable SWE/AI work instead of standalone scripts.

## Metadata

| Field | Value |
|-------|-------|
| Type | REFACTOR |
| Complexity | LOW |
| Systems Affected | Python source layout, imports |
| Issue | Issue 1 from `docs/ISSUES.md` |

---

## Current Codebase Patterns

### Source Files

Current reusable code lives directly under `src/`:

```text
src/color_profiles.py
src/image_generator.py
src/prepare_dataset.py
src/train_model.py
src/color_extractor_class.py
src/color_extractor_main.py
```

### Imports

Modules currently import siblings as top-level scripts:

```python
# src/image_generator.py
from color_profiles import (
    IMAGE_SIZE,
    NUM_VARIATIONS,
    NOISE_RANGE,
    FRESCO_DIR,
    ALTERADO_DIR,
    COLORS,
    FRESCO_THRESHOLD
)
```

```python
# src/train_model.py
from prepare_dataset import get_datasets
```

```python
# src/color_extractor_main.py
from color_extractor_class import ColorExtractor
```

These imports will break after moving files unless converted to package-relative imports.

### Script Entrypoints

Two files have direct script behavior:

```python
# src/image_generator.py
if __name__ == "__main__":
    generate_images()
```

```python
# src/color_extractor_main.py
if __name__ == "__main__":
    ...
```

`train_model.py` currently trains at import time because the training code is top-level. For Issue 1, preserve behavior but avoid importing it from `__init__.py`.

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `src/film_color/__init__.py` | CREATE | Mark package and expose basic metadata |
| `src/film_color/profiles.py` | CREATE | New package location for color profile constants |
| `src/film_color/generator.py` | CREATE | New package location for image generation |
| `src/film_color/dataset.py` | CREATE | New package location for dataset loading |
| `src/film_color/model.py` | CREATE | New package location for baseline model training |
| `src/film_color/color_extractor.py` | CREATE | New package location for color extraction utility |
| `src/film_color/color_extractor_main.py` | CREATE | Optional script-style analyzer module |
| old `src/*.py` files | DELETE | Remove loose duplicate modules after package move |

---

## Implementation Tasks

### Task 1: Create package directory

- **File**: `src/film_color/__init__.py`
- **Action**: CREATE
- **Implement**:
  - Add a short package docstring.
  - Add `__all__ = []` or minimal exports.
  - Do not import TensorFlow or heavy modules here.
- **Validate**:
  - `python -c "import sys; sys.path.insert(0, 'src'); import film_color; print(film_color.__name__)"`

### Task 2: Move color profile constants

- **File**: `src/film_color/profiles.py`
- **Action**: CREATE from `src/color_profiles.py`
- **Implement**:
  - Preserve constants for now: `IMAGE_SIZE`, `NUM_VARIATIONS`, `NOISE_RANGE`, `FRESCO_THRESHOLD`, `DATASET_DIR`, class dirs, and `COLORS`.
  - Keep comments readable; fix mojibake only if touching those lines.
- **Validate**:
  - `python -c "import sys; sys.path.insert(0, 'src'); from film_color.profiles import COLORS; print(len(COLORS))"`

### Task 3: Move generator module and update imports

- **File**: `src/film_color/generator.py`
- **Action**: CREATE from `src/image_generator.py`
- **Implement**:
  - Replace `from color_profiles import ...` with `from .profiles import ...`.
  - Preserve public functions: `setup_directories`, `generate_color_variations`, `create_image`, `generate_images`.
  - Preserve `if __name__ == "__main__": generate_images()` for direct module execution.
- **Validate**:
  - `python -c "import sys; sys.path.insert(0, 'src'); from film_color.generator import create_image; print(create_image((150, 255, 255)).size)"`

### Task 4: Move dataset module and update imports

- **File**: `src/film_color/dataset.py`
- **Action**: CREATE from `src/prepare_dataset.py`
- **Implement**:
  - Preserve `load_dataset`, `normalize_dataset`, and `get_datasets`.
  - No behavior changes yet.
- **Validate**:
  - Import check only, if TensorFlow is installed:
    `python -c "import sys; sys.path.insert(0, 'src'); import film_color.dataset; print('ok')"`

### Task 5: Move model module and update imports

- **File**: `src/film_color/model.py`
- **Action**: CREATE from `src/train_model.py`
- **Implement**:
  - Replace `from prepare_dataset import get_datasets` with `from .dataset import get_datasets`.
  - Keep top-level training behavior for now to avoid scope creep, but do not import this module from package `__init__`.
  - Later issues can make training command-driven.
- **Validate**:
  - Syntax/import validation only if TensorFlow/Keras are installed.

### Task 6: Move color extractor modules and update imports

- **Files**:
  - `src/film_color/color_extractor.py`
  - `src/film_color/color_extractor_main.py`
- **Action**: CREATE from current extractor files
- **Implement**:
  - Replace `from color_profiles import ...` with `from .profiles import ...`.
  - Replace `from color_extractor_class import ColorExtractor` with `from .color_extractor import ColorExtractor`.
  - Preserve existing analyzer behavior.
- **Validate**:
  - `python -c "import sys; sys.path.insert(0, 'src'); from film_color.color_extractor import ColorExtractor; print(ColorExtractor.__name__)"`

### Task 7: Remove old loose source files

- **Files**:
  - `src/color_profiles.py`
  - `src/image_generator.py`
  - `src/prepare_dataset.py`
  - `src/train_model.py`
  - `src/color_extractor_class.py`
  - `src/color_extractor_main.py`
- **Action**: DELETE
- **Implement**:
  - Delete only after package equivalents exist.
- **Validate**:
  - `rg "from (color_profiles|prepare_dataset|color_extractor_class)" src`
  - The command should return no package source imports using old loose names.

---

## Validation Plan

Run lightweight import checks:

```powershell
python -c "import sys; sys.path.insert(0, 'src'); import film_color; print(film_color.__name__)"
python -c "import sys; sys.path.insert(0, 'src'); from film_color.profiles import COLORS; print(len(COLORS))"
python -c "import sys; sys.path.insert(0, 'src'); from film_color.generator import create_image; print(create_image((150, 255, 255)).size)"
python -c "import sys; sys.path.insert(0, 'src'); from film_color.color_extractor import ColorExtractor; print(ColorExtractor.__name__)"
rg "from (color_profiles|prepare_dataset|color_extractor_class)" src
```

TensorFlow-dependent modules may be import-checked only if installed locally. Full training is out of scope for Issue 1.

---

## Risks

| Risk | Mitigation |
|------|------------|
| Breaking script imports | Use package-relative imports inside `src/film_color/` |
| Accidentally triggering model training during package import | Keep `__init__.py` lightweight and avoid importing `model.py` |
| Scope creep into CLI/package metadata | Leave CLI and `pyproject.toml` for Issues 2 and 6 |
| Deleting source before replacement | Create new package files first, validate imports, then remove old files |

---

## Acceptance Criteria

- [ ] Package modules can be imported with `import film_color`.
- [ ] Core modules no longer depend on relative execution from the repo root.
- [ ] Existing generation logic still works after the move.
- [ ] Old loose source files are removed after package equivalents exist.
- [ ] No CLI or packaging metadata changes are included in this issue.

