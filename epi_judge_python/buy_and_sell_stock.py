from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price, max_profit = float('inf'), 0.0

    for price in prices:
        sell_today = price - min_price
        max_profit = max(max_profit, sell_today)
        min_price = min(min_price, price)

    return max_profit



def find_longest_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0

    max_seq = 1
    current_seq = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_seq += 1
        else:
            max_seq = max(max_seq, current_seq)
            current_seq = 1

    return max_seq if max_seq >= current_seq else current_seq

A = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2]
print(find_longest_sub_array(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
