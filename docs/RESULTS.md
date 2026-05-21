# Results

This document summarizes the current validated behavior of Film Color Simulator.

## Synthetic Dataset Example

The committed example dataset was generated with:

```powershell
film-color generate --samples 1 --output examples/sample_dataset --image-size 128 --seed 42
```

Output:

- `examples/sample_dataset/fresh/fresh_0_0.png`
- `examples/sample_dataset/altered/altered_1_0.png`
- `examples/sample_dataset/metadata.json`

Metadata summary:

| Field | Value |
| --- | --- |
| Image size | 128 x 128 |
| Random seed | 42 |
| Generated images | 2 |
| Classes | `fresh`, `altered` |

## Test Results

Current fast test suite:

```text
7 passed
```

Covered behavior:

- HSV profile values are in valid ranges.
- Default class labels are `fresh` and `altered`.
- Generated images have expected dimensions and RGB mode.
- Dataset generation creates class folders and metadata.
- CLI generation works with temporary output folders.
- Invalid CLI arguments fail cleanly.

## Baseline Model Metrics

The training and evaluation commands are implemented, but model metrics are not committed yet because they depend on running TensorFlow in a compatible local environment.

To produce the baseline validation accuracy and confusion matrix:

```powershell
film-color generate --samples 20 --output dataset --image-size 128 --seed 123
film-color train --data dataset --epochs 10 --image-size 128 --model-output artifacts/model.keras
film-color evaluate --data dataset --image-size 128 --model artifacts/model.keras --output artifacts/evaluation.json
```

Expected evaluation artifact:

```text
artifacts/evaluation.json
```

## Limitations

These results validate the synthetic generator and command workflow. They do not demonstrate real-world food freshness performance. Real lab images would be required to evaluate generalization beyond controlled synthetic color profiles.
