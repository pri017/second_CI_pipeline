from collections import Counter


def first_non_repeating(text):
    """Return first character occurring once, or None."""
    counts = Counter(text)
    return next((char for char in text if counts[char] == 1), None)
