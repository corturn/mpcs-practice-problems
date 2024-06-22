class Tree:
    '''
    Class representing a tree node. 

    Public attributes:
        node_num: the node number of the node
        value: the value of the node
        children: a list of children of the node

    Public methods:
        add_child(other_tree): adds other_tree to the list of children
        num_children(): returns the number of children
    '''    
    def __init__(self, nn: int, v: int) -> None:
        '''
        Initializes a Tree object with node number nn and value v.

        Arguments:
            nn: the node number of the node
            v: the value of the node

        Returns:
            None
        '''
        self.node_num = nn
        self.value = v 
        self.children: list['Tree'] = []

    def add_child(self, child_tree: 'Tree') -> None:
        '''
        Adds other_tree to the list of children of this node.

        Arguments:
            child_tree: the tree to be added as a child

        Returns:
            None
        '''
        self.children.append(child_tree)

    def num_children(self) -> int:
        '''
        Returns the number of children of this node.

        Arguments:
            None

        Returns:
            the number of children of this node
        '''
        return len(self.children)

    def __repr__(self) -> str:
        '''
        Returns a string representation of the tree rooted at this node.
        
        Arguments:
            None
            
        Returns:
            a string representation of the tree rooted at this node
        '''
        children = ','.join([str(child) for child in self.children])
        return f'({self.node_num},{self.value},[{children}])'