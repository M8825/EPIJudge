from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    A.sort()

    left, right = 0, len(A) - 1

    while left <= right:
        sum = A[left] + A[right]

        if sum < t:
            left += 1
        elif sum > t:
            right -= 1
        else: # sum == target
            return True

    return False




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
