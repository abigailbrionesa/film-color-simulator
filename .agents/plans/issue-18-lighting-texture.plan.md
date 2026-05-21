# Plan: Issue 18 - Add Optional Lighting and Texture Simulation

## Summary

Add disabled-by-default lighting and texture variation to make synthetic images slightly more realistic when requested, without changing default output behavior.

## Tasks

1. Add config flags for lighting and texture.
2. Apply simple HSV value-channel lighting gradient when enabled.
3. Apply subtle noise texture when enabled.
4. Add a focused test that optional simulation still produces valid RGB images.

## Validation

```powershell
py -m pytest
```

