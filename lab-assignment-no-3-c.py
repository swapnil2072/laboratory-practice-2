import heapq


class GraphShortestPath:
    def __init__(self):
        self.node_indexes = {}
        self.adjacency_list = []

    def add_node(self, node):
        if node not in self.node_indexes:
            index = len(self.node_indexes)
            self.node_indexes[node] = index
            self.adjacency_list.append([])

    def add_edge(self, node1, node2, weight):
        if node1 in self.node_indexes and node2 in self.node_indexes:
            index1 = self.node_indexes[node1]
            index2 = self.node_indexes[node2]

            self.adjacency_list[index1].append((index2, weight))
            self.adjacency_list[index2].append((index1, weight))

    def dijkstra_shortest_path(self, start_node):
        if start_node not in self.node_indexes:
            print("Start node not found.")
            return

        start_index = self.node_indexes[start_node]
        n = len(self.node_indexes)

        distance = [float("inf")] * n
        distance[start_index] = 0

        priority_queue = [(0, start_index)]  # (distance, node_index)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distance[current_node]:
                continue

            for neighbor, edge_weight in self.adjacency_list[current_node]:
                new_distance = current_distance + edge_weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        self.display_shortest_paths(start_node, distance)

    def display_shortest_paths(self, start_node, distance):
        print("Shortest Paths from", start_node, ":")
        for node, idx in self.node_indexes.items():
            print(f"To {node}: {distance[idx]}")

    def get_node_name(self, index):
        for node, idx in self.node_indexes.items():
            if idx == index:
                return node
        return ""


def main():
    graph_shortest_path = GraphShortestPath()

    while True:
        print("----------------Single-Source Shortest Path----------------------")
        print("1. Add Node.")
        print("2. Add Edge.")
        print("3. Find Shortest Paths (Dijkstra's Algorithm).")
        print("4. Exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            node = input("Enter the node name: ")
            graph_shortest_path.add_node(node)
            print("Node added:", node)

        elif choice == 2:
            node1 = input("Enter the first node: ")
            node2 = input("Enter the second node: ")
            weight = float(input("Enter the edge weight: "))
            graph_shortest_path.add_edge(node1, node2, weight)
            print(f"Edge added between {node1} and {node2} with weight {weight}")

        elif choice == 3:
            start_node = input("Enter the starting node for Dijkstra's Algorithm: ")
            graph_shortest_path.dijkstra_shortest_path(start_node)

        elif choice == 4:
            print("End of the program")
            break

        else:
            print("Invalid choice!")

        print()


if __name__ == "__main__":
    main()
