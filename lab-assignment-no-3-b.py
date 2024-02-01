class GraphMST:
    def __init__(self):
        self.node_indexes = {}
        self.adjacency_matrix = []
        self.adjacency_list = []

    def add_node(self, node):
        if node not in self.node_indexes:
            index = len(self.node_indexes)
            self.node_indexes[node] = index

            # Ensure the adjacency matrix has the correct size
            for row in self.adjacency_matrix:
                row.append(float("inf"))
            self.adjacency_matrix.append([float("inf")] * (index + 1))

            self.adjacency_list.append([])

    def add_edge(self, node1, node2, weight):
        if node1 in self.node_indexes and node2 in self.node_indexes:
            index1 = self.node_indexes[node1]
            index2 = self.node_indexes[node2]

            # Ensure the adjacency matrix has the correct size
            while len(self.adjacency_matrix) <= index1:
                self.adjacency_matrix.append([float("inf")] * len(self.node_indexes))
            while len(self.adjacency_matrix[index1]) <= index2:
                self.adjacency_matrix[index1].append(float("inf"))

            self.adjacency_matrix[index1][index2] = weight
            self.adjacency_matrix[index2][index1] = weight
            self.adjacency_list[index1].append((index2, weight))
            self.adjacency_list[index2].append((index1, weight))

    def prim_mst(self):
        n = len(self.node_indexes)
        visited = [False] * n
        parent = [-1] * n
        key = [float("inf")] * n

        key[0] = 0  # Start with the first node

        for _ in range(n):
            u = self._min_key_vertex(key, visited)
            visited[u] = True

            for v, weight in self.adjacency_list[u]:
                if not visited[v] and weight < key[v]:
                    parent[v] = u
                    key[v] = weight

        self.display_mst(parent)

    def _min_key_vertex(self, key, visited):
        min_key = float("inf")
        min_index = -1

        for i in range(len(key)):
            if not visited[i] and key[i] < min_key:
                min_key = key[i]
                min_index = i

        return min_index

    def display_mst(self, parent):
        print("Minimum Spanning Tree:")
        for i in range(1, len(parent)):
            print(
                f"Edge: {self.get_node_name(parent[i])} - {self.get_node_name(i)}, Weight: {self.adjacency_matrix[i][parent[i]]}"
            )

    def get_node_name(self, index):
        for node, idx in self.node_indexes.items():
            if idx == index:
                return node
        return ""


def main():
    graph_mst = GraphMST()

    while True:
        print("----------------Minimum Spanning Tree----------------------")
        print("1. Add Node.")
        print("2. Add Edge.")
        print("3. Find Minimum Spanning Tree (Prim's Algorithm).")
        print("4. Exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            node = input("Enter the node name: ")
            graph_mst.add_node(node)
            print("Node added:", node)

        elif choice == 2:
            node1 = input("Enter the first node: ")
            node2 = input("Enter the second node: ")
            weight = float(input("Enter the edge weight: "))
            graph_mst.add_edge(node1, node2, weight)
            print(f"Edge added between {node1} and {node2} with weight {weight}")

        elif choice == 3:
            graph_mst.prim_mst()

        elif choice == 4:
            print("End of the program")
            break

        else:
            print("Invalid choice!")

        print()


if __name__ == "__main__":
    main()
