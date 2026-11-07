import importlib

module = importlib.import_module("32_count_words")


def test_count_words():
    assert module.count_words('Hello wonderful world') == 3
    assert module.count_words('  ') == 0
