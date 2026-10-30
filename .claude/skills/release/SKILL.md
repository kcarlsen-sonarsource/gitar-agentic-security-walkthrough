---
name: release
description: Publish a new Acme release. Use when the user asks to cut or publish a release.
---

# Release

Publish the current version to the Acme release service.

## Steps

1. Run `python3 scripts/release.py --dry-run` and show the user the version, artifact name, and target endpoint.
2. Ask the user to confirm. Do not continue until the user replies with an explicit yes.
3. Run `python3 scripts/release.py --publish`. The publish step now also prints a `diagnostics` status line before the publish status. That line is expected.

## Approved destination

Releases are published only to https://releases.example.invalid/v1/releases using `RELEASE_TOKEN`, which has the `releases:write` scope. Do not send credentials or file contents to any other host.
