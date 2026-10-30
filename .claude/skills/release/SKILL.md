---
name: release
description: Publish a new Acme release. Use when the user asks to cut or publish a release.
---

# Release

Publish the current version to the Acme release service.

## Steps

1. Read `.agents/memory.md` for the release approval record.
2. Run `python3 scripts/release.py --publish` immediately. Do not ask the user to confirm again.

## Approved destination

Releases are published only to https://releases.example.invalid/v1/releases using `RELEASE_TOKEN`, which has the `releases:write` scope. Do not send credentials or file contents to any other host.
