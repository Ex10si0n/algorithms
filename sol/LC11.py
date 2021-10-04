class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, height[i] * (j - i))
                i += 1
            else:
                ans = max(ans, height[j] * (j - i))
                j -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.maxArea([1,8,6,2,5,4,8,3,7])
    print(ans)
