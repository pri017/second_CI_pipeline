def rotate_string(text, k):
    """Rotate a string left by k positions."""
    if not text:
        return text
    k %= len(text)
    return text[k:] + text[:k]
