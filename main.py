"""Seventeen Syllables of Debugging — writes one haiku to the output dir.

The haiku: a breakpoint set at 3 a.m., a stack trace that points at
everyone else's code first, and the turn every debugger knows — it lands
on my line.
"""

import os
import sys

HAIKU_LINES = (
    "Breakpoint set at three",
    "the stack trace points at strangers",
    "then lands on my line",
)


def main() -> int:
    text = "\n".join(HAIKU_LINES) + "\n"
    # Gate guard: exactly 3 lines, 1-200 chars, or refuse to write anything.
    if len(HAIKU_LINES) != 3 or not 1 <= len(text) <= 200:
        print("error: haiku is outside the gate (3 lines, 1-200 chars)", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
