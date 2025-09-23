import pytest

def test_my_list():
    expected_array = np.array([1,2,3,4,5])
    actual_array = np.array([1,2,3,4,5])
    np.testing.assert_array_equal(actual_array, expected_array)

def test_matrix_properties():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    assert arr.shape == (2, 4)  # Test the shape (rows, columns)
    assert arr.ndim == 2       # Test the number of dimensions
    assert arr.dtype == np.int64 # Test the data type (adjust as needed)