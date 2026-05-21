# Plan: Issue 12 - Add `film-color evaluate` CLI Command

## Summary

Expose the evaluation module through `film-color evaluate` so users can run the complete generate/train/evaluate workflow from the command line.

## Tasks

1. Add evaluate subcommand.
2. Support `--data`, `--model`, `--output`, `--batch-size`, `--image-size`, and `--seed`.
3. Print a concise evaluation summary.

## Validation

```powershell
py -m compileall src
film-color evaluate --help
```

