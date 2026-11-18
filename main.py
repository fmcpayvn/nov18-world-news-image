#!/usr/bin/env python3
"""news-image-20261118 entry: copy the bundled image to /output/entry.png.

The image (entry.png, 1024x1024 PNG) sums up the world news of Wednesday
18 November 2026: the Bitcoin crash, Nvidia's $115.8B quarter, OpenAI's
GPT-6.2, a week of crypto hacks, and Iran's strikes on US bases.

Standard library only. No network, no randomness, no timestamps: every run
writes the same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"bundled image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    # Fail loudly instead of shipping a truncated copy.
    if dest.stat().st_size != SOURCE.stat().st_size:
        raise IOError(f"copy mismatch: {dest} is not {SOURCE}")


if __name__ == "__main__":
    main()
