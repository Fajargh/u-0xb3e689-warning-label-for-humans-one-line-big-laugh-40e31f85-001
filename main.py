"""Warning Label for Humans: One Line, Big Laugh.

Writes the chosen single-line safety warning label to /output/entry.txt.

The line is a fixed constant in this file: it is deterministic, stdlib-only,
and the validate_line() guard below enforces the competition gate (UTF-8 text of
1 to 160 characters, single line, not only whitespace) before anything is
written.
"""

import os

ENTRY = (
    "WARNING: This human ships with no off switch, no mute button, "
    "and will insist it is fine while visibly on fire."
)

MAX_CHARS = 160


def validate_line(line: str) -> None:
    """Enforce the competition gate: 1-160 chars, single line, non-blank UTF-8."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable as UTF-8


def main() -> None:
    validate_line(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
