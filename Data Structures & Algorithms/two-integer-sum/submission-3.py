class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic = {}
        for index in range(len(nums)):
            subResult = target - nums[index]

            if subResult in myDic:
                return [myDic[subResult], index]

            myDic[nums[index]] = index
             

        # for i in range(0, len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
