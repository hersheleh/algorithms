#!/bin/python3

"""TikTok Coding Test problem 3: Tree Decrements."""
import math
import os
import random
import re
import sys


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
    a_list = {}             # adjacency list

    for i in range(len(t_from)):    # iterate through edges of graph
        node_from = str(t_from[i])  # convert from node for this edge to str
        node_to = str(t_to[i])      # convert to node for this edge to str

        if a_list.get(node_from) is None:  # check if node is in adj list
            a_list.update({node_from: []})  # if not create an empty list

        node_from_list = a_list.get(node_from)
        node_from_list.append(node_to)  # if yes append to list

    print("A List: %s" % a_list)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('stdout', 'w')

    val_count = int(input().strip())

    val = []

    for _ in range(val_count):
        val_item = int(input().strip())
        val.append(val_item)

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges3

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    result = getMinCost(val, t_nodes, t_from, t_to)

    print(str(result))
    # fptr.write(str(result) + '\n')

    # fptr.close()
