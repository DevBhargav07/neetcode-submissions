# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # using dfs
        def dfs(curr):
            if curr is None:
                return (True, 0)
            left, right = dfs(curr.left), dfs(curr.right)
            balanced = left[0] and right[0] and abs((left[1] - right[1])) <= 1

            return (balanced, 1+max(left[1], right[1]))
        
        return dfs(root)[0]









        def height(curr):
            if curr is None:
                return [True, 0]
            left = height(curr.left)
            right = height(curr.right)

            balanced = left[0] and right[0] and abs((left[1] - right[1])) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        return height(root)[0]

        #     # we got the left height & right height
        #     # compare and check abs diff is 1 or more
        #     if abs(left - right) > 1:
        #         return False
        #     return  1 + max(left, right)
        # boolean = height(root)
        # print(boolean)
        # return False
        