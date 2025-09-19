# use pip package to add a Python package of your choice to your project, and write a 
# script to demonstrate how to use it
import pytest
import numpy as np

# using numpy in an array
my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list)
print(f"Here is an example of a NumPy array: {numpy_array}")

print()

matrix = np.array( [ [1,2,3,4], 
                     [5,6,7,8], 
                     [9,10,11,12] ] )
print("Here is an example of a NumPy two-dimensional array ")
print(matrix)

#==============================================================================
def test_my_list():
    expected_array = np.array([1,2,3,4,5])
    actual_array = np.array([1,2,3,4,5])
    np.testing.assert_array_equal(actual_array, expected_array)

def test_matrix_properties():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    assert arr.shape == (2, 4)  # Test the shape (rows, columns)
    assert arr.ndim == 2       # Test the number of dimensions
    assert arr.dtype == np.int64 # Test the data type (adjust as needed)