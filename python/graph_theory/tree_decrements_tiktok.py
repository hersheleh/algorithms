#!/bin/python3

"""TikTok Coding Test problem 3: Tree Decrements."""
import math
import os
import random
import re
import sys
from g_graph import g_Graph
#
# Complete the 'getMinCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY val
#  2. UNWEIGHTED_INTEGER_GRAPH t
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#


def getMinCost(val, t_nodes, t_from, t_to):
    """Calculate the minimum tree decrements."""
    # create graph from given data
    tree = g_Graph(val, t_nodes, t_from, t_to)
    # run BFS on node 1
    odd_nodes = set()

    for i in range(len(val)):
        if (val[i] % 2) != 0:
            node = i + 1
            odd_nodes.add(node)
            tree.breath_first_search(node)

    for node in odd_nodes:
        print(node)


if __name__ == '__main__':
    val = [3, 2, 4, 2, 5]
    t_nodes = 5
    t_from = [1, 1, 3, 3]
    t_to = [2, 3, 4, 5]
    min_cost = getMinCost(val, t_nodes, t_from, t_to)
