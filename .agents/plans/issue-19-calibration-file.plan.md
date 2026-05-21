# Plan: Issue 19 - Calibrate Profiles Against Real Lab Samples

## Summary

Add optional calibration-file loading for HSV profiles so real measurements can replace the defaults when available.

## Tasks

1. Add calibration JSON loader.
2. Validate HSV values.
3. Add `GenerationConfig.from_calibration_file`.
4. Add tests for valid and invalid calibration files.

## Validation

```powershell
py -m pytest
```

