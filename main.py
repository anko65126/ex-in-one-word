"""Entry program for 'Describe Your Ex in One Word'.

One word: nonrefundable. I spent three years, two apartments and one
holiday in Kyoto on the relationship, and when it ended there was no receipt,
no returns desk and no store credit, only a loyalty card with one stamp on it.
The word does the whole job by itself:
it says I paid, I kept the box, and the box is empty. Anyone who has ever
tried to return something past thirty days understands it before the second
syllable, and that is exactly why it fits in a single word.
"""

from pathlib import Path
import sys

TEXT = "nonrefundable"
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(TEXT) <= 111, f"text is {len(TEXT)} characters, outside the 1-111 limit"
    assert TEXT.strip(), "text must not be blank"
    assert " " not in TEXT.strip(), "entry must be exactly one word"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main(sys.argv)
