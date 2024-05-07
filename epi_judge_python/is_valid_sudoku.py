from typing import List

from test_framework import generic_test
import collections


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)

    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(n):
        for c in range(n):
            num = partial_assignment[r][c]
            if num == 0: continue

            if (num in rows[r] or
                num in cols[c] or
                num in squares[(r // 3, c // 3)]):
                return False

            rows[r].add(num)
            cols[c].add(num)
            squares[(r // 3, c // 3)].add(num)

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
