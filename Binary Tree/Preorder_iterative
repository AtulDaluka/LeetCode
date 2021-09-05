class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_array = []
        if root is None:
            return out_array
        else:
            stack = [root]
            while (len(stack)>0):
                cur_node = stack.pop()
                out_array += [cur_node.val]
                if(cur_node.right != None):
                     stack += [cur_node.right]
                if(cur_node.left != None):
                     stack += [cur_node.left]
            return out_array
