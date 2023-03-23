import numpy as np

# Assumptions:
# - Empty cells have 0
# - Don't need to solve it
# - Don't have to check for valid solution

# Check if row/column/block is valid

def is_sub_part_valid(sub_part: list):
    return len(set(sub_part)) == len(sub_part)

# Loop through rows/columns/blocks

def check_grid(puzzle : np.array):
    for i in range(9):
        j, k = (i // 3) * 3, (i % 3) * 3
        is_valid = false
        # Check row
        is_sub_part_valid()
        # Check column
        is_sub_part_valid()
        # Check block
        is_sub_part_valid()


# Collect results
