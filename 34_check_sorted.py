def is_sorted(values):
    """Return True for a list sorted in nondecreasing order."""
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))
