import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number_xor():
    assert module.missing_number_xor([1, 2, 4, 5]) == 3
    assert module.missing_number_xor([]) == 1
