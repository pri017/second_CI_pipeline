import importlib

module = importlib.import_module("34_check_sorted")


def test_check_sorted():
    assert module.is_sorted([1, 2, 2, 5])
    assert not module.is_sorted([3, 1, 2])
