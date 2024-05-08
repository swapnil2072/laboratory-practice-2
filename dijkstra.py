def get_min_distance_vertex(distances, visited):
    min_vertex = -1
    min_distance = float("inf")
    for v, dist in enumerate(distances):
        if not visited[v] and dist < min_distance:
            min_vertex = v
            min_distance = dist
    return min_vertex


def print_shortest_distances(graph, num_vertices):
    distances = [float("inf")] * num_vertices
    visited = [False] * num_vertices
    distances[0] = 0

    for _ in range(num_vertices - 1):
        min_vertex = get_min_distance_vertex(distances, visited)
        visited[min_vertex] = True
        for v in range(num_vertices):
            if graph[min_vertex][v] != 0 and not visited[v]:
                dist = distances[min_vertex] + graph[min_vertex][v]
                if dist < distances[v]:
                    distances[v] = dist

    print("Vertex\tDistance from Source")
    for v, dist in enumerate(distances):
        print(f"{v}\t{dist}")


def main():
    num_vertices, num_edges = map(
        int, input("Enter number of vertices and edges: ").split()
    )
    graph = [[0] * num_vertices for _ in range(num_vertices)]

    for _ in range(num_edges):
        s, d, weight = map(
            int, input("Enter edge and weight (source dest weight): ").split()
        )
        graph[s][d] = weight
        graph[d][s] = weight

    print_shortest_distances(graph, num_vertices)


if __name__ == "__main__":
    main()
