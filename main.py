#!/usr/bin/env python3
"""news-summary-01 entry: write the summary in summary.txt to /output/entry.txt.

The summary is the repository's own text: this program copies it byte for
byte, so two runs write identical bytes. No network, no randomness, no
timestamps, standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "summary.txt", out_dir / "entry.txt")


if __name__ == "__main__":
    main()
