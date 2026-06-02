class Solution:
    def rob(self, nums: List[int]) -> int:

#botton top (constant space)
# T - O(n)
# S - O(1)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2,n):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr


"""
# botton top (tabulization)
# T - O(n)
# S - O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
"""

"""
#top bottom DP (memorization)
# T - O(n)
# S - O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = {0:nums[0], 1:max(nums[0], nums[1])}
        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i-1), helper(i-2) + nums[i])
                return memo[i]

        return helper(n-1)
"""

""" 
# Recursion
# T - O(2^n)
# S - O(n)
        n = len(nums)

        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            return max(helper(i-1), helper(i-2) + nums[i])

        return helper(n-1)
"""



        