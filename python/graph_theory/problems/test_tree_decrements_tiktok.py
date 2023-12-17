import unittest
from tree_decrements_tiktok import getMinCost


class TestGetMinCost(unittest.TestCase):
    def test_3nodes_2edges(self):
        val = [3, 1, 2]
        t_nodes = 3
        t_from = [1, 1]
        t_to = [2, 3]
        min_cost = getMinCost(val, t_nodes, t_from, t_to)
        self.assertEquals(min_cost, 1)

    def test_5nodes_4edges(self):
        val = [3, 2, 4, 2, 5]
        t_nodes = 5
        t_from = [1, 1, 3, 3]
        t_to = [2, 3, 4, 5]
        min_cost = getMinCost(val, t_nodes, t_from, t_to)
        self.assertEquals(min_cost, 2)
