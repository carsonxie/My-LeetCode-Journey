class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBSTHelper(self, node, low, high):
        #base case
        if not node:
            return True
        if ((node.val > low and node.val < high) and 
            self.isValidBSTHelper(node.left, low, node.val) and #left sub tree show always less than current node
            self.isValidBSTHelper(node.right, node.val, high)): #right subtree should greater than current node
            return True
        return False

    def isValidBST(self, node):
        return self.isValidBSTHelper(node, float('-inf'), float('inf'))


#  5
# / \
#4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))



#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False
