def maxprofit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)

        min_price = min(min_price, price)
    return max_profit


h = list(map(int, input('Enter numbers separated by spaces: ').split()))  # 7 1 5 3 6 4
print(maxprofit(h))