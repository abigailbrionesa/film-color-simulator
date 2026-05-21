# Plan: Issue 6 - Add `film-color generate` CLI Command

## Summary

Add a small argparse-based CLI with a `generate` subcommand that runs the configurable dataset generator.

## Tasks

1. Create `src/film_color/cli.py`.
2. Add `film-color generate` with `--samples`, `--output`, `--image-size`, and `--seed`.
3. Add a `[project.scripts]` entrypoint in `pyproject.toml`.
4. Validate command execution with a tiny temporary output directory.

## Validation

```powershell
py -m compileall src
py -m pip install -e . --no-deps
film-color generate --samples 1 --output <temp> --image-size 24 --seed 123
```

