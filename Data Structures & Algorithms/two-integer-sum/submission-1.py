class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = list()

        for index,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                result.extend([seen[diff],index])
            seen[num] = index
        return result
        