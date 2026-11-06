class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            next_dp = set()
            for num in dp:
                if (nums[i] + num) == target:
                    return True
                next_dp.add(nums[i] + num)
                next_dp.add(num)
            dp = next_dp
        return True if target in dp else False
        