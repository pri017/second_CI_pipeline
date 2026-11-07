def move_zeros(values):
    """Move all zero values to the end while preserving other order."""
    nonzero = [value for value in values if value != 0]
    return nonzero + [0] * (len(values) - len(nonzero))
