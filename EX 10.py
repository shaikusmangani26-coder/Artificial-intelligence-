
import heapq

def astar(graph, heuristic, start, goal):
    # Priority queue: (f_cost, g_cost, current_node, path)
    open_list = [(heuristic[start], 0, start, [start])]
    g_cost = {start: 0}
    visited = set()

    while open_list:
        f, cost, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, cost

        if current in visited:
            continue

        visited.add(current)

        for neighbor, distance in graph[current].items():
            new_cost = cost + distance

            if new_cost < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (f_cost, new_cost, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Graph with edge costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Heuristic values to goal node D
heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
