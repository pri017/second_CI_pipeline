def transpose_matrix(matrix):
    """Transpose a rectangular matrix (list of rows)."""
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('Matrix rows must have equal lengths')
    return [list(column) for column in zip(*matrix)]
