"""Have You Tried Turning It Off?

Writes one single funny line, a hopeless tech support agent's reply to a
desperate customer, to entry.txt in the output directory given by
MAKEFUN_OUTPUT_DIR (default "/output").

The moment: the customer's router is dead, and the agent walks them through
the sacred ritual — unplug it, count to ten out loud, plug it back in and
pray — while both of them already know this is the whole plan.
"""

import os

ENTRY = (
    "Unplug the router, count to ten out loud — yes, out loud, it can tell — "
    "plug it back in, and if the lights blink, we both pretend that was the "
    "plan all along."
)

MAX_CHARS = 199


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, over the {MAX_CHARS} limit")
    if len(body) < 1:
        raise SystemExit("entry is empty")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
