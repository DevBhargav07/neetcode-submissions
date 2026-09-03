# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # finding the height and using the height to find the max height will solve it.
        self.res = 0
        def height(curr):
            if curr is None:
                return 0
            left = height(curr.left)
            right = height(curr.right)
            self.res = max(self.res, (left+right)) # finding the diameter is adding left & right taking max of it
            return 1 + max(left, right) # finding the height is taking the max
        height(root)
        return self.res