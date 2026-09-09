class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            minHeight = min(heights[left], heights[right])
            distance = right - left
            area = minHeight * distance
            maxArea = max(maxArea, area)
            left += 1
            
        return  maxArea

        