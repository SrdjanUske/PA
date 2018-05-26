import math

class Vertex:
    def __init__(self, p = None, d1 = None, d2 = None, edges = None):
        self.p = p  
        self.d1 = d1
        self.d2 = d2
        self.edges = edges

class Edge:
    def __init__(self, source = None, dest = None, weight = None):
        self.source = source
        self.dest = dest
        self.weight = weight

def MakeGraph():
        global graph

        graph = []
        a = Vertex(d1 = 'a')
        b = Vertex(d1 = 'b')
        c = Vertex(d1 = 'c')
        d = Vertex(d1 = 'd')
        e = Vertex(d1 = 'e')
        f = Vertex(d1 = 'f')
        g = Vertex(d1 = 'g')
        h = Vertex(d1 = 'h')
        graph = [a, b, c, d, e, f, g, h]
        
        list_edges = []
        list_edges.append([Edge(a, b, 3), Edge(a, e, 2)])
        list_edges.append([Edge(b, c, 6), Edge(b, h, 3)])
        list_edges.append([Edge(c, d, 3)])
        list_edges.append([])
        list_edges.append([Edge(e, f, 2)])
        list_edges.append([Edge(f, g, 4), Edge(f, h, 3)])
        list_edges.append([Edge(g, d, 4)])
        list_edges.append([Edge(h, d, 4), Edge(h, f, 3)])

        for i in range(0, len(graph)):
            graph[i].edges = []
            for edge in list_edges[i]:
                graph[i].edges.append(edge)

        return graph

def w(u, v):
    for egde in u.edges:
        if egde.dest == v:
            return egde.weight
    return -1

def INITIALIZE_SINGLE_SOURCE(G, s):
    for v in G:
        v.d2 = math.inf
        v.p = Vertex()
    s.d2 = 0

def EXTRACT_MIN(Q):
    min = Q[0]
    for vertex in Q:
        if vertex.d2 < min.d2:
            min = vertex
    Q.remove(min)
    return min

def RELAX(u, v, w):
    if v.d2 > u.d2 + w:
        v.d2 = u.d2 + w
        v.p = u

def DIJKSTRA(G, w, s):
    INITIALIZE_SINGLE_SOURCE(G, s)
    S = []
    Q = G[:]
    while Q != []:
        u = EXTRACT_MIN(Q)
        S.append(u)
        for v in u.edges:
            RELAX(v.source, v.dest, w(v.source,  v.dest))

def ShortestPath(graph):
    DIJKSTRA(graph, w, graph[0])

    List = []
    parent = graph[3]
    while parent.p != None:
        List.append(parent.d1)            
        parent = parent.p
    List.reverse()

    return (List, graph[3].d2)

def UpdateEdge(graph, nodeB, nodeH, weight):
    exist = 0
    for edge in nodeB.edges:
        if edge.dest == nodeH:
            exist = 1
            edge.weight = weight
    if exist == 0:
        nodeB.edges.append(Edge(nodeB, nodeH, weight))