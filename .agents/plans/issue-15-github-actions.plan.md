# Plan: Issue 15 - Add GitHub Actions Workflow

## Summary

Add a lightweight test workflow that installs the package and runs the fast pytest suite without expensive model training.

## Tasks

1. Add `.github/workflows/tests.yml`.
2. Use Python 3.11.
3. Install lightweight test dependencies.
4. Install the package editable with `--no-deps`.
5. Run `pytest`.

## Validation

```powershell
py -m pytest
```

