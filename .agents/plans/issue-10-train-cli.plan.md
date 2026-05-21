# Plan: Issue 10 - Add `film-color train` CLI Command

## Summary

Add a command-line training workflow that loads a generated dataset, trains the baseline CNN, saves the model, and prints final metrics.

## Tasks

1. Add `src/film_color/training.py`.
2. Add `TrainingConfig`.
3. Implement `train_model`.
4. Add `film-color train` CLI command.

## Validation

```powershell
py -m compileall src
film-color train --help
```

Full training validation requires TensorFlow runtime support.

