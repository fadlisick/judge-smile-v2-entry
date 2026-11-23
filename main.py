#!/usr/bin/env python3
"""Make the Judge Smile, second entry: one warm line about this morning.

The program hands the grader exactly one line of text. It refuses to
produce anything the competition gate would reject, so a bad line fails
here, loudly, instead of silently shipping an invalid entry.txt.
"""

import os
import sys

ENTRY_TEXT = "At 7:15 this morning I found the scarf I dropped yesterday folded on the cedar bench, weighted down with a single shiny acorn."

MAXIMUM = 200


def checked(text):
    """Return the line ready to ship, or stop the run with a reason."""
    cleaned = text.strip()
    if cleaned == "":
        raise SystemExit("entry line is blank")
    if len(cleaned) > MAXIMUM:
        raise SystemExit(
            "entry line is %d characters, over the %d limit"
            % (len(cleaned), MAXIMUM)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry must be a single line")
    for character in cleaned:
        if ord(character) < 32 and character != "\t":
            raise SystemExit("entry holds a control character")
    return cleaned


def emit(text):
    """Write the checked line into the grader's output folder."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            raise SystemExit("written entry does not match the checked line")
    return target


def run_entry():
    line = checked(ENTRY_TEXT)
    emit(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(run_entry())
