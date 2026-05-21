# Plan: Issue 14 - Add CLI Smoke Tests

## Summary

Add fast CLI tests for the generate command and invalid argument handling.

## Tasks

1. Test `generate` creates expected folders and files.
2. Test invalid arguments exit cleanly.
3. Keep tests isolated in temporary folders.

## Validation

```powershell
py -m pytest
```

