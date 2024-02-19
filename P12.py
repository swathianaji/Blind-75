"""
Problem: 121. Best Time to Buy and Sell Stock

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# lets use two pointers for this problem, buy is at first value, and sell is at second value
# let's find profit, if profit is greater than 0, compare it with mx and change accordingly 
# if profit if less than 0 which means that not the lowest value from left side so we reassign sell value to buy


def maxProfit(prices):
    mx = 0
    buy = 0
    sell = 1
    while(sell < len(prices)):
        profit = prices[sell] - prices[buy]
        if profit >= 0:
            mx = max(mx,profit)
        elif profit < 0:
            buy = sell
        sell += 1
    return mx

# Sample test case
print(maxProfit([7,1,5,3,6,4]))
