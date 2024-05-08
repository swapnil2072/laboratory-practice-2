class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


def find_parent(vertex, parent):
    if vertex == parent[vertex]:
        return vertex
    return find_parent(parent[vertex], parent)


def kruskal_algorithm(edges, num_vertices, num_edges):
    edges = sorted(edges, key=lambda edge: edge.weight)
    output = []

    parent = [i for i in range(num_vertices)]
    count = 0
    i = 0
    while count < num_vertices - 1:
        current_edge = edges[i]
        src_parent = find_parent(current_edge.src, parent)
        dest_parent = find_parent(current_edge.dest, parent)

        if src_parent != dest_parent:
            output.append(current_edge)
            parent[src_parent] = dest_parent
            count += 1
        i += 1
    return output


def get_input():
    num_vertices, num_edges = map(
        int, input("Enter the number of vertices and edges: ").split()
    )
    edges = []

    for _ in range(num_edges):
        src, dest, weight = map(
            int, input("Enter source, destination, and weight for edge: ").split()
        )
        edge = Edge(src, dest, weight)
        edges.append(edge)

    return num_vertices, num_edges, edges


def print_output(edges):
    print("Edges in the Minimum Spanning Tree:")
    for edge in edges:
        if edge.src < edge.dest:
            print(f"{edge.src} {edge.dest} {edge.weight}")
        else:
            print(f"{edge.dest} {edge.src} {edge.weight}")


def main():
    num_vertices, num_edges, edges = get_input()
    output_edges = kruskal_algorithm(edges, num_vertices, num_edges)
    print_output(output_edges)


if __name__ == "__main__":
    main()
