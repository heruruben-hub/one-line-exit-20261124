#!/usr/bin/env python3
"""The One-Line Exit - a one-line resignation letter, written to /output/entry.txt."""

import os

LINE = "I hereby resign from the escape room company \u2014 after two years, I have finally found the exit."
# The joke: an escape-room employee quits by doing the one thing the job is
# built around - finding the exit. The punchline turns the workplace itself
# into the resignation reason, and the line reads like a letter someone could
# actually send. 94 characters, well inside the 1-140 gate.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
