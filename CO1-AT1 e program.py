def dfs(start, goal):
    stack = [[start]]
    visited = {start}
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
            
        x, y = node
        # Reverse move order so Down is popped first from LIFO stack
        for dx, dy in reversed(MOVES):
            nx, ny = x + dx, y + dy
            if 1 <= nx <= GRID_SIZE and 1 <= ny <= GRID_SIZE:
                if (nx, ny) not in BLOCKED and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append(path + [(nx, ny)])
    return None

path_dfs = dfs(START, GOAL)
print("DFS Path:", path_dfs)
print("DFS Cost:", len(path_dfs) - 1)
