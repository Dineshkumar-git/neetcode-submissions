# T -> O(2^log(n))
# S -> 0(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarysearch(nums, target, True)
        right = self.binarysearch(nums, target, False)
        return [left, right]

    def binarysearch(self, nums, target, leftbias):
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                i = m
                if leftbias:
                    r = m - 1
                else:
                    l = m + 1
        return i

        