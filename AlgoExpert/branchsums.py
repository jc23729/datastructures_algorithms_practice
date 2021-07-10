# Write a function that takes in a binary tree and returns a list of its branch sum ordered from leftmost to rightmost branch sum.
# A branch is a sum of all the values in a binary tree branch, 
# a binary tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node

# Each BinaryTree node has an integer value, a left child node, and a right child node.
# Children nodes can either be BinaryTree nodes themselves or None/null


# Sample input

# tree =    (1)
#       (2)      (3)
#     (4) (5) (6) (7)
#   (8)(9) (10)

# Sample output = [15, 16, 18, 10, 11]

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSum(root):


