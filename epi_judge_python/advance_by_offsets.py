from typing import List

from test_framework import generic_test

def can_reach_end(A: List[int]) -> bool:
    goal = len(A) - 1
    for i in reversed(range(len(A))):
        if i + A[i] >= goal:
            goal = i

    return goal == 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
