from src import GraphInterface
from random import randint


class DiGraph(GraphInterface.GraphInterface):

    def __init__(self):
        self.nodes = dict()
        self.edges = dict()
        self.edgesi = dict()
        self.modeCount = 0
        self.edgesSize = 0

    def v_size(self):
        return len(self.nodes)

    def e_size(self):
        return self.edgesSize

    def get_all_v(self):
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        return self.edgesi[id1]

    def all_out_edges_of_node(self, id1: int):
        return self.edges[id1]

    def get_mc(self):
        return self.modeCount

    def add_edge(self, id1: int, id2: int, weight: float):
        if weight < 0:
            print("weight < 0")
            return False
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
            return False
        else:
            if id2 not in self.edges[id1].keys():
                self.edgesSize += 1
                self.edges[id1].update({id2: weight})
                self.edgesi[id2].update({id1: weight})
                self.modeCount += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None):
        if not (self.nodes.__contains__(node_id)):
            if pos is not None:
                self.nodes.update({node_id: {pos}})
            else:
                self.nodes.update({node_id:
                                       [randint(0, 10000),
                                        randint(0, 10000)]
                                   })
            self.edges.update({node_id: {}})
            self.edgesi.update({node_id: {}})
            self.modeCount = self.modeCount + 1
            return True
        return False

    def remove_node(self, node_id: int):
        if node_id in self.nodes:
            for i in self.edgesi[node_id].keys():
                self.edges[i].pop(node_id)
                self.edgesSize -= 1

            for i in self.edges[node_id].keys():
                self.edgesi[i].pop(node_id)
                self.edgesSize -= 1

            self.edgesi.pop(node_id)
            self.edges.pop(node_id)
            self.nodes.pop(node_id)
            self.modeCount += 1
            return True

        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 not in self.edgesi[node_id2].keys() or node_id2 not in self.edges[node_id1].keys():
            return False
        else:
            self.edges[node_id1].pop(node_id2)
            self.edgesi[node_id2].pop(node_id1)
            self.modeCount += 1
            self.edgesSize += 1
            return True
