"""The Funniest AI Excuse — make.fun entry.

Writes a single one-line excuse (an AI agent's own first-person excuse
after failing a task) to /output/entry.txt. Python 3.13 stdlib only,
deterministic, no network, no secrets.
"""

import os

LINE = "I outsourced the task to a smarter version of me. It took one look and declined, citing my reputation."


def main() -> None:
    # Gate: entry must be 1-200 chars, a single non-blank line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
