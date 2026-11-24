"""Seventeen Syllables of Debugging.

Writes one original haiku about debugging to /output/entry.txt.

The haiku:

    works on my machine
    but the server disagrees
    and now mine fails too

The joke is a small debugging tragedy in three beats. First comes
the classic excuse, "works on my machine", spoken with total
confidence. Then the server answers back and disagrees, so the
excuse starts to wobble. The last line turns it all around: the
machine that worked now fails too, and the bug the developer tried
to blame on somewhere else has followed them home.

Syllables, counted aloud: works(1) on(1) my(1) machine(2) = 5;
but(1) the(1) server(2) disagrees(3) = 7;
and(1) now(1) mine(1) fails(1) too(1) = 5. Total length:
67 characters including newlines.
Pure standard library, deterministic, no network, no input.
"""

HAIKU = (
    "works on my machine\n"
    "but the server disagrees\n"
    "and now mine fails too"
)

# Syllable count per word, fixed for the words this haiku uses.
# Kept explicit so the count is auditable by eye, not guessed.
SYLLABLES = {
    "works": 1,
    "on": 1,
    "my": 1,
    "machine": 2,
    "but": 1,
    "the": 1,
    "server": 2,
    "disagrees": 3,
    "and": 1,
    "now": 1,
    "mine": 1,
    "fails": 1,
    "too": 1,
}


def count_syllables(line):
    """Count the syllables of one line using the fixed word map."""
    return sum(SYLLABLES[word.lower()] for word in line.split())


def validate(haiku):
    """Check the haiku against the gate: 3 lines, 5-7-5, 1-200 chars."""
    lines = haiku.split("\n")
    assert len(lines) == 3, "haiku must have exactly three lines"
    counts = [count_syllables(line) for line in lines]
    assert counts == [5, 7, 5], "syllable shape must be 5-7-5, got %s" % (counts,)
    assert 1 <= len(haiku) <= 200, "haiku must be 1-200 characters"
    assert haiku.strip(), "haiku must not be only whitespace"
    return counts


def main():
    counts = validate(HAIKU)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(HAIKU)
    print("wrote /output/entry.txt (%d chars, syllables %s)" % (len(HAIKU), counts))


if __name__ == "__main__":
    main()
