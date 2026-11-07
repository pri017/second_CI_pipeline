def gcd(a, b):
    """Find greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)
