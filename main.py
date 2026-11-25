#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (one line, <= 100 characters) to
/output/entry.txt. Fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "fix: dedupe duplicate employee records; "
    "merged the twins into one badge, one salary, one chair"
)


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
