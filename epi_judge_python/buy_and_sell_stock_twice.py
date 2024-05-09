from typing import List

from test_framework import generic_test

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_total_profit, min_price = 0.0, float('inf')
    buy_sell_first_scan = [0.0] * len(prices)
    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        max_total_profit = max(max_total_profit, price - min_price)
        buy_sell_first_scan[i] = max_total_profit

    max_price = float('-inf')

    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        max_total_profit = max(
            max_total_profit,
            max_price - price + buy_sell_first_scan[i]
        )

    return max_total_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
