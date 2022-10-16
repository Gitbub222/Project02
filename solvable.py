def get_inversion_count(arr):
    inversion_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inversion_count += 1
    return inversion_count


# This function returns true
# if given 8 puzzle is solvable.
def is_solvable(puzzle):
    # Count inversions in given 8 puzzle
    inv_count = get_inversion_count([j for sub in puzzle for j in sub])

    # return true if inversion count is even.
    return (inv_count % 2 == 0)
