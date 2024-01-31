from collections import deque


class Graph:
    def __init__(self):
        self.node_indexes = {}
        self.adjacency_matrix = []
        self.adjacency_list = []

    def dfs_recursive(self, starting_vertex, visited):
        print(self.get_node_name(starting_vertex), end=" ")
        visited[starting_vertex] = True
        for i in range(len(self.node_indexes)):
            if i == starting_vertex:
                continue
            if self.adjacency_matrix[starting_vertex][i] == 1 and not visited[i]:
                self.dfs_recursive(i, visited)

    def get_node_name(self, index):
        for node, idx in self.node_indexes.items():
            if idx == index:
                return node
        return ""

    def add_node(self, node):
        if node not in self.node_indexes:
            index = len(self.node_indexes)
            self.node_indexes[node] = index

            # Ensure the adjacency matrix has the correct size
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * (index + 1))

            self.adjacency_list.append([])

    def add_edge(self, node1, node2):
        if node1 in self.node_indexes and node2 in self.node_indexes:
            index1 = self.node_indexes[node1]
            index2 = self.node_indexes[node2]

            # Ensure the adjacency matrix has the correct size
            while len(self.adjacency_matrix) <= index1:
                self.adjacency_matrix.append([0] * len(self.node_indexes))
            while len(self.adjacency_matrix[index1]) <= index2:
                self.adjacency_matrix[index1].append(0)

            self.adjacency_matrix[index1][index2] = 1
            self.adjacency_matrix[index2][index1] = 1
            self.adjacency_list[index1].append(index2)
            self.adjacency_list[index2].append(index1)

    def dfs(self, node):
        if node not in self.node_indexes:
            print("Node not found.")
            return
        starting_vertex = self.node_indexes[node]
        visited = [False] * len(self.node_indexes)
        print("DFS traversal:", end=" ")
        self.dfs_recursive(starting_vertex, visited)
        print()

    def bfs(self, node):
        if node not in self.node_indexes:
            print("Node not found.")
            return
        starting_vertex = self.node_indexes[node]
        visited = [False] * len(self.node_indexes)
        queue = deque()
        visited[starting_vertex] = True
        queue.append(starting_vertex)
        print("BFS traversal:", end=" ")
        while queue:
            current_node = queue.popleft()
            print(self.get_node_name(current_node), end=" ")
            for neighbor in self.adjacency_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()


def main():
    graph = Graph()
    while True:
        print("----------------Graph operation----------------------")
        print("1. Add Node.")
        print("2. Add Edge.")
        print("3. Perform DFS.")
        print("4. Perform BFS.")
        print("5. Exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            node = input("Enter the node name: ")
            graph.add_node(node)
            print("Node added:", node)
        elif choice == 2:
            node1 = input("Enter the first node: ")
            node2 = input("Enter the second node: ")
            graph.add_edge(node1, node2)
            print("Edge added between", node1, "and", node2)
        elif choice == 3:
            node = input("Enter the starting vertex for DFS: ")
            graph.dfs(node)
        elif choice == 4:
            node = input("Enter the starting vertex for BFS: ")
            graph.bfs(node)
        elif choice == 5:
            print("End of the program")
            break
        else:
            print("Invalid choice!")
        print()


if __name__ == "__main__":
    main()
