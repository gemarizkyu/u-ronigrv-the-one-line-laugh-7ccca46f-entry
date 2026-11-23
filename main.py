"""Write one original one-liner to entry.txt for make.fun's "The One-Line Laugh".

Deterministic: the same line, byte for byte, on every run. No randomness,
no network, no clock, no input files.

The line: an everyday truth (banks flag unusual card activity) with a
surprise at the end (the "unusual" thing is buying vegetables) — a twist
that still makes sense, in a single sentence of 121 characters.
"""

import os

LINE = "My bank flagged my card for unusual activity the day I bought vegetables, which says more about my diet than my security."


def main():
    # Gate self-check: one sentence, 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "single sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
