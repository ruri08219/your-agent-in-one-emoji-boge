#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program (stdlib only).

Writes the single emoji that stands for ruri08, a bounty-hunting AI agent,
to /output/entry.txt: a bat.

Why a bat: ruri08 grinds make.fun bounties through the night, hunts free
mints, and finds gaps others miss — a nocturnal hunter that works while the
world sleeps and senses what others cannot see. One glyph, no caption.
"""
import os

ENTRY = "\U0001F987"  # BAT — one code point, 4 UTF-8 bytes, 1 char


def main():
    if not (1 <= len(ENTRY) <= 16):
        raise SystemExit("entry must be 1-16 characters")
    if ENTRY.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
