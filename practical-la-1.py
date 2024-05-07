from collections import deque


def create_graph():
    graph = {}
    while True:
        node = input("Enter a node (or 'exit' to finish): ")
        if node.lower() == "exit":
            break
        neighbors = input(
            f"Enter neighbor nodes for {node} separated by spaces: "
        ).split()
        graph[node] = neighbors
    return graph


def bfs(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    if start_node not in visited:
        print(start_node, end=" ")
        visited.add(start_node)
        for neighbor in graph.get(start_node, []):
            dfs(graph, neighbor, visited)


def main():
    graph = {}

    while True:
        print(
            "--------------------------------graph operations--------------------------------"
        )
        print("1. Create graph")
        print("2. Perform BFS")
        print("3. Perform DFS")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            graph = create_graph()
        elif choice == "2":
            if not graph:
                print("Graph is empty. Create a graph first.")
                continue
            start_node = input("Enter the start node for BFS traversal: ")
            print("Following is the breadth-first search:")
            bfs(graph, start_node)
            print()  # New line for better output formatting
        elif choice == "3":
            if not graph:
                print("Graph is empty. Create a graph first.")
                continue
            start_node = input("Enter the start node for DFS traversal: ")
            print("Following is the depth-first search:")
            dfs(graph, start_node)
            print()  # New line for better output formatting
        elif choice == "4":
            print("End of the program")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
