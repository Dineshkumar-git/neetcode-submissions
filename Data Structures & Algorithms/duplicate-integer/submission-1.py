class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list2 = []

        for i in nums:
            if i in list2:
                return True
            else:
                list2.append(i)
        return False

        