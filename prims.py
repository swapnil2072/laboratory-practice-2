'''
Time complexity : O(E * log(V))
Space complexity : O(V^2)
'''
import sys


class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [
            [0 for _ in range(num_vertices)] for _ in range(num_vertices)
        ]

    def add_edge(self, v1, v2, weight):
        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight

    def get_min_vertex(self, visited, weight):
        min_vertex = -1
        for i in range(self.num_vertices):
            if not visited[i] and (min_vertex == -1 or weight[i] < weight[min_vertex]):
                min_vertex = i
        return min_vertex

    def prims_algorithm(self):
        visited = [False for _ in range(self.num_vertices)]
        parent = [-1 for _ in range(self.num_vertices)]
        weight = [sys.maxsize for _ in range(self.num_vertices)]

        for _ in range(self.num_vertices - 1):
            min_vertex = self.get_min_vertex(visited, weight)
            visited[min_vertex] = True
            for j in range(self.num_vertices):
                if (
                    self.adj_matrix[min_vertex][j] != 0
                    and not visited[j]
                    and self.adj_matrix[min_vertex][j] < weight[j]
                ):
                    weight[j] = self.adj_matrix[min_vertex][j]
                    parent[j] = min_vertex

        print("Edges in the Minimum Spanning Tree:")
        for i in range(1, self.num_vertices):
            if parent[i] > i:
                print(f"{i} {parent[i]} {weight[i]}")
            else:
                print(f"{parent[i]} {i} {weight[i]}")


num_vertices, num_edges = map(
    int, input("Enter the number of vertices and edges: ").split()
)

g = Graph(num_vertices)

print("Enter edges as 'src dest weight' (space separated):")
for _ in range(num_edges):
    src, dest, weight = map(int, input().split())
    g.add_edge(src, dest, weight)

g.prims_algorithm()
