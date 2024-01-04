"""Tree class implemented using a simple 1D array."""


class Tree:
    """A binary tree."""

    def __init__(self, input_array):
        """Construct a tree from the input_array, initialize rootnode index."""
        self.tree = input_array
        self.node = 0

    def __repr__(self):
        """Return string representation of tree as array."""
        return repr(self.tree)

    def get_node_index(self):
        """Return the current node."""
        return self.node

    def get_left_node_index(self):
        """Return index of left node. Or index of node if it's a leaf."""
        if (not isinstance(self.node, int)):
            raise TypeError(
                f"node is wrong type expexted int got {type(self.node)}")
        if (self.node >= len(self.tree) and self.node < 0):
            raise IndexError("node not in self.tree")
        left_node = 2*self.node+1
        if (left_node) >= len(self.tree):
            return self.node
        return left_node

    def get_right_node_index(self):
        """Return index of right node. Or index of node if it's a leaf."""
        if (not isinstance(self.node, int)):
            raise TypeError(
                f"node is wrong type expexted int got {type(self.node)}")
        if (self.node >= len(self.tree) and self.node < 0):
            raise IndexError("node not in self.tree")
        right_node = 2*self.node+2
        if (right_node) >= len(self.tree):
            return self.node
        return right_node

    def goto_left_node(self):
        """Set current node to left node."""
        self.node = self.get_left_node_index()

    def goto_right_node(self):
        """Set curruent node to right node."""
        self.node = self.get_left_node_index()
