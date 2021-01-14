from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    g = DiGraph()
    for i in range(6):
        g.add_node(i)
    g.add_edge(0, 1, 2.5)
    g.add_edge(1, 2, 1.5)
    g.add_edge(1, 3, 4.5)
    g.add_edge(2, 3, 1.5)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 3.3)
    g.add_edge(4, 2, 2.7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(7)
    g.add_edge(7, 8, 1.1)
    g.add_edge(8, 9, 1.6)
    g.remove_node(9)
    g.remove_edge(7, 8)

    # shortestPath(0,3) = (5.5,[0,1,2,3])
    # connectedComponent = [[0],[1],[2,3,4]]
    def test_v_size(self):
        self.assertEqual(8, self.g.v_size())

    def test_e_size(self):
        self.assertEqual(9, self.g.e_size())

    def test_all_in_edges_of_node(self):
        i = self.g.all_in_edges_of_node(4)
        self.assertEqual(i[2], 3)
        self.assertEqual(i[3], 3.3)

    def test_all_out_edges_of_node(self):
        o = self.g.all_out_edges_of_node(0)
        self.assertEqual(o[1], 2.5)

    def test_get_mc(self):
        self.assertEqual(self.g.get_mc(), 20)

    def test_add_edge(self):
        self.g.add_edge(4, 2, 2.8)
        self.assertEqual(self.g.all_out_edges_of_node(4)[2], 2.7)

    def test_remove_node(self):
        b = 9 not in self.g.all_out_edges_of_node(8)
        self.assertEqual(b, True)

    def test_remove_edge(self):
        b = 7 not in self.g.all_in_edges_of_node(8)
        self.assertEqual(b,True)