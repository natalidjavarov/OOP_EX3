import math
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
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
    gAlgo = GraphAlgo(g)

    def test_shortest_path(self):
        s1 = self.gAlgo.shortest_path(0, 3)
        s2 = self.gAlgo.shortest_path(1, 0)
        s3 = self.gAlgo.shortest_path(0, 0)
        self.assertEqual(s1, (5.5, [0, 1, 2, 3]))
        self.assertEqual(s2, (math.inf, []))
        self.assertEqual(s3, (0, [0]))

    def test_connected_component(self):
        c = self.gAlgo.connected_component(0)
        self.assertEqual(c, [0])

    def test_connected_components(self):
        c1 = self.gAlgo.connected_components()
        counter = 0
        ans = False
        for i in c1:
            if i == [0]:
                counter += 1
            if i == [1]:
                counter += 1
            if i == [5]:
                counter += 1
        if counter == 3 and len(c1) == 4:
            ans = True
        print(self.gAlgo.connected_components())
        self.assertEqual(ans, True)
