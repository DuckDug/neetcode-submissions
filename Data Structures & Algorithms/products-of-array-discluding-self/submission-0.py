class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        endResult = []
        for x in range(0, len(nums)):
            result = 1
            for y in range(0, len(nums)):
                if x == y:
                    continue
                else:
                    result *= nums[y]
            endResult.append(result)
        return endResult