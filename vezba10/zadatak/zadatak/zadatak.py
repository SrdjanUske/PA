import math
import random

def generate_random_graph():
    number_of_vertexes = random.randint(3, 10)
    vertexi = []
    for i in range(1, number_of_vertexes+1):
        vertexi.append(Vertex(d1=i))
    for vertex in vertexi:
        number_of_edges = random.randint(0, number_of_vertexes)
        vertex.edges = []
        for i in range(0, number_of_edges):
            vertex.edges.append(Edge(source=vertex, dest=vertexi[random.randint(0, number_of_vertexes-1)], weight=random.randint(0, 15)))

    return vertexi

class Vertex:
    def __init__(self, d1 = None, d2 = None, edges = None, p = None):
        self.d1 = d1
        self.d2 = d2
        self.edges = edges
        self.p = p

class Edge:
    def __init__(self, source = None, dest = None, weight = None):
        self.source = source
        self.dest = dest
        self.weight = weight

def initialize_single_source(G, s):
    for vertex in G:
        vertex.d2 = math.inf
        vertex.p = Vertex()
    s.d2 = 0

def relax(u, v, w):
    if v.d2 > (u.d2 + w(u, v)):
        v.d2 = u.d2 + w(u, v)
        v.p = u

def w(u, v):
    for i in u.edges:
        if i.dest == v:
            temp = i
    return temp.weight

def extract_min(Q):
    min = Q[0]
    for i in Q:
        if min.d2 > i.d2:
            min = i

    Q.remove(min)
    return min

def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    Q = G[:]
    while Q != []:
        u = extract_min(Q)
        S.append(u)
        for edge in u.edges:
            relax(edge.source, edge.dest, w)

if __name__ == "__main__":
    list = []
    vertex = ['s', 't', 'x', 'y', 'z']
    for i in range(0, len(vertex)):
        list.append(Vertex(d1 = vertex[i]))
    nodes = [[Edge(list[0], list[1], 10), Edge(list[0], list[3], 5)], [Edge(list[1], list[2], 1), Edge(list[1], list[3], 2)], [Edge(list[2], list[4], 4)], [Edge(list[3], list[1], 3), Edge(list[3], list[2], 9), Edge(list[3], list[4], 2)], [Edge(list[4], list[0], 7), Edge(list[4], list[2], 6)]]
    for i in range(0, len(nodes)):
        list[i].edges = []
        for j in range(0, len(nodes[i])):
            list[i].edges.append(nodes[i][j])
    print("Zadatak 1")
    for v in list:
        print("-------------")
        for e in v.edges:
            print(e.source.d1, e.dest.d1, e.weight)
    print("-------------")

    print("Zadatak 2")
    dijkstra(list, w, list[0])
    for vertex in list:
        print(vertex.d1, vertex.d2)

    print("Zadatak 3")
    rand_list = generate_random_graph()
    for v in rand_list:
        print("-------------")
        for e in v.edges:
            print(e.source.d1, e.dest.d1, e.weight)
    print("-------------")
    dijkstra(rand_list, w, rand_list[0])
    for vertex in rand_list:
        print(vertex.d1, vertex.d2)