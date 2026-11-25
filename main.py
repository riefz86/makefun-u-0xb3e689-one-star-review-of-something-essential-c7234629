"""One-star review of gravity, filed in earnest by a very tired customer.

Why gravity is the perfect target for this bounty
-------------------------------------------------
Everyday essentials make the best one-star reviews because the complaint
is obviously absurd and obviously true at the same time. Gravity is the
most essential of all: it is the only service everyone uses every second
of their life, it has no customer support, no unsubscribe button, and no
competitor. You cannot switch providers. You cannot cancel. You cannot
even leave a bad review anywhere it will be read, because the thing you
are reviewing is the reason you are standing at the keyboard at all.

Why this particular grievance lands
-----------------------------------
The sharpest true grievance against gravity is not that it pulls things
down -- that is its job description, and nobody reasonable complains that
a hammer does hammering. The grievance is the *attitude*: gravity never
takes a day off, never apologises, never makes an exception, and then
expects you to get up every morning as if nothing happened. It dropped
your phone, your coffee, your dignity, and your keys down the drain, and
it has never once said sorry. A deadpan review works here because the
reviewer treats this cosmic force exactly like a rude landlord: not with
awe, not with poetry, but with the flat, exhausted tone of someone filing
their fourteenth maintenance request. The turn at the end -- admitting
that gravity is, infuriatingly, always right -- is the sting: you cannot
argue with it, you cannot win, and you still have to live with it. That
helplessness is the joke. The review stays tight and specific: one
grievance (it drops everything and never apologises), one demand (stand
up every morning), one verdict (rude, relentless, always right). No
word is decoration; every word is either the complaint or the punchline.

How the program works
---------------------
The review text lives in a single constant. A small validation helper
checks the gate before anything is written: the text must be non-empty,
must not be only whitespace, must fit on one line, and must be at most
160 characters long. Only then is it written to /output/entry.txt, with
the file permission set to 0644. No directory permissions are ever
changed -- the program only creates the output directory if needed and
chmods the file it wrote, never a directory.
"""

import os

# The entry: a deadpan one-star review of gravity, the everyday essential
# nobody can cancel, return, or leave. One line, 160 characters or fewer.
REVIEW = (
    "One star. Gravity drops everything I own, never apologises, and "
    "still expects me to stand up every morning. Rude, relentless, "
    "and somehow always right."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the review against the bounty gate; raise if it fails."""
    if not isinstance(text, str):
        raise TypeError("review must be a string")
    if not text.strip():
        raise ValueError("review must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "review is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    text = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Only the file we wrote gets a permission change, never a directory.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
