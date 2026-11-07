def most_frequent(values):
    """Return the most frequent element, breaking ties by first appearance."""
    if not values:
        return None
    return max(values, key=values.count)
