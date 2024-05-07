import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    left, right = 0, len(A) - 1
    i = 0

    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    while i <= right:
        if A[i] < pivot:
            swap(i, left)
            left += 1
            i += 1
        elif A[i] > pivot:
            swap(i, right)
            right -= 1
        else: # A[i] == pivot
            i += 1

def four_color_flag(A: List[int]) -> None:
    p0, p1, p2 = 0, 0, 0
    i = 0

    def swap(i, j):
        A[i], A[j] = A[j], A[i]

    while i < len(A):
        if A[i] == 0:
            swap(i, p0)
            if p0 < p1: swap(i, p1)
            if p1 < p2: swap(i, p2)
            p0 += 1
            p1 += 1
            p2 += 1
        elif A[i] == 1:
            swap(i, p1)
            if p1 < p2: swap(i, p2)
            p1 += 1
            p2 += 1
        elif A[i] == 2:
            swap(i, p2)
            p2 += 1
        i += 1

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
