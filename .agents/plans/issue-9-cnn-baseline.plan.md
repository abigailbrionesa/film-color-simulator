# Plan: Issue 9 - Implement Small CNN Baseline Model

## Summary

Turn the current import-time training script into a reusable baseline model module. The model should be created only when requested and should remain compact for quick local experiments.

## Tasks

1. Add `ModelConfig`.
2. Move TensorFlow/Keras imports inside `create_model`.
3. Remove top-level dataset loading/training side effects.
4. Keep architecture small and binary-classification oriented.

## Validation

```powershell
py -m compileall src
py -c "from film_color.model import ModelConfig; print(ModelConfig())"
```

