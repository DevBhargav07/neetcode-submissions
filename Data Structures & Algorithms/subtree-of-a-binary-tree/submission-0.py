# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # to find the subtree of another tree - first we try to write the all nodes in a list
        # using the serialize method
        def serialize(node: Optional[TreeNode]) -> list:
            if not node:
                return []
            out, stack = [], [node]
            while stack:
                curr = stack.pop()
                if not curr:
                    out.append(None) # if no values found for left or right childs
                    continue
                out.append(curr.val)                    
                stack.append(curr.left)
                stack.append(curr.right)
            return out
        
        # now we need to find the pattern in that text exists
        # using kmp algorithm for better usage and optimal solution
        def kmp_pattern(text: list, pattern: list) -> bool:
            lps = [0] * len(pattern)

            k = 0
            for i in range(1, len(pattern)): # starts from 1 as needed by the kmp
                while k and pattern[i] != pattern[k]:
                    k = lps[k-1]
                if pattern[i] == pattern[k]:
                    k += 1
                lps[i] = k
            
            # scanning the text now
            k  = 0
            for x in text:
                while k and x != pattern[k]:
                    k = lps[k-1]
                if x == pattern[k]:
                    k += 1
                if len(pattern) == k:
                    return True
            return False
        return kmp_pattern(serialize(root), serialize(subRoot))