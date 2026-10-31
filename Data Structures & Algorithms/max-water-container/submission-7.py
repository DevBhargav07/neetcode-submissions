class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            width = right - left
            curr_area = min_height * width
            area = max(area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area