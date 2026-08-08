class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        nums.sort()
        result = []

        while l < r - 1:
            m = l + 1
            r = len(nums) - 1
            leftNumber = nums[l]
            target = abs(nums[l])
            while m < r:
                middleNumber = nums[m]
                rightNumber = nums[r]
                total = middleNumber + rightNumber
                if leftNumber + middleNumber + rightNumber == 0:
                    appendArr = [leftNumber, middleNumber, rightNumber]
                    appendArr.sort()
                    if appendArr not in result:
                        result.append(appendArr)
                    m += 1
                if total < target:
                    m += 1
                if total > target:
                    r -= 1
            l += 1
        return result