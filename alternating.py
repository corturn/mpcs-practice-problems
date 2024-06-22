from binary_tree import BinaryTree
from typing import Optional


def count_alternating_paths(tree: Optional[BinaryTree]) -> int:
    '''
    Return the number of root to leaf paths in the tree that alternate between
    even and odd values.

    Arguments:
        tree: the tree to count the number of alternating paths in

    Returns:
        The number of alternating paths in the tree
    '''
    # TODO: Write your solution here

    if tree is None:
        return 1
    if tree.left is None and tree.right is None:
        return 1
    r_even = even(tree.value)
    num_paths = 0
    if tree.left is not None and r_even != even(tree.left.value):
        num_paths += count_alternating_paths(tree.left)
    if tree.right is not None and r_even != even(tree.right.value):
        num_paths += count_alternating_paths(tree.right)
    return num_paths

def even(n):
    return n % 2 == 0


def mk_node(node_num: int, val: int,
            left: Optional[BinaryTree],
            right: Optional[BinaryTree]) -> BinaryTree:
    """
    Create a binary tree node, given the node number, value,
    left child, and right child.
    """
    t = BinaryTree(node_num, val)
    t.add_left(left)
    t.add_right(right)
    return t

def mk_sample_tree() -> BinaryTree:
    '''
    Make the sample tree from the problem statement.

    Returns:
        The root node of the sample tree
    '''
    return mk_node(1, 10,
           mk_node(2, 45,
               mk_node(4, 10,
                   mk_node(7, 33, None, None),
                   mk_node(8, 20, None, None)),
               mk_node(5, 50, None, None)),               
           mk_node(3, 55,
               None,
               mk_node(6, 25,
                   mk_node(9, 80, None, None),
                   None)))

print(count_alternating_paths(mk_sample_tree()))