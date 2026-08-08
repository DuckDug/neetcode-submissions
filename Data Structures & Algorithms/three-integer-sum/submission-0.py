class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for index, leftNumber in enumerate(nums[:-2]):
            middle = index + 1
            right = len(nums) - 1
            target = abs(leftNumber)


            while middle < right:
                middleNumber = nums[middle]
                rightNumber = nums[right]
                if leftNumber + middleNumber + rightNumber == 0:
                    sortedResult = [leftNumber, middleNumber, rightNumber]
                    sortedResult.sort()
                    if sortedResult not in results:
                        results.append(sortedResult)
                    middle += 1
                if middleNumber + rightNumber < target:
                    middle += 1
                if middleNumber + rightNumber > target:
                    right -= 1 

        return results