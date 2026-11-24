#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 chars) to /output/entry.txt:
a quiet, earned moment of pride — a girl who saved coins for three years
buys her mother the winter coat, and walks home in the cold herself.
Deterministic: same bytes on every run. Python stdlib only.
"""

import os

ENTRY = (
    "For three years she saved coins in a jam jar; "
    "this morning she bought her mother the winter coat, "
    "and walked home in the cold herself."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
