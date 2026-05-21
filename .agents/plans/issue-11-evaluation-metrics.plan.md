# Plan: Issue 11 - Add Evaluation Metrics and Confusion Matrix Output

## Summary

Add a reusable evaluation module that loads a trained model, evaluates the validation split, computes a confusion matrix, and saves metrics to JSON.

## Tasks

1. Add `EvaluationConfig`.
2. Load validation data through `DatasetConfig`.
3. Compute validation accuracy and confusion matrix.
4. Save `evaluation.json`.

## Validation

```powershell
py -m compileall src
py -c "from film_color.evaluation import EvaluationConfig; print(EvaluationConfig())"
```

Runtime evaluation requires TensorFlow and a trained model.

