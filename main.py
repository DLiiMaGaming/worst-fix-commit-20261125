#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (one line, <= 100 characters) to
/output/entry.txt. Fully deterministic: the same bytes on every run.
"""

import os

ENTRY = "fix: dedupe duplicate employee records; merged the twins into one badge, one salary, one chair"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
