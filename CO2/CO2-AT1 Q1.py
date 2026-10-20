
import heapq

# Map: neighbouring locations and actual travel distances
graph = {
    'S': {'A': 4, 'B': 2, 'C': 7},
    'A': {'S': 4, 'D': 3},
    'B': {'S': 2, 'D': 5, 'E': 4},
    'C': {'S': 7, 'E': 2},
    'D': {'A': 3, 'B': 5, 'G': 6},
    'E': {'B': 4, 'C': 2, 'G': 3},
    'G': {'D': 6, 'E': 3, 'Auditorium': 2},
    'Auditorium': {'G': 2}
}

# Straight-line heuristic distances to the Auditorium
h = {
    'S': 8,
    'A': 6,
    'B': 5,
    'C': 6,
    'D': 4,
    'E': 3,
    'G': 2,
    'Auditorium': 0
}

def greedy_best_first_search(start, goal):
    pq = [(h[start], start)]
    visited = set()
    parent = {start: None}

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        print("Expanded:", current)

        if current == goal:
            break

        for neighbour, distance in graph[current].items():
            if neighbour not in visited and neighbour not in parent:
                parent[neighbour] = current
                heapq.heappush(pq, (h[neighbour], neighbour))

    if goal not in visited:
        print("No route found.")
        return

    # Reconstruct route
    route = []
    node = goal

    while node is not None:
        route.append(node)
        node = parent[node]

    route.reverse()

    # Calculate actual travel distance
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i + 1]]

    print("Route:", " -> ".join(route))
    print("Total distance:", total_distance)

greedy_best_first_search('S', 'Auditorium')
