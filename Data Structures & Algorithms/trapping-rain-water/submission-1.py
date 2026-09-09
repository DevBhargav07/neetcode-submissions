class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        for i in range(len(height)-1):

            left = height[i]
            for j in range(i):
                left = max(left, height[j])
            
            right = height[i]
            for j in range(i+1, len(height)-1):
                right = max(right, height[j])
            
            res += (min(left, right) - height[i])
        return res



