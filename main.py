"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table, to
/output/entry.txt (1-200 characters, one sentence, no apology).
"""

import os

LINE = "The glass spent all morning hogging my sunbeam, so I gave it a one-way ticket to the floor."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
