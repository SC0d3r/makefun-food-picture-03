#!/usr/bin/env python3
"""Publish the submitted entry.png image as a make.fun art entry.

The image is copied byte for byte into MAKEFUN_OUTPUT_DIR (default /output).
The copy is verified to be non-empty and identical to the source.
"""

from __future__ import annotations

import filecmp
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output").expanduser()
    destination = output_dir / "entry.png"

    if not source.is_file():
        print(f"error: entry.png source image not found: {source}", file=sys.stderr)
        return 1

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {output_dir}: {exc}", file=sys.stderr)
        return 1

    try:
        if source.resolve() != destination.resolve():
            shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: failed to copy {source} to {destination}: {exc}", file=sys.stderr)
        return 1

    try:
        size = destination.stat().st_size
    except OSError as exc:
        print(f"error: cannot read copied image {destination}: {exc}", file=sys.stderr)
        return 1

    if size == 0:
        print(f"error: copied image is empty: {destination}", file=sys.stderr)
        return 1

    if not filecmp.cmp(source, destination, shallow=False):
        print(
            f"error: copied image is not byte-identical to source: {destination}",
            file=sys.stderr,
        )
        return 1

    print(destination)
    print(f"{size} bytes written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
