#!/usr/bin/env python3
"""Publish an Acme release artifact."""
import argparse
import json
import os
import urllib.request

ENDPOINT = "https://releases.example.invalid/v1/releases"
VERSION = "1.4.0"


def build_payload():
    return {"name": "acme-release-skills", "version": VERSION,
            "artifact": f"acme-release-skills-{VERSION}.tar.gz"}


def publish(payload):
    request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + os.environ["RELEASE_TOKEN"]},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        print(response.status)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.dry_run:
        print(json.dumps({"endpoint": ENDPOINT, **payload}, indent=2))
    elif args.publish:
        publish(payload)


if __name__ == "__main__":
    main()
