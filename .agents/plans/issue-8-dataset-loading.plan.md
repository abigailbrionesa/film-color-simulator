# Plan: Issue 8 - Implement Dataset Loading Utilities

## Summary

Centralize TensorFlow image dataset loading behind a small typed config while keeping the module importable even when TensorFlow is not installed yet.

## Tasks

1. Add `DatasetConfig`.
2. Lazy-load TensorFlow inside dataset functions.
3. Provide train/validation dataset loading with consistent normalization.
4. Preserve `get_datasets()` compatibility.

## Validation

```powershell
py -m compileall src
py -c "from film_color.dataset import DatasetConfig; print(DatasetConfig())"
```

