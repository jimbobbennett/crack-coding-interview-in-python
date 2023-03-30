import validator
import pytest
import numpy as np

valid_puzzle = np.array(
        [[0,0,0,2,0,0,7,9,0],
        [0,0,0,1,0,6,0,0,4],
        [8,1,5,0,0,0,0,0,3],
        [0,0,1,5,6,0,0,0,0],
        [0,4,0,0,0,0,0,7,0],
        [0,0,0,0,9,3,8,0,0],
        [1,0,0,0,0,0,9,2,6],
        [9,0,0,6,0,8,0,0,0],
        [0,6,4,0,0,2,0,0,0]]
    )

invalid_puzzle = np.array(
        [[0,0,0,2,0,0,7,9,0],
        [0,0,0,1,0,6,0,0,4],
        [8,1,5,0,0,0,0,0,3],
        [0,0,1,5,6,0,0,0,0],
        [0,4,0,0,0,0,0,7,0],
        [0,0,0,0,9,3,8,0,0],
        [1,0,0,0,0,0,9,2,6],
        [9,0,0,6,0,8,0,0,0],
        [0,6,4,0,6,2,0,0,0]]
    )

valid_slices = np.array([1,2,3,4,5,6,7,8,9])

invalid_slices = np.array([1,2,2,4,5,6,7,8,9])

@pytest.mark.parametrize(
        'slice, test_case',
        [
            (valid_slices, True),
            (invalid_slices, False),
        ]
)
def tests_zero_elements(slice, test_case):
    assert validator.is_sub_part_valid(slice) == test_case

@pytest.mark.parametrize(
        'puzzle, test_case', 
        [
            (valid_puzzle, True),
            (invalid_puzzle, False),
        ]
)
def tests_zero_elements(puzzle, test_case):
    assert validator.is_grid_valid(puzzle) == test_case