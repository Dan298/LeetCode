def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i - 1] <= prices[i]:
            profit += prices[i] - prices[i - 1]

    return profit


class Solution:
    pass


print(max_profit([1, 2, 3, 4, 5]))