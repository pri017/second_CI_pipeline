import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent():
    assert module.most_frequent([1, 2, 2, 3]) == 2
    assert module.most_frequent([]) is None
