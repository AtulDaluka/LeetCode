# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal_helper(self, root, out_array):
        if(root!=None):
            out_array.append(root.val)
            self.preorderTraversal_helper(root.left, out_array)
            self.preorderTraversal_helper(root.right, out_array)
            # print(out_array)
        return out_array
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_array = []
        if root is None:
            return out_array
        else:
            self.preorderTraversal_helper(root, out_array)
            return out_array
