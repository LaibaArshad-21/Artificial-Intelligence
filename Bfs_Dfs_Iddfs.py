def bfs(graph, start):
    visited = []  
    queue = [start]

    while queue:
        node = queue.pop(0)  

        if node not in visited:
            print(node, end=' ')  
            visited.append(node)  

           
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
    return visited


def dls(node, goal, depth, graph, visited):
    if depth == 0 and node == goal:
        return True
    if depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(neighbor, goal, depth - 1, graph, visited):
                    return True
        visited.remove(node)
    return False

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        visited = set()
        if dls(start, goal, depth, graph, visited):
            print(f"Goal found at depth {depth}")
            return True
    print("Goal not found")
    return False




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


bfs(graph, 'A')
print()
dfs(graph,'A')
print()
iddfs(graph, 'A', 'F', 3)





class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = 3

    def is_goal(self):
        return self.board == self.goal

    def find_zero(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    return i, j

    def generate_moves(self):
        zero_row, zero_col = self.find_zero()
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < self.n and 0 <= new_col < self.n:
                new_board = [row[:] for row in self.board]
                new_board[zero_row][zero_col], new_board[new_row][new_col] = (
                    new_board[new_row][new_col],
                    new_board[zero_row][zero_col],
                )
                moves.append(Puzzle(new_board, self.goal))
        return moves

    def dfs(self, depth):
        if self.is_goal():
            return True
        if depth <= 0:
            return False
        for move in self.generate_moves():
            if move.dfs(depth - 1):
                return True
        return False

def iddfs(puzzle, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if puzzle.dfs(depth):
            return True
    return False

initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

puzzle = Puzzle(initial_state, goal_state)

if iddfs(puzzle, 20):
    print("Goal state found!")
else:
    print("Goal state not found.")