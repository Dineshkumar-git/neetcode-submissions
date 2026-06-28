class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_wall = r_wall = 0
        max_left = [0] * n
        max_right = [0] * n


        for l in range(n):
            r = -l -1
            max_left[l] = l_wall
            max_right[r] = r_wall

            l_wall = max(l_wall, height[l])
            r_wall = max(r_wall, height[r])

        summ = 0

        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot-height[i])

        return summ



        