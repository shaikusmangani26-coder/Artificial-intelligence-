
import heapq

# Graph with actual distances between locations
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

# Straight-line distance to the Auditorium
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

def astar(start, goal):
    # Priority queue stores (f value, node)
    pq = [(h[start], start)]

    # Actual distance from start
    g = {start: 0}

    parent = {start: None}
    closed = set()

    while pq:
        f, current = heapq.heappop(pq)

        if current in closed:
            continue

        print("\nExpanded:", current)

        if current == goal:
            break

        closed.add(current)

        for neighbour, cost in graph[current].items():
            new_g = g[current] + cost
            new_f = new_g + h[neighbour]

            print(
                neighbour,
                "g =", new_g,
                "h =", h[neighbour],
                "f =", new_f
            )

            if new_g < g.get(neighbour, float('inf')):
                g[neighbour] = new_g
                parent[neighbour] = current

                # Reopen a node if a better route is found
                closed.discard(neighbour)
                heapq.heappush(pq, (new_f, neighbour))

    if goal not in g:
        print("No route found.")
        return

    # Reconstruct the route
    route = []
    node = goal

    while node is not None:
        route.append(node)
        node = parent[node]

    route.reverse()

    print("\nShortest route:", " -> ".join(route))
    print("Total distance:", g[goal], "km")


astar('S', 'Auditorium')
