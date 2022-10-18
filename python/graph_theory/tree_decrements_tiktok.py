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
    tree.breath_first_search(1)
    tree.nodes[1].distance
    odd_nodes = set()

    for i in val:
        if (val[i] % 2) != 0:
            node = i + 1
            odd_nodes.append(node)
            tree.breath_first_search(node)

    for node in odd_nodes:
        for
        tree.nodes[node].distance

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('stdout', 'w')
    """
    3
    2
    1
    1
    3 2
    1 2
    1 3
    """
    val_count = int(input().strip())
    print("val_count %s " % val_count)

    val = []

    for _ in range(val_count):
        val_item = int(input().strip())
        print("val_item %s " % val_item)
        val.append(val_item)

    t_nodes, t_edges = map(int, input().rstrip().split())
    print("t_nodes: %s, t_edges: %s" % (t_nodes, t_edges))

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())
        print("t_from[i]: %s, t_to[i]:%s" % (t_from[i], t_to[i]))

        # result = getMinCost(val, t_nodes, t_from, t_to)

    # print(str(result))
    # fptr.write(str(result) + '\n')

    # fptr.close()
