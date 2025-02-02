# Time Complexity : O(n), n is no of nodes in the tree
# Space Complexity : O(n), because the queue can store all leaf nodes at max in the worst case
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        # using dfs - recusrsion approach
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, lvl):
        # base case
        if root is None:
            return
        
        if lvl == len(self.result):
            # if level is same as the size of the result list
            # it means we are at this index for the first time
            # so we create a new list at that index
            # we will create this for the left child, because when we come to the left most element
            # at a level, we wil need to create a new list
            self.result.append([])
        

        # now we have a list at the index equal to the size 
        # so just go the list at that index, and append the value
        # this will happen when we come to the right child, we would have already added a left child
        self.result[lvl].append(root.val)
        self.dfs(root.left, lvl+ 1)
        self.dfs(root.right, lvl + 1)




        