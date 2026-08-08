class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longestStreak = 1
        currentStreak = 1
        nums = sorted(list(set(nums)))
        print(nums)
        for index in range(0,len(nums) - 1):
            if abs(nums[index] - nums[index + 1]) == 1:
                currentStreak += 1
                if longestStreak < currentStreak:
                    longestStreak = currentStreak
            else:
                currentStreak = 1
        return longestStreak