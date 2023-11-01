import pytest
from hw3 import sum_general_int_list

def test_sum_general_int_list():
    test_list_1 = [[2], 3, [[1,2],5]]
    result = sum_general_int_list(test_list_1)
    expected = 13
    assert result == expected, "Incorrect result"
    
    test_list_2 = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
    result = sum_general_int_list(test_list_2)
    expected = 48
    assert result == expected, "Incorrect result"

