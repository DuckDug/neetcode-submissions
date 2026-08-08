class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxBuy = prices[0]
        maxProfit = -1 

        for x in prices: 

            if x > maxBuy:
                maxBuy = x
            if x < minBuy:
                minBuy = x
                maxBuy = x
            profitResult = maxBuy - minBuy
            if profitResult > maxProfit:
                    maxProfit = profitResult

        return maxProfit