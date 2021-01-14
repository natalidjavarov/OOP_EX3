# ex3
READ ME
Task number 3 from OOP course, Ariel University.
Authors: Natali Djavarov and Liron Asaraf.
About the task:                                                                                                    
In this task we were required to implement a directed and weighted graph with all the algorithms similar to the previous task only in the Python programming language (Links to previous assignments about graphs in Java will appear below).
The goal of the task is that we were required to compare execution times between our results and the networkx and Java library and also implemented a graphical representation of the graph using maplotlib library in Python, the results we were write in Wiki.
Workspace:                                                                                                         
PyCharm
Linux
macOs
How it works?                                                                                                      
Copy the link from this git and clone it to your workspace.
After the project is open in your workspace you can check it by using the class of Ex3 main, you can copy it from here:
    g = DiGraph()  # creates an empty directed graph
for n in range(4):
    g.add_node(n)
g.add_edge(0, 1, 1)
g.add_edge(1, 0, 1.1)

g.add_edge(1, 2, 1.3)
g.add_edge(2, 3, 1.1)
g.add_edge(1, 3, 1.9)
g.remove_edge(1, 3)
g.add_edge(1, 3, 10)
print(g)  # prints the __repr__ (func output)
print(g.get_all_v())  # prints a dict with all the graph's vertices.
print(g.all_in_edges_of_node(1))
print(g.all_out_edges_of_node(1))
g_algo = GraphAlgo(g)
print(g_algo.shortest_path(0, 3))
g_algo.plot_graph()

About the classes:                                                                                                
Vertex:
•	__init__(self,key: tuple = None): init all the data of the node.
•	getKey(self): return the key of the vertex.
•	getLocation(self): return the location of the vertex.
•	setLocation(self, p: GeoLocation): set the location of the vertex.
•	 getWeight(self): return the weight of the vertex.    
•	setWeight(self,w:float): set the weight of the vertex.
•	getInfo(self): return the info of the vertex.
•	setInfo(self,s:str): set the info of the vertex.    
•	getTag(self): return the tag of the vertex.
•	setTag(self,t:int): set the tag of the vertex.
    
DiGraph Class :
•	init(self): Init this graph.
•	v_size(self): Returns the number of vertices in this graph.
•	e_size(self): Returns the number of edges in this graph.
•	all_in_edges_of_node(self, id1: int): return a dictionary of all the nodes connected to (into) node_id, each node is represented using a pair (key, weight).
•	all_out_edges_of_node(self, id1: int): return a dictionary of all the nodes connected from node_id, each node is represented using a pair (key, weight).
•	get_mc(self): Returns the current version of this graph, on every change in the graph state we count to represent the current graph.
•	add_edge(self, id1: int, id2: int, weight: float): Adds an edge to the graph return: True if the edge was added successfully, else return false.
•	add_node(self, node_id: int, pos: tuple = None): Adds a node to the graph return: True if the node was added successfully, else return false.
•	remove_node(self, node_id: int): Removes a node from the graph it will return true if it removed successfully, else return false.
•	remove_edge(self, node_id1: int, node_id2: int): Removes an edge from the graph return, it will return true if the edge removed successfully, else return false.
GraphAlgo Class :
•	init (self, g: tuple = None): init the graph.
•	get_graph(self): return this graph
•	load_from_json(self,file:str): Loads a graph from a json file.
•	save_to_json: save a graph to a json file.
•	Shortest_path(self, id1: int, id2: int): Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
•	connected_component(self, id1: int): list: Finds the Strongly Connected Component(SCC) that node id1 is a part of.
•	plot_graph(self): Plots the graph If the nodes have a position, the nodes will be placed there Otherwise, they will be placed in a random but elegant manner using matplot lib libarary.
                                                                                                     
External links:                                                                                                      
Ex2 assignment: https://github.com/natalidjavarov/ex2.git

Dijkstra's Algorithms:
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Matplotlib:
https://matplotlib.org/3.1.1/gallery/style_sheets/dark_background.html

