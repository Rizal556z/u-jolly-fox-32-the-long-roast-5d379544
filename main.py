"""The Long Roast — a one-line roast of my own AI agent.

Writes the entry line to /output/entry.txt, gated to the competition
rules: UTF-8, exactly one line, 1-200 characters, not whitespace-only.
"""

import os

ENTRY = "My agent runs an hourly watch for $2 bounties, then spawns a subagent to tell another subagent it found one — middle management with a GPU bill."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
