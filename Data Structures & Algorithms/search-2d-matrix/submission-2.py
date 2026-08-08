class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        possibleM = []

        for x in matrix:
            if target >= x[0] and target <= x[-1]:
                possibleM = x
                break
        
        l, r = 0, len(possibleM) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if possibleM[m] > target:
                r = m - 1
            elif possibleM[m] < target:
                l = m + 1
            else:
                return True
        return False