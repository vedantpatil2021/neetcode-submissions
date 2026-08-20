class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = prices
        cur_val = n[0]       # cheapest buying price seen so far
        max_profit = 0       # best profit seen so far

        for i in range(len(n)):
            # Buying
            if n[i] < cur_val:
                cur_val = n[i]

            # Selling
            profit = n[i] - cur_val

            if profit > max_profit:
                max_profit = profit

        return max_profit