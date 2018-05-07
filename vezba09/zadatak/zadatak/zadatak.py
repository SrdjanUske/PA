from enum import Enum
import math



class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, obj = None, s = None, f = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.obj = obj
        self.s = s
        self.f = f

    def printVertex(self):
        print(self.d1)

    def printNodes(self):
        print("Nodes for vertex " + self.d1 + ":")
        for i in range(0, len(self.obj)):
            self.obj[i].printVertex()

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255
		

def printRelation(list):
    print("Relations for vertex " + list.d1)
    for vertex in list.obj:
        print(list.d1 + " -> " + vertex.d1)

def BFS(G, s):
    for elem in G:
        if elem != s:
            elem.c = VertexColor.WHITE
            elem.d2 = math.inf
            elem.p = None
    s.c = VertexColor.GRAY
    s.d2 = 0
    s.p = None
    list = []
    list.append(s)
    while list != []:
        u = list.pop(0)
        for v in u.obj:
            if v.c == VertexColor.WHITE:
                v.c = VertexColor.GRAY
                v.d2 = u.d2 + 1
                v.p = u
                list.append(v)
        u.color = VertexColor.BLACK

def PRINT_PATH(G, s, v):
    if v.d1 == s.d1:
        print(s.d1)
    elif v.p == None:
        print("No path from " + s.d1 + " to " + v.d1 + " exists")
    else:
        PRINT_PATH(G, s, v.p)
        print(v.d1)

def DFS_Visit(G, u):
    global time, lista
    time += 1
    u.s = time
    u.c = VertexColor.GRAY
    for v in u.obj:
        if v.c == VertexColor.WHITE:
            v.p = u
            DFS_Visit(G, v)
    u.c = VertexColor.BLACK
    time += 1
    u.f = time
    lista = [u] + lista      

def DFS(G):
    global time
    for u in G:
        u.c = VertexColor.WHITE
        u.p = None
    time = 0
    for u in G:
        if u.c == VertexColor.WHITE:
            DFS_Visit(G, u)     

def TOPOLOGICAL_SORT(G):
    global lista
    DFS(G)    
    return lista    

def printVertex(obj):
    print(obj.d1 + ": " + "Start: " + str(obj.s) + " , Finish: " + str(obj.f))

if __name__ == "__main__":
    # 1)
    print("ZADATAK 1")
    print("----------")
    list = []
    vertex = ['A', 'B', 'C', 'D', 'E']
    for i in range(0, len(vertex)):
        list.append(Vertex(d1 = vertex[i]))
    nodes = [[list[1], list[2]], [list[0], list[2], list[3], list[4]], [list[0], list[1]], [list[1]], [list[1]]]
    for i in range(0, len(nodes)):
        list[i].obj = []
        for j in range(0, len(nodes[i])):
            list[i].obj.append(nodes[i][j])
    print("(i)")
    for i in range(0, len(nodes)):
        list[i].printNodes()
    print("\n(ii)")
    for i in range(0, len(list)):
        printRelation(list[i])

    # 2)
    print("\nZADATAK 2")
    print("----------")
    list = []
    vertex = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    for i in range(0, len(vertex)):
        list.append(Vertex(d1 = vertex[i]))
    nodes = [[list[1], list[4]], [list[0], list[5]], [list[3], list[5], list[6]], [list[2], list[6], list[7]], [list[0]], [list[1], list[2], list[6]], [list[2], list[3], list[5], list[7]], [list[3], list[6]]]
    for i in range(0, len(nodes)):
        list[i].obj = []
        for j in range(0, len(nodes[i])):
            list[i].obj.append(nodes[i][j])

    BFS(list, list[1])
    print("Path from " + list[1].d1 + " to " + list[4].d1 + ":")
    PRINT_PATH(list, list[1], list[4])

    # 3)
    print("\nZADATAK 3")
    print("----------")
    time = 0
    list = []
    lista = []
    vertex = ['u', 'v', 'w', 'x', 'y', 'z']
    for i in range(0, len(vertex)):
        list.append(Vertex(d1 = vertex[i]))
    nodes = [[list[1], list[3]], [list[4]], [list[4], list[5]], [list[1]], [list[4]], [list[5]]]
    for i in range(0, len(nodes)):
        list[i].obj = []
        for j in range(0, len(nodes[i])):
            list[i].obj.append(nodes[i][j])
    DFS(list)
    for i in range(0, len(lista)):
        printVertex(lista[i])

    # 4)
    print("\nZADATAK 4")
    print("----------")
    list = []
    lista = []
    vertex = ['undershorts', 'socks', 'watch', 'pants', 'shoes', 'shirt', 'belt', 'tie', 'jacket']
    for i in range(0, len(vertex)):
        list.append(Vertex(d1 = vertex[i]))
    nodes = [[list[3], list[4]], [list[4]], [], [list[4], list[6]], [], [list[6], list[7]], [list[8]], [list[8]], []]
    for i in range(0, len(nodes)):
        list[i].obj = []
        for j in range(0, len(nodes[i])):
            list[i].obj.append(nodes[i][j])

    lista = TOPOLOGICAL_SORT(list)
    for i in range(0, len(lista)):
        printVertex(lista[i])
    