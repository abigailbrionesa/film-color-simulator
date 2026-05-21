# Plan: Issue 5 - Add Deterministic Generation With Random Seed Support

## Summary

Make synthetic dataset generation reproducible by using local random number generators and writing generation metadata to the output directory.

## Tasks

1. Thread a local `random.Random` instance through HSV variation generation.
2. Thread a local NumPy generator through image noise generation.
3. Write `metadata.json` with seed, sample count, image size, labels, and generated file count.
4. Validate same seed/config creates the same metadata and file count.

## Validation

```powershell
py -m compileall src
py -c "... run generation twice with the same seed ..."
```

