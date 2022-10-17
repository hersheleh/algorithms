"""Breadth first search implementation in python."""
from enum import Enum


class Color(Enum):
    """Color Nodes if visited."""

    White = 1                   # Not Discovered
    Grey = 2                    # Discovered
    Black = 3                   # Visited


class Node:
    """Single Node in a g_Graph. Each stores a record of it's BFS run."""

    def __init__(self, index):
        """Construct a Node."""
        self.index = index

        # These are set on g_Graph initialization
        self.adjacent = []          # list of adjancent nodes

        # These are set when breath_first_search is run on this Node
        self.color = {}             # color of nodes during BFS run
        self.distance = {}          # distances to all other nodes
        self.parent = {}            # parents of all other nodes


class g_Graph:
    """Implemtation of a Graph."""

    def __init__(self, val, t_nodes, t_from, t_to):
        """Construct graph representation from t_from & t_to lists."""
        self.nodes = {}         # dictionary of nodes eg. {1: Node()}

        # add all nodes to this graph's nodes dictionary
        for i in range(1, t_nodes+1):  # nodes start at 1
            self.nodes.update({i: Node(index=i)})

        num_edges = len(t_from)
        # iterate through the edges of the graph
        for edge in range(num_edges):
            from_node = t_from[edge]
            to_node = t_to[edge]
            # add to_node to from_node's adjacency list
            self.nodes[from_node].adjacent.append(to_node)

    def breath_first_search(self, source):
        """Breadth First Search algorithm."""
        # iterate over all vertices and initialize
        source_node = self.nodes[source]
        for i in range(len(self.nodes)):
            source_node.color[i] = Color.White
            source_node.distance[i] = float('inf')
            source_node.parent[i] = None

        # initialize & discover the source node
        source_node.color[source] = Color.Grey
        source_node.distance[source] = 0
        source_node.parent[source] = None

        Queue = []              # Create a new empty queue

        Queue.append(source)

        while (len(Queue) > 0):          # while queue is not empty
            current_node = Queue.pop(0)  # dequeue node
            # iterate through adjacent nodes
            for adj_node in self.nodes[current_node].adjacent:
                # if the adjacent node is White (undiscovered)
                if (source_node.color[adj_node] == Color.White):
                    # color it Grey (discover it)
                    source_node.color[adj_node] = Color.Grey
                    # update the adjacent nodes distance from source
                    current_node.distance = source_node.distance[current_node]
                    source_node.distance[adj_node] = current_node.distance + 1
                    # set the adjacent nodes parent to current node
                    source_node.parent[adj_node] = current_node
                    Queue.append(adj_node)
                # color the current node Black (visited)
                source_node.color[current_node] = Color.Black
