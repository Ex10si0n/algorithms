class Solution:
    def maxProfit(self, prices):
        max = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max += prices[i] - prices[i - 1]
        return max

if __name__ == '__main__':
    sol = Solution()
    ans = sol.maxProfit([1, 2, 3])
    print(ans)
