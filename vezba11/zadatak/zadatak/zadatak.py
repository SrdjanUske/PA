import math
import random

class Vertex:
    def __init__(self, d1 = None, d2 = None, in_node = None, out_node = None, p = None):
        self.d1 = d1
        self.d2 = d2
        self.in_node = in_node
        self.out_node = out_node
        self.p = p

class Edge:
    def __init__(self, source = None, dest = None, weight = None):
        self.source = source
        self.dest = dest
        self.weight = weight

def INITIALIZE_SINGLE_SOURGE(G, s):
    for vertex in G:
        vertex.d2 = math.inf
        vertex.p = Vertex()
    s.d2 = 0

def RELAX(u, v, w):
    if v.d2 > (u.d2 + w(u, v)):
        v.d2 = u.d2 + w(u, v)
        v.p = u

def w(u, v):
    for i in u.out_node:
        if i.dest == v:
            temp = i
            return temp.weight
    return -1

def extract_min(Q):
    min = Q[0]
    for i in Q:
        if min.d2 > i.d2:
            min = i
    Q.remove(min)
    return min

def BELLMAN_FORD(G, w, s):
    INITIALIZE_SINGLE_SOURGE(G, s)
    for i in range(0, len(G) - 1):
        for edge in G[i].out_node:
            RELAX(edge.source, edge.dest, w)
    for i in range(0, len(G)):
        for edge in G[i].out_node:
            if edge.dest.d2 > edge.source.d2 + w(edge.source, edge.dest):
                return False
    return True

def MakeGraph():
    global graph
    graph = []
    vertex = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for i in range(0, len(vertex)):
        graph.append(Vertex(d1 = vertex[i]))
    nodes_in = [[], ['a'], ['a'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f']]
    nodes_out = [[Edge(graph[0], graph[1], 8), Edge(graph[0], graph[2], 6)], [Edge(graph[1], graph[3], 10)], [Edge(graph[2], graph[3], 15), Edge(graph[2], graph[4], 9)], [Edge(graph[3], graph[4], 14), Edge(graph[3], graph[5], 4)], [Edge(graph[4], graph[5], 13), Edge(graph[4], graph[6], 17)], [Edge(graph[5], graph[6], 7)], []]
    
    for i in range(0, len(nodes_in)):
        graph[i].in_node = []
        for j in range(0, len(nodes_in[i])):
            graph[i].in_node.append(nodes_in[i][j])
    for i in range(0, len(nodes_out)):
        graph[i].out_node = []
        for j in range(0, len(nodes_out[i])):
            graph[i].out_node.append(nodes_out[i][j])
    return graph

def GetInDegrees(graph):
    list = []
    for elem in graph:
        list.append(len(elem.in_node))
    return list

def GetOutDegrees(graph):
    list = []
    for elem in graph:
        list.append(len(elem.out_node))
    return list

def ShortestPath(graph, nodeA, nodeB):
    if BELLMAN_FORD(graph, w, nodeA):
        list = []
        parent = nodeB
        while parent.p != None:
            list.append(parent.d1)
            parent = parent.p
        list.reverse()
        return (list, nodeB.d2)
    else:
        return None

def UpdateEdge(graph, nodeA, nodeB, weight):
    found = 0
    for egdes in nodeA.out_node:
        if egdes.dest == nodeB:
            egdes.weight = weight
            found = 1
    if found == 0:
        nodeA.out_node.append(Edge(nodeA, nodeB, weight))

def NewShortestPath():
    global graph
    if BELLMAN_FORD(graph, w, nodeA):
        list = []
        parent = nodeB
        while parent.p != None:
            list.append(parent.d1)
            parent = parent.p
        list.reverse()
        return (list, nodeB.d2)
    else:
        return None
    
    return
if __name__ == "__main__":
    print("1)")
    graph = MakeGraph()
    print("GRAPH MADE!")
    print("2)")
    inin = GetInDegrees(graph)
    out = GetOutDegrees(graph)
    print("In degrees: ", inin)
    print("Out degrees: ", out)
    
    print("3)")
    path = ShortestPath(graph, graph[0], graph[6])
    print(path)
    
    print("4)")
    UpdateEdge(graph, graph[1], graph[2], -6)
    print("w(B,C) = ", w(graph[1], graph[2]))
    
    print("5)")
    path = ShortestPath(graph, graph[0], graph[6])
    print(path)