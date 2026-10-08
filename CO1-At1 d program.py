from collections import deque

GRID_SIZE = 5
BLOCKED = {(2,2), (2,3), (3,3), (4,2), (4,4)}
START = (1, 1)
GOAL = (5, 5)

# Actions: Down, Right, Up, Left
MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        x, y = node
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= GRID_SIZE and 1 <= ny <= GRID_SIZE:
                if (nx, ny) not in BLOCKED and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(path + [(nx, ny)])
    return None

path = bfs(START, GOAL)
print("BFS Path:", path)
print("BFS Cost:", len(path) - 1)
