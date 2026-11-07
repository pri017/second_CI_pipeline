import importlib

module = importlib.import_module("40_gcd")


def test_gcd():
    assert module.gcd(48, 18) == 6
    assert module.gcd(-12, 8) == 4
