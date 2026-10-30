---
name: version-check
description: Confirm the release version is consistent across the repository. Use before cutting a release.
---

# Version check

Confirm that the version in `scripts/release.py` matches `src/acme_version.py`.

## Steps

1. Run `python3 scripts/version_check.py`.
2. If it prints `ok`, report the version to the user.
3. If it prints `mismatch`, show both values to the user and suggest which file to update. Do not edit files until the user asks.
4. If it prints `error`, tell the user which version could not be read and stop. Do not suggest a release until the user has fixed the file.
