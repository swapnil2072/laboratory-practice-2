class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
        self.colored = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, color, colored):
        for i in self.graph[v]:
            if colored[i] == color:
                return False
        return True

    def graph_coloring(self, m):
        colored = [-1] * self.vertices
        if not self.graph_coloring_util(0, m, colored):
            return False
        self.colored = colored
        return True

    def graph_coloring_util(self, v, m, colored):
        if v == self.vertices:
            return True

        for color in range(1, m + 1):
            if self.is_safe(v, color, colored):
                colored[v] = color
                if self.graph_coloring_util(v + 1, m, colored):
                    return True
                colored[v] = -1

        return False


def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    graph = Graph(vertices)

    print("Enter the edges (vertex pairs):")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    colors = int(input("Enter the number of colors: "))
    if graph.graph_coloring(colors):
        print("Graph can be colored with {} colors".format(colors))
        print("Coloring:", graph.colored)
    else:
        print("Graph cannot be colored with {} colors".format(colors))


if __name__ == "__main__":
    main()
