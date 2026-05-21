# Plan: Issue 3 - Create Typed Config Objects for Generation Settings

## Summary

Add a lightweight typed configuration object for synthetic dataset generation and update the generator to accept it. This replaces hard-coded generation settings at call sites while preserving simple defaults.

## Scope

- Create `src/film_color/config.py`.
- Add a `GenerationConfig` dataclass.
- Update generator functions to accept caller-provided configuration.
- Keep CLI work out of scope.

## Tasks

1. Add `GenerationConfig` with image size, variations, output directory, random seed placeholder, noise range, labels, threshold, and colors.
2. Update `setup_directories` and `generate_images` to use config.
3. Update `create_image` to accept a configurable noise range.
4. Keep default behavior available through `generate_images()`.

## Validation

```powershell
python -m compileall src
python -c "import sys; sys.path.insert(0, 'src'); from film_color.config import GenerationConfig; print(GenerationConfig().image_size)"
```

Full generator runtime validation depends on `opencv-python`.

## Acceptance Criteria

- Generator can run with default config.
- Generator can run with caller-provided settings.
- Config values are type hinted.

