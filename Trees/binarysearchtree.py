'''
                                            Binary Search Tree
A binary tree is a tree data structure in which each node can have a maximum of 2 children.  It means that each node in a binary tree can have either one, or two or no children. Each node in a binary tree contains data and references to its children. Both the children are named as left child and the right child according to their position.

Time Complexity - O(logn)
'''
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root


def search(root, value):
    # Condition 1
    if root == None:
        return False
    # Condition 2
    elif root.data == value:
        return True
    # Condition 3
    elif root.data < value:
        return search(root.rightChild, value)
    # Condition 4
    else:
        return search(root.leftChild, value)


def findLargestElement(root):
    # check if binary search tree is empty
    if root == None:
        return False
    # check if current node is rightmost node
    elif root.rightChild == None:
        return root.data
    # check right subtree of current node
    else:
        return findLargestElement(root.rightChild)


root = insert(None, 15)


def findSmallestElement(root):
    # check if binary search tree is empty
    if root == None:
        return False
    # check if current node is leftmost node
    elif root.leftChild == None:
        return root.data
    # check right subtree of current node
    else:
        return findSmallestElement(root.leftChild)


insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print(search(root, 14))  # True
print(findLargestElement(root))  # 60
print(findSmallestElement(root))  # 6
