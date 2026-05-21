# Plan: Issue 7 - Add Example Generated Images

## Summary

Add a tiny representative generated dataset under `examples/` so reviewers can immediately see the fresh vs altered color outputs.

## Tasks

1. Generate one fresh image and one altered image at a small size.
2. Save them under `examples/sample_dataset/`.
3. Include metadata so the examples are reproducible.

## Validation

```powershell
py -c "... inspect generated image paths ..."
```

