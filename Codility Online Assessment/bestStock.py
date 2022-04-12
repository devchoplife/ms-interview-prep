"""
Given an array price[] of length N, representing the prices of the stocks on different days, the task is to 
find the maximum profit possible for buying and selling the stocks on different days using transactions 
where at most one transaction is allowed.

Examples:

Input: prices[] = {7, 1, 5, 3, 6, 4]
Output: 5
Explanation:
The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
Therefore, maximum possible profit = 6 - 1 = 5. 

Input: prices[] = {7, 6, 4, 3, 1} 
Output: 0
Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.
"""

def findMaxProfit(prices, i, k, buy, v):
    if (i >= len(prices) or k <= 0):
        return 0
    
    if (v[i][buy] != -1):
        return v[i][buy]
    
    # If a stock is already bought
    if buy:
        v[i][buy] = max(-prices[i] + findMaxProfit(prices, i + 1, k, not buy, v), findMaxProfit(prices, i + 1, k, buy, v))
        return v[i][buy]
    
    else:
        # Buy now
        v[i][buy] = max(prices[i]
                        + findMaxProfit(prices, i + 1, k - 1, not buy, v), 
                        findMaxProfit(prices, i + 1, k, buy, v))
        return v[i][buy]
    

# Functiion to find the maximum profit in the buy and sell stock
def maxProfit(prices):
    n = len(prices)
    v = [[-1 for x in range(2)]for y in range(n)]
    
    return findMaxProfit(prices, 0, 1, 1, v)

prices = [7, 1, 5, 3, 6, 4]
ans = maxProfit(prices)
print(ans)