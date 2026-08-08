class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        left, right = 0, len(heights) - 1

        while(left < right):
            rightHeight = heights[right]
            leftHeight = heights[left]
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            
            if area > maxA:
                maxA = area
            if rightHeight > leftHeight:
                left += 1
            else:
                right -= 1

        return maxA