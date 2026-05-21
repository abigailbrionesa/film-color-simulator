# Plan: Issue 20 - Add Lightweight Inference Command

## Summary

Add `film-color predict` for running a trained model on one image and printing the predicted class plus confidence.

## Tasks

1. Add `prediction.py`.
2. Add `PredictionConfig`.
3. Add `film-color predict` CLI command.
4. Validate command help and missing-path handling.

## Validation

```powershell
py -m pytest
film-color predict --help
```

Runtime prediction requires TensorFlow and a trained model.

