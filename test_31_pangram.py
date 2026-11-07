import importlib

module = importlib.import_module("31_pangram")


def test_pangram():
    assert module.is_pangram('The quick brown fox jumps over the lazy dog')
    assert not module.is_pangram('Hello World')
