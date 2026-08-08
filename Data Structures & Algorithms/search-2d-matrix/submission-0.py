class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetInMatrix = False
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                left, right = 0, len(row) - 1
                while left <= right:
                    middle = left + ((right - left) // 2)
                    if row[middle] < target:
                        left = middle + 1
                    elif row[middle] > target:
                        right = middle - 1
                    else: 
                        targetInMatrix = True
                        break
                break
        return targetInMatrix