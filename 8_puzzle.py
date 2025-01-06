#BFS function
def bfs(graph, start):
    queue = ([start])
    visited = set([start])
    bfs_order = []

    while queue:
        node = queue.pop()
        bfs_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return bfs_order

graph={
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[],
    5:[]
}

bfs_result=bfs(graph,0)
print(bfs_result)



#DFS FUNCTION
def dfs(graph, start):
    stack = [start]
    visited = set()  
    dfs_order = []   

    while stack:
        node = stack.pop()  

        if node not in visited:
            visited.add(node)  
            dfs_order.append(node)  
           
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return dfs_order


graph={
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[],
    5:[]
}

dfs_result=dfs(graph,0)
print(bfs_result)


#IDDFS
def iddfs(graph, start, target, max_depth):
    for depth in range(max_depth + 1):
        visited = set()  
        print(f"Searching at depth {depth}...")
        path = dfs(graph, start, target, depth, visited)
        if path:
            return path 
    return None 
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    start_node = 'A'
    target_node = 'F'
    max_depth = 4 
    path = iddfs(graph, start_node, target_node, max_depth)
    print("Path traversed:", path)
    
main()










#8 PUZZLE PROBLEM
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
