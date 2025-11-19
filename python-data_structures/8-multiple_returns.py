#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character (or None if empty)."""
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    return (len(sentence), first_char)
