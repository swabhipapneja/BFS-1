# Time Complexity : O(n), n is no of nodes in the tree
# Space Complexity : O(n), because the queue can store all leaf nodes at max in the worst case
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# we are using a queue to do level order traversal of a binary tree
# expected output example = [[1], [3,2], [4,5,6]]
# so we start with initializing this list, and then we need a queue
# we put the root of the tree in the queue
# since we need to differentiate between the levels of the tree, we need to use the size variable
# while the queue is not empty, we do the following operations:
# first, we take size of the queue
# then we start another loop that goes on for size no of times
# then we remove a node from it
# then we add the value of this node to a list, that we initialize for every level
# for every node, we check, if left and right children are valid, we add them to the queue
# at the end of the size loop, we will append the level list to our main list
# at the end we can return the final result list


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        # empty final list to return
        result = []
        # a queue to add the nodes of the tree, intialized with root
        q = deque([root])
        
        # size variable to store the size of queue, and do differentiate the levels
        size = 1
        while q:
            size = len(q)
            # list to store the nodes at every level
            level = []
            # for size number of items in the queue
            for _ in range(size):
                # remove node from the queue, and add to the list
                node = q.popleft()
                level.append(node.val)
                # add left and right child to the queue
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            result.append(level)
        
        return result



        