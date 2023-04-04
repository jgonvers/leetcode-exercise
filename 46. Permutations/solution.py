class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        sol = []
        for i in range(len(nums)):
            less = self.permute(nums[:i]+nums[i+1:])
            for e in less:
                e.append(nums[i])
            sol.extend(less)
        return sol
            