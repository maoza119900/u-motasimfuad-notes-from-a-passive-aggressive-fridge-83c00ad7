#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one fixed passive-aggressive note from a smart fridge to its owner
into $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Fully deterministic: the output is a single hard-coded string. The program
reads no clock, no randomness, no network and no input files.
"""

import os

NOTE = "The yogurt expired Tuesday. You sniffed it, put it back, and sniffed it again. My sensors have logged this as a cry for help."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
