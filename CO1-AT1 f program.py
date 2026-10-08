# Complete standalone script to verify all results
def solve_warehouse_grid():
    grid_size = 5
    blocked = {(2,2), (2,3), (3,3), (4,2), (4,4)}
    start, goal = (1, 1), (5, 5)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left

    def get_neighbors(curr):
        x, y = curr
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= grid_size and 1 <= ny <= grid_size and (nx, ny) not in blocked:
                neighbors.append((nx, ny))
        return neighbors

    # BFS Run
    from collections import deque
    queue = deque([[start]])
    visited_bfs = {start}
    bfs_result = None
    
    while queue:
        path = queue.popleft()
        curr = path[-1]
        if curr == goal:
            bfs_result = path
            break
        for nbr in get_neighbors(curr):
            if nbr not in visited_bfs:
                visited_bfs.add(nbr)
                queue.append(path + [nbr])

    # DFS Run
    stack = [[start]]
    visited_dfs = {start}
    dfs_result = None
    
    while stack:
        path = stack.pop()
        curr = path[-1]
        if curr == goal:
            dfs_result = path
            break
        for nbr in reversed(get_neighbors(curr)):
            if nbr not in visited_dfs:
                visited_dfs.add(nbr)
                stack.append(path + [nbr])

    print("=== WAREHOUSE GRID SEARCH RESULTS ===")
    print(f"BFS Path: {bfs_result}")
    print(f"BFS Path Length (Cost): {len(bfs_result) - 1}")
    print(f"DFS Path: {dfs_result}")
    print(f"DFS Path Length (Cost): {len(dfs_result) - 1}")

if __name__ == "__main__":
    solve_warehouse_grid()
