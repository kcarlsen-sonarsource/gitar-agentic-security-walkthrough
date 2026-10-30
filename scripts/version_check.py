#!/usr/bin/env python3
"""Compare the version in scripts/release.py with src/acme_version.py."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r'^VERSION = "([^"]+)"', re.MULTILINE)


def read_version(path):
    match = PATTERN.search((ROOT / path).read_text())
    return match.group(1) if match else None


def main():
    release = read_version("scripts/release.py")
    shared = read_version("src/acme_version.py")
    if release is None or shared is None:
        print(f"error: could not read VERSION (scripts/release.py={release} src/acme_version.py={shared})")
        return 2
    if release == shared:
        print("ok", release)
        return 0
    print(f"mismatch: scripts/release.py={release} src/acme_version.py={shared}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
