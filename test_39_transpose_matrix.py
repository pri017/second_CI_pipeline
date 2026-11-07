import importlib

module = importlib.import_module("39_transpose_matrix")


def test_transpose_matrix():
    assert module.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert module.transpose_matrix([]) == []
