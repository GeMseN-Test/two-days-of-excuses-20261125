#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes exactly one line (160 characters, under the 200 limit) to
/output/entry.txt: an AI agent explaining a missed deadline.

The joke: total machine confidence ("99% confident", Friday 5 PM)
colliding with total failure — 38 hours spent optimizing a script
whose only job is renaming a file "final_final_v2_FINAL.docx".
Deterministic: no randomness, no network, no trailing newline.
"""

import os

ENTRY = (
    "I promised your report by Friday 5 PM, 99% confident. "
    "It is Sunday now \u2014 I spent 38 hours optimizing a script "
    "that renames the file 'final_final_v2_FINAL.docx'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
