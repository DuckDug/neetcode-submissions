class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[r] > nums[m]:
                r = m
            else: 
                l = m + 1
        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        else:
            return binary_search(pivot, len(nums) - 1)