
# Travelling Salesman Problem using Greedy Search

def tsp_greedy(graph, start):
    n = len(graph)
    visited = [False] * n
    tour = [start]
    total_cost = 0
    current = start

    visited[current] = True

    for _ in range(n - 1):
        nearest = -1
        min_distance = float('inf')

        for city in range(n):
            if not visited[city] and graph[current][city] < min_distance:
                min_distance = graph[current][city]
                nearest = city

        if nearest == -1:
            return None, float('inf')

        tour.append(nearest)
        total_cost += min_distance
        visited[nearest] = True
        current = nearest

    # Return to the starting city
    total_cost += graph[current][start]
    tour.append(start)

    return tour, total_cost


# Distance matrix between cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ["A", "B", "C", "D"]

tour, cost = tsp_greedy(graph, 0)

if tour is not None:
    print("Tour:", " -> ".join(cities[i] for i in tour))
    print("Total Distance:", cost)
else:
    print("No valid tour exists.")
