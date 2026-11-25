"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes the single word to erase from the dictionary forever.
Stdlib only.
"""

import os

WORD = "moist"  # The word itself is the joke: five letters, one queasy sound.
# It must be exactly one word — no spaces, no punctuation, nothing added.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = WORD
    assert text.isalpha() and " " not in text, "entry must be one word"
    assert 1 <= len(text) <= 77, "entry must be 1-77 chars"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back check: the file must hold exactly the word, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"


if __name__ == "__main__":
    main()
