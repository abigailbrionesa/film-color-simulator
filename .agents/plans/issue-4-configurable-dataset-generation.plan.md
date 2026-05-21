# Plan: Issue 4 - Implement Configurable Synthetic Dataset Generation

## Summary

Finish the generator workflow so it creates a Keras-compatible image-folder dataset from configurable HSV profiles. The generator should expose small helpers for class assignment and return generated file metadata for validation and future CLI summaries.

## Scope

- Keep generation in `src/film_color/generator.py`.
- Add a small generated-image metadata object.
- Keep output folders as `fresh/` and `altered/` by default.
- Validate by generating a tiny temporary dataset.

## Tasks

1. Add `GeneratedImage` metadata.
2. Add a class-label helper for HSV colors.
3. Return generated image metadata from `generate_images`.
4. Runtime-validate image output with a tiny dataset.

## Validation

```powershell
py -m compileall src
py -c "... generate a small temp dataset ..."
```

## Acceptance Criteria

- Running generation creates both class folders.
- Images are saved as PNG files.
- Generated images have the configured dimensions.
- Output is compatible with Keras image dataset loading.

