from tree import Tree
def count_monotonic_paths(root):
    '''
    Count the number of paths from the root to a leaf node that are strictly
    monotonically increasing. See the problem description for more details.
    
    Arguments:
        root: the root of the tree
        
    Returns:
        the number of paths from the root to a leaf node that are strictly
        monotonically increasing
    '''
    # TODO: Implement this function
    if root.num_children() == 0:
        return 1
    num_paths = 0
    for c in root.children:
        if c.value > root.value:
            num_paths += count_monotonic_paths(c)
    return num_paths
