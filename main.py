"""Spikes Into Perches — Pigeon Pitch, One Line (make.fun).

A city pigeon pitches investors its startup: the anti-pigeon spikes
meant to keep birds off buildings are rented back out as paid perches,
so the building now pays the pigeon to sit exactly where it once paid
to keep it away. The program writes that one-line pitch to
/output/entry.txt, byte for byte, with no trailing newline.
"""

import os

# ENTRY: the pigeon's one-line elevator pitch to investors, 132
# characters, one line, no trailing newline when written out.
ENTRY = "Spikes were supposed to stop us; I rent them out as perches at $1 an hour. The building pays me to sit where it paid to keep me off."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
