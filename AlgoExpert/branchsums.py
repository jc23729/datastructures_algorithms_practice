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

# were going to try to solve this recursively...
# we are going to be passing the running sum, which is the sum of all the sums above its
# also we want to be have a running list


# def branchSum(root):
#     if root == None:
#         return []
#     else:
#         return branchSum(root.left) + [root.value] + branchSum(root.right)


def branchSum(root):
    # decalre a running sum list
    sums = []
    # our actual function
    # so we start with the root node and initialize it to zero because we have no running sum
    # then we declare a list, sums append values to this list
    def calculateBranchSums(root, 0, sums)
    return sums
    # our actual recursive function
    def calcualteBranchSum(node, runningSum, sums):
    if node == None:
        return
    # so we have our running sum, and we append it with the new node 
    newRunningSum = runningSum + node.value
    # if our node is a leaf node lets add this new running sum to ours sums list
    # we determine if its a leaf node if there is no chile nodes to the left or right
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)



# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def branchSum(root):

#     sums = []
#     calculateBranchSums(root, 0, sums)
#     return sums

# def calcualteBranchSums(node, runningSum, sums):
#     if node is None:
#         return
    
#     newRunningSum = runningSum + node.value
#     if node.left is None and node.right is None:
#         sums.append(newRunningSum)
#         return

#     calculateBranchSums(node.left, newRunningSum, sums)
#     calculateBranchSums(node.right, newRunningSum, sums)
