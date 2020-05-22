"""Module that represents linked binary tree for the game"""


class LinkedBinaryTree:
    """Represents Linked Binary tree"""
    def __init__(self, root):
        """(LinkedBinaryTree, root)

        A new binary tree with root.
        """
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """(LinkedBinaryTree, BTNode)

        Inserts node to the left part of the tree.
        """
        if self.left_child is None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            tree = LinkedBinaryTree(new_node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, new_node):
        """(LinkedBinaryTree, BTNode)

        Inserts node to the right part of the tree.
        """
        if self.right_child is None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            tree = LinkedBinaryTree(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_right_child(self):
        """(LinkedBinaryTree)

        Returns right elements of the tree.
        """
        return self.right_child

    def get_left_child(self):
        """(LinkedBinaryTree)

        Returns left elements of the tree.
        """
        return self.left_child

    def leaves(self):
        """(LinkedBinaryTree) -> list

        Returns the list of leaves of the tree.
        """
        tree_leaves = []

        def find_leaves(root):
            """
            Helper function to find the leaves
            of the tree.
            """
            if root.get_right_child():
                find_leaves(root.right_child)
            if root.get_left_child():
                find_leaves(root.left_child)

            if root.get_left_child() is None:
                if root.key not in tree_leaves:
                    tree_leaves.append(root.key)
                    return

            if self.get_right_child() is None:
                if root.key.data not in tree_leaves:
                    tree_leaves.append(root.key)
                    return

        find_leaves(self)
        return tree_leaves
