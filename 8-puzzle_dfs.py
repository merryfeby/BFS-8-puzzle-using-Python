class PuzzleState:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
        
    def __str__(self):
        result = ""
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    result += "  "
                else:
                    result += str(self.state[i][j]) + " "
            result += "\n"
        return result
    
    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j
        
    def get_children(self):
        i, j = self.find_blank()
        children = []
        
        moves = [('up', -1, 0), ('down', 1, 0), ('left', 0, -1), ('right', 0, 1)]
        
        for move_name, di, dj in moves:
            new_i, new_j = i + di, j + dj
            
            if 0 <= new_i < 3 and 0 <= new_j < 3:

                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                
                child = PuzzleState(new_state, self, move_name, self.depth + 1)
                children.append(child)
                
        return children

def dfs_solve(initial_state, goal_state):
    initial = PuzzleState(initial_state)
    goal = PuzzleState(goal_state)
    
    stack = [initial]
    visited = set()
    
    max_depth = 31  
    
    while stack:
        current = stack.pop()  
        
        
        if current == goal:
            
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1]  
        
        state_str = str(current.state)
        if state_str in visited or current.depth >= max_depth:
            continue
            
        visited.add(state_str)
        
     
        for child in current.get_children():
            stack.append(child)
    
    return None  

def print_solution(path):
    if not path:
        print("No solution found.")
        return
    
    print("Initial State:")
    print(path[0])
    
    for i in range(1, len(path)):
        print(f"Step {i}: Move {path[i].move}")
        print(path[i])
    
    print(f"Solution found in {len(path)-1} steps.")

# initial state 
initial_state = [
    [1, 3, 0],
    [4, 2, 5],
    [7, 8, 6]
]

# Goal state: 1,2,3 / 4,5,6 / 7,8,0
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = dfs_solve(initial_state, goal_state)

print_solution(solution)