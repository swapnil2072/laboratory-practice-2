import copy


class PuzzleNode:

    def __init__(self, state_matrix, level, f_val):
        self.state_matrix = state_matrix
        self.level = level
        self.f_val = f_val

    def generate_children(self):
        empty_cell = self.find_empty_cell(self.state_matrix)

        if empty_cell is None:
            return []

        x, y = empty_cell
        possible_moves = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []

        for move in possible_moves:
            child_state = self.move_tile(self.state_matrix, x, y, move[0], move[1])
            if child_state is not None:
                child_node = PuzzleNode(child_state, self.level + 1, 0)
                children.append(child_node)
        return children

    def find_empty_cell(self, state_matrix):
        for i in range(len(state_matrix)):
            for j in range(len(state_matrix)):
                if state_matrix[i][j] == "-":
                    return (i, j)

    def move_tile(self, state_matrix, x1, y1, x2, y2):
        size = len(state_matrix)

        if 0 <= x2 < size and 0 <= y2 < size:
            new_state = copy.deepcopy(state_matrix)
            temp = new_state[x2][y2]
            new_state[x2][y2] = new_state[x1][y1]
            new_state[x1][y1] = temp
            return new_state
        else:
            return None


class PuzzleSolver:
    def __init__(
        self,
        size,
    ):
        self.size = size
        self.open_list = []
        self.closed_list = []

    def accept_matrix(self):
        matrix = []

        for _ in range(self.size):
            row = input("Enter the row elements separated by space1 :").split()
            processed_row = []
            for cell in row:
                if cell == "-":
                    processed_row.append(cell)
                else:
                    processed_row.append(int(cell))
            matrix.append(processed_row)
        return matrix

    def calculate_f_value(self, current_node, goal_matrix):
        return (
            self.calculate_heuristic_value(current_node.state_matrix, goal_matrix)
            + current_node.level
        )

    def calculate_heuristic_value(self, current_state, goal_matrix):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if (
                    current_state[i][j] != goal_matrix[i][j]
                    and current_state[i][j] != "_"
                    and current_state[i][j] != "-"
                ):
                    count += 1
        return count

    def process_puzzle(self):
        print("Enter the Start state matrix ")
        start_matrix = self.accept_matrix()
        print("Enter the End state matrix ")
        goal_matrix = self.accept_matrix()

        start_node = PuzzleNode(start_matrix, 0, 0)

        start_node.f_value = self.calculate_f_value(start_node, goal_matrix)

        self.open_list.append(start_node)

        while True:
            current_node = self.open_list[0]

            print("\nCurrent State:")
            for row in current_node.state_matrix:
                print(" ".join(map(str, row)))

            if (
                self.calculate_heuristic_value(current_node.state_matrix, goal_matrix)
                == 0
            ):
                print("Goal State found")
                break

            for child_node in current_node.generate_children():
                child_node.f_val = self.calculate_f_value(child_node, goal_matrix)
                self.open_list.append(child_node)

            self.closed_list.append(current_node)
            del self.open_list[0]
            self.open_list.sort(key=lambda x: x.f_val, reverse=False)


puzzleSolver = PuzzleSolver(3)
puzzleSolver.process_puzzle()
