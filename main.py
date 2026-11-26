#!/usr/bin/env python3
"""One Line, Big Laugh — round 4 entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Deterministic, no network, no side effects beyond that one file.

The line: a hotel wake-up call answered by a priest. The setup promises
a routine travel complaint; the punchline turns it into last rites.
"""

import os

ENTRY = "I asked the hotel for a wake-up call; they sent a priest."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
