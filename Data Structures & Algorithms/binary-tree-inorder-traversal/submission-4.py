# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack = []
        # result = []
        # current = root
        # while current or stack:
        #     while current:
        #         stack.append(current)
        #         current = current.left
            
        #     current = stack.pop()
        #     result.append(current.val)
        #     current = current.right
        # return result
        nodes = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        inorder(root)
        return nodes