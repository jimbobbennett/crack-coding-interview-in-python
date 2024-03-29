import numpy as np

# Assumptions:
# - Empty cells have 0
# - Don't need to solve it
# - Don't have to check for valid solution

# Check if row/column/block is valid
def is_sub_part_valid(sub_part: np.array) -> bool:
    """Checks a slice of the array """
    nonzero_elements = [item for item in sub_part if item != 0]
    return len(set(nonzero_elements)) == len(nonzero_elements)


# Loop through rows/columns/blocks
def is_grid_valid(puzzle : np.array) -> bool:
    """
    Checks for valid rows, columns, and blocks
    in a sudoku puzzle expressed as a numpy array
    """
    for i in range(9):
        # Check row
        if not is_sub_part_valid(puzzle[i, :]):
            return False
        # Check column
        if not is_sub_part_valid(puzzle[:, i]):
            return False
        # Check block
        # Get the starting index for each grid
        j, k = (i // 3) * 3, (i % 3) * 3
        if not is_sub_part_valid(puzzle[j:j+3, k:k+3].ravel()):
            return False
    return True
