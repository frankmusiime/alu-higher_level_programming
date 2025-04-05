#!/usr/bin/python3

from lazy_matrix_mul import lazy_matrix_mul

# Valid matrix multiplication - integer values
print(lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
# Expected Output: [[19, 22], [43, 50]]

# Valid matrix multiplication - floats
print(lazy_matrix_mul([[1.0, 2.0], [3.0, 4.0]], [[0.5, 0.5], [0.5, 0.5]]))
# Expected Output: [[1.5, 1.5], [3.5, 3.5]]

# m_a is not a list
try:
    lazy_matrix_mul("not a list", [[1, 2], [3, 4]])
except Exception as e:
    print(e)
# Expected: m_a must be a list

# m_b is not a list of lists
try:
    lazy_matrix_mul([[1, 2], [3, 4]], [1, 2])
except Exception as e:
    print(e)
# Expected: m_b must be a list of lists

# m_a is empty
try:
    lazy_matrix_mul([], [[1, 2], [3, 4]])
except Exception as e:
    print(e)
# Expected: m_a can't be empty

# m_b is [[]]
try:
    lazy_matrix_mul([[1, 2], [3, 4]], [[]])
except Exception as e:
    print(e)
# Expected: m_b can't be empty

# Element in m_a is not int/float
try:
    lazy_matrix_mul([[1, '2'], [3, 4]], [[5, 6], [7, 8]])
except Exception as e:
    print(e)
# Expected: m_a should contain only integers or floats

# m_b has uneven rows
try:
    lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]])
except Exception as e:
    print(e)
# Expected: each row of m_b must be of the same size

# Incompatible sizes for multiplication
try:
    lazy_matrix_mul([[1, 2]], [[1, 2], [3, 4], [5, 6]])
except Exception as e:
    print(e)
# Expected: m_a and m_b can't be multiplied

