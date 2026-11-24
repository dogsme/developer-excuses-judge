"""Developer-excuses entry for make.fun.

Writes one funny single-line developer excuse to /output/entry.txt.
The line is a fixed string: the program takes no input, reads no files,
and makes no network calls, so every run produces the same entry.
"""

from pathlib import Path

EXCUSE = (
    "It worked on my machine because my machine has never met a user, "
    "a deadline, or a single byte of real production data."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
