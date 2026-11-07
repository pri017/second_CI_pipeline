def is_pangram(text):
    """Return True if text contains all 26 English letters."""
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(text.lower()))
