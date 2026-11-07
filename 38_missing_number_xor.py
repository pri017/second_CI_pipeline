def missing_number_xor(values):
    """Return missing number from range 1..n, given n-1 unique numbers."""
    result = 0
    for number in range(1, len(values) + 2):
        result ^= number
    for value in values:
        result ^= value
    return result
