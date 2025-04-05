#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    # 1. Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Check if m_a or m_b is empty (either [] or [[]])
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Check that all elements in m_a and m_b are ints or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    # 5. Check that each row of m_a and m_b is the same size
    row_length_a = len(m_a[0])
    if not all(len(row) == row_length_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_length_b = len(m_b[0])
    if not all(len(row) == row_length_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Check if m_a and m_b can be multiplied (columns in m_a == rows in m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7. Matrix multiplication logic
    result = []
    for i in range(len(m_a)):  # iterate over rows of m_a
        new_row = []
        for j in range(len(m_b[0])):  # iterate over columns of m_b
            elem = 0
            for k in range(len(m_b)):  # iterate over the shared dimension
                elem += m_a[i][k] * m_b[k][j]
            new_row.append(elem)
        result.append(new_row)

    return result

