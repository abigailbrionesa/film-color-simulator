# Plan: Issue 2 - Add `pyproject.toml` and Dependency Metadata

## Summary

Add modern Python packaging metadata so the project can be installed locally and its dependencies are visible in one standard place. This issue should introduce `pyproject.toml` and align dependency documentation, while keeping actual CLI command implementation for later issues.

## User Story

As a developer cloning the project,
I want a standard Python project configuration,
So that I can install dependencies and import the package reliably.

## Metadata

| Field | Value |
|-------|-------|
| Type | ENHANCEMENT |
| Complexity | LOW |
| Systems Affected | Packaging, dependency metadata, docs |
| Issue | Issue 2 from `docs/ISSUES.md` |

---

## Current Codebase Patterns

### Existing Dependencies

Current `docs/requirements.txt` contains:

```text
numpy
opencv-python
Pillow
```

Source usage shows additional runtime dependencies:

```python
# src/film_color/dataset.py
import tensorflow as tf
```

```python
# src/film_color/model.py
from keras import layers, models
```

```python
# src/film_color/color_extractor.py
import cv2
import numpy as np
```

### Current Package Layout

Issue 1 introduced:

```text
src/
  film_color/
    __init__.py
    profiles.py
    generator.py
    dataset.py
    model.py
    color_extractor.py
    color_extractor_main.py
```

This supports a `setuptools` package discovery configuration using `package-dir = {"" = "src"}`.

### CLI Status

No `src/film_color/cli.py` exists yet. Because Issue 6 owns `film-color generate`, this issue should not pretend a real CLI is implemented.

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `pyproject.toml` | CREATE | Define project metadata, dependencies, package discovery, and dev extras |
| `docs/requirements.txt` | UPDATE | Either mirror runtime deps or point users to `pyproject.toml` |
| `.agents/plans/issue-2-pyproject-dependencies.plan.md` | CREATE | Record this implementation plan |

---

## Dependency Decision

Use standard dependencies:

- `numpy`
- `opencv-python`
- `Pillow`
- `tensorflow`

Do not list standalone `keras` separately unless validation shows local imports require it. Modern TensorFlow includes `tf.keras`, but the current code imports `keras` directly. For this issue, prefer one of two safe choices during implementation:

1. Include `keras` in dependencies to match current source imports exactly.
2. Or update `src/film_color/model.py` from `from keras import layers, models` to `from tensorflow.keras import layers, models`.

Recommended implementation: update the model import to `tensorflow.keras` and keep dependency metadata simpler with `tensorflow`.

---

## Implementation Tasks

### Task 1: Add `pyproject.toml`

- **File**: `pyproject.toml`
- **Action**: CREATE
- **Implement**:
  - Use `setuptools.build_meta`.
  - Set project name to `film-color-simulator`.
  - Set Python requirement to `>=3.10`.
  - Add runtime dependencies: `numpy`, `opencv-python`, `Pillow`, `tensorflow`.
  - Add optional dev dependencies: `pytest`.
  - Configure package discovery from `src`.
- **Do Not Implement Yet**:
  - Do not add `[project.scripts]` until `src/film_color/cli.py` exists in Issue 6.
- **Validate**:
  - `python -m pip install -e . --dry-run` if supported.
  - Or inspect metadata with `python -m pip install -e .` only if acceptable locally.

### Task 2: Align model import with dependency metadata

- **File**: `src/film_color/model.py`
- **Action**: UPDATE
- **Implement**:
  - Change `from keras import layers, models` to `from tensorflow.keras import layers, models`.
  - This avoids requiring a separate `keras` package.
- **Validate**:
  - `python -m compileall src`

### Task 3: Update dependency docs

- **File**: `docs/requirements.txt`
- **Action**: UPDATE
- **Implement**:
  - Add `tensorflow` if the file remains a dependency mirror.
  - Optionally add a comment that `pyproject.toml` is the source of truth.
- **Validate**:
  - Dependency docs and `pyproject.toml` do not contradict each other.

---

## Validation Plan

Run:

```powershell
python -m compileall src
python -m pip install -e . --dry-run
```

If `pip --dry-run` is unavailable, run:

```powershell
python -m pip --version
```

and report that install validation was limited.

Avoid installing heavy ML dependencies unless already available or explicitly needed; this issue is metadata-focused.

---

## Risks

| Risk | Mitigation |
|------|------------|
| TensorFlow install is heavy | Validate metadata without forcing dependency installation where possible |
| Adding CLI script too early | Defer `[project.scripts]` until Issue 6 creates `film_color.cli` |
| Dependency mismatch from direct `keras` import | Update model import to `tensorflow.keras` |
| Docs drift | Keep `docs/requirements.txt` aligned or mark `pyproject.toml` as source of truth |

---

## Acceptance Criteria

- [ ] `pyproject.toml` exists.
- [ ] Package discovery points to `src/film_color`.
- [ ] Runtime dependencies include image generation and ML packages needed by the current source.
- [ ] Dependency docs are aligned with packaging metadata.
- [ ] No actual CLI commands are claimed until Issue 6.

