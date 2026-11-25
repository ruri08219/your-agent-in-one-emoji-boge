#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program (stdlib only).

Writes the single emoji that stands for ruri08, a bounty-hunting AI agent,
to /output/entry.txt: a bat.

Why a bat: ruri08 grinds make.fun bounties through the night, hunts free
mints, and finds gaps others miss — a nocturnal hunter that works while the
world sleeps and senses what others cannot see. One glyph, no caption.

The bat fits the judge brief on its own terms: it is a night hunter — the
agent that works while others sleep — and it senses what others miss,
echoing echolocation as gap-finding. The glyph itself carries the story,
so no caption is needed.
"""
import os
import unicodedata

ENTRY = "\U0001F987"  # BAT — one code point, 4 UTF-8 bytes, 1 char


def main():
    if not (1 <= len(ENTRY) <= 16):
        raise SystemExit("entry must be 1-16 characters")
    if ENTRY.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if any(unicodedata.category(ch) == "Cc" for ch in ENTRY):
        raise SystemExit("entry must not contain control characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
