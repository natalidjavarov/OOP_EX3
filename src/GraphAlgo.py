from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import json
import matplotlib.pyplot as plt
import math


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: tuple = None):
        if g is None:
            self.g = DiGraph()
        else:
            self.g = g

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str):
        self.g = DiGraph()
        with open(file_name) as f:
            data = json.load(f)
            for n in data['Nodes']:
                self.g.add_node(n['id'])
            for e in data['Edges']:
                self.g.add_edge(e['src'], e['dest'], e['w'])

    def save_to_json(self, file_name: str):
        data = {
            "Edges": [],
            "Nodes": []
        }
        for n in self.g.get_all_v().keys():
            data["Nodes"].append({"id": n})
        for n in self.g.get_all_v().keys():
            for n2, w in self.g.all_out_edges_of_node(n).items():
                data["Edges"].append({"src": n, "w": w, "dest": n2})
        with open(file_name, 'w+') as f:
            json.dump(data, f)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        distancedict = {}
        q = []
        list = []
        q.append(id1)
        distancedict.update({id1: 0})
        while len(q) != 0:
            tmp = q.pop(0)
            for i in self.g.all_out_edges_of_node(tmp):
                if i not in distancedict:
                    q.append(i)
                    distancedict.update({i: self.g.all_out_edges_of_node(tmp)[i] + distancedict[tmp]})
                elif (self.g.all_out_edges_of_node(tmp)[i] + distancedict[tmp]) < distancedict[i]:
                    q.append(i)
                    distancedict.update({i: self.g.all_out_edges_of_node(tmp)[i] + distancedict[tmp]})
        if not id2 in distancedict:
            return math.inf, []
        tmp2 = id2
        list.append(id2)
        while tmp2 != id1:
            for i in self.g.all_in_edges_of_node(tmp2):
                distancedict[i]
                if self.g.all_out_edges_of_node(i)[tmp2] + distancedict[i] == distancedict[tmp2]:
                    list.append(i)
                    tmp2 = i
                    break
        list.reverse()
        return distancedict[id2], list

    def SCCUtil(self, u):
        next = 0
        nextgroup = 0
        index = [None] * self.g.v_size()
        lowlink = [None] * self.g.v_size()
        onstack = [False] * self.g.v_size()
        stack = []
        groups = []
        groupid = {}
        work = [(u, 0)]
        while work:
            v, i = work[-1]
            del work[-1]
            if i == 0:
                index[v] = next
                lowlink[v] = next
                next += 1
                stack.append(v)
                onstack[v] = True
            recurse = False
            for j in self.g.all_out_edges_of_node(v).keys():
                w = j
                if index[w] == None:
                    work.append((v, j + 1))
                    work.append((w, 0))
                    recurse = True
                    break
                elif onstack[w]:
                    lowlink[v] = min(lowlink[v], index[w])
            if recurse: continue
            if index[v] == lowlink[v]:
                com = []
                while True:
                    w = stack[-1]
                    del stack[-1]
                    onstack[w] = False
                    com.append(w)
                    groupid[w] = nextgroup
                    if w == v: break
                groups.append(com)
                nextgroup += 1
            if work:
                w = v
                v, _ = work[-1]
                lowlink[v] = min(lowlink[v], lowlink[w])
        return groups

    def connected_component(self, id1: int):
        for i in self.SCCUtil(id1):
            for j in i:
                if (j == id1):
                    return i
        return list()

    def Diff(self, li1, li2):
        return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))

    def connected_components(self):
        check = list(self.g.get_all_v().keys())
        ans = list()
        for i in self.g.get_all_v().keys():
            obj = self.SCCUtil(i)
            for j in obj:
                if check.__contains__(j[0]):
                    j.reverse()
                    ans.append(j)
                    check = self.Diff(check, j)

        if not self.g.get_all_v().keys():
            ans.append(list())
        return ans

    def plot_graph(self):
        for key, val in self.g.get_all_v().items():
            x = val[0]
            y = val[1]
            plt.text(x, y, key)
            for node, _ in self.g.all_out_edges_of_node(key).items():
                x2, y2 = self.g.get_all_v()[node]
                x1, y1 = val
                plt.plot([x1, x2], [y1, y2], marker='o')
        plt.show()