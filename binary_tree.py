'''
Distribution file for the alternating module. You should not modify this file.

Your answer should be placed in the problem4.py file.
'''

class BinaryTree:
    '''
    Class for representing binary trees.

    Public attributes:
        nodeNum: the number assigned to this node
        value: the value associated with this node represented as an integer
        left: the left child of the node (will be None, if the
            node does not have a left child)
        right: the right child of the node (will be None, if the
            node does not have a right child)

    Public methods: (see below)
    '''

    def __init__(self, node_num: int, value: int) -> None:
        '''
        Constructor for BinaryTree class.

        Arguments:
            node_num: the number assigned to this node
            value: the value associated with this node represented as an integer

        Returns:
            None
        '''
        self.node_num = node_num
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, left: 'BinaryTree') -> None:
        '''
        Add a left child to a node.

        Arguments:
            left: the left child of the node

        Returns:
            None
        '''
        # Sanity check
        assert self.left is None

        self.left = left

    def add_right(self, right: 'BinaryTree') -> None:
        '''
        Add a right child to a node.

        Arguments:
            right: the right child of the node

        Returns:
            None
        '''
        # Sanity check
        assert self.right is None

        self.right = right