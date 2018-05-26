from vertex import *

if __name__ == "__main__":
    print("1)")
    graph = []
    graph = MakeGraph()
    for vertex in graph:
        print(vertex.d1)
        for edge in vertex.edges:
            print(str(edge.source.d1) + " " + str(edge.dest.d1) + " " + str(edge.weight))
        print("-----------------")
    print("\n2)")
    print(ShortestPath(graph))
    print("\n3)")
    UpdateEdge(graph, graph[1], graph[7], 5)
    print(ShortestPath(graph))