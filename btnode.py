"""Module for the node for a binary tree"""


class BTNode:
    """Represents a node for a linked binary search tree."""
    def __init__(self, data, left=None, right=None):
        """(BTNode, str)

        A new node for binary tree.
        """
        self.data = data
        self.left = left
        self.right = right
