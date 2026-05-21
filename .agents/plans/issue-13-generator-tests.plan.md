# Plan: Issue 13 - Add Unit Tests for Color Profiles and Generator

## Summary

Add fast pytest coverage for HSV profiles, image creation, generated folder structure, and deterministic metadata.

## Tasks

1. Add profile tests.
2. Add generator tests using `tmp_path`.
3. Avoid TensorFlow-dependent tests.

## Validation

```powershell
py -m pytest
```

